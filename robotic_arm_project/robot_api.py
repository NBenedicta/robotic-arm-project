from geometry_msgs.msg import PoseStamped
from moveit.planning import MoveItPy
from moveit_configs_utils import MoveItConfigsBuilder


class RobotAPI:

    def __init__(self):
        print("Initializing MoveItPy...")

        moveit_config = (
            MoveItConfigsBuilder(
                "panda",
                package_name="moveit_resources_panda_moveit_config"
            )
            .robot_description()
            .robot_description_semantic()
            .robot_description_kinematics()
            .planning_pipelines(
                pipelines=["ompl"],
                default_planning_pipeline="ompl"
            )
            .trajectory_execution()
            .to_moveit_configs()
        )

        config = moveit_config.to_dict()

        config["planning_pipelines"] = {
            "pipeline_names": ["ompl"],
            "default_planning_pipeline": "ompl",
        }

        config["plan_request_params"] = {
            "planning_pipeline": "ompl",
            "planner_id": "RRTConnectkConfigDefault",
            "planning_time": 5.0,
            "planning_attempts": 10,
            "max_velocity_scaling_factor": 0.5,
            "max_acceleration_scaling_factor": 0.5,
        }

        config["ompl"]["planning_plugins"] = ["ompl_interface/OMPLPlanner"]

        self.panda = MoveItPy(
            node_name="moveit_py",
            config_dict=config
        )

        self.arm = self.panda.get_planning_component("panda_arm")

        print("Connected to MoveIt!")

    def plan_named_motion(self, start_name, goal_name):
        print(f"Planning motion from {start_name} to {goal_name}...")

        self.arm.set_start_state(configuration_name=start_name)
        self.arm.set_goal_state(configuration_name=goal_name)

        plan_result = self.arm.plan()

        if plan_result:
            print(f"Plan successful: {start_name} -> {goal_name}")
            print("Executing trajectory...")
            self.panda.execute(plan_result.trajectory, controllers=["panda_arm_controller"])
            print("Execution complete.")
        else:
            print(f"Planning failed: {start_name} -> {goal_name}")

    def plan_to_xyz(self, x, y, z, label="target"):
        print(f"Planning to {label}: x={x}, y={y}, z={z}")

        target_pose = PoseStamped()
        target_pose.header.frame_id = "panda_link0"

        target_pose.pose.position.x = x
        target_pose.pose.position.y = y
        target_pose.pose.position.z = z

        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0

        self.arm.set_start_state_to_current_state()
        self.arm.set_goal_state(
            pose_stamped_msg=target_pose,
            pose_link="panda_hand"
        )

        plan_result = self.arm.plan()

        if plan_result:
            print(f"Plan successful to {label}.")
            print("Executing trajectory...")
            self.panda.execute(plan_result.trajectory, controllers=["panda_arm_controller"])
            print("Execution complete.")
        else:
            print(f"Planning failed to {label}.")