class PickAndPlacePipeline:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        print("Starting pick-and-place demo pipeline...")

        self.robot.plan_to_xyz(0.35, 0.20, 0.45, "Approach Point A")
        self.robot.plan_to_xyz(0.35, 0.20, 0.30, "Lower to Pick Point")
        self.robot.plan_to_xyz(0.35, 0.20, 0.45, "Lift Object")
        self.robot.plan_to_xyz(0.45, -0.20, 0.45, "Move to Place Area")
        self.robot.plan_to_xyz(0.45, -0.20, 0.35, "Lower to Place Point")

        print("Pick-and-place demo planning complete.")