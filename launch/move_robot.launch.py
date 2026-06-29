from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("panda", package_name="moveit_resources_panda_moveit_config")
        .robot_description()
        .robot_description_semantic()
        .robot_description_kinematics()
        .planning_pipelines()
        .trajectory_execution()
        .to_moveit_configs()
    )

    move_robot_node = Node(
        package="robotic_arm_project",
        executable="move_robot",
        output="screen",
        parameters=[moveit_config.to_dict()],
    )

    return LaunchDescription([move_robot_node])