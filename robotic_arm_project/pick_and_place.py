class PickAndPlacePipeline:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        print("Starting clean Point A to Point B demo...")

        self.robot.plan_named_motion("ready", "extended")
        self.robot.plan_to_xyz(0.35, 0.20, 0.45, "Point A")
        self.robot.plan_to_xyz(0.55, -0.20, 0.45, "Point B")

        print("Robot moved from Point A to Point B.")