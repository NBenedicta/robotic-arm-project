class PickAndPlacePipeline:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        print("Starting Point A to Point B robotic arm motion...")

        self.robot.plan_named_motion("ready", "extended")
        self.robot.plan_to_xyz(0.35, 0.20, 0.45, "Point A")
        self.robot.plan_to_xyz(0.55, -0.20, 0.45, "Point B")

        print("Robot arm completed Point A to Point B motion.")