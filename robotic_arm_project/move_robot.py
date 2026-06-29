#!/usr/bin/env python3

from robotic_arm_project.pick_and_place import PickAndPlacePipeline
import os
import rclpy
from rclpy.node import Node

from robotic_arm_project.robot_api import RobotAPI


class RobotController(Node):

    def __init__(self):

        super().__init__("robot_controller")

        self.get_logger().info("Robot Controller Started!")

        self.robot = RobotAPI()

        self.get_logger().info("MoveIt Connected Successfully!")


def main(args=None):
    rclpy.init(args=args)

    node = RobotController()

    pipeline = PickAndPlacePipeline(node.robot)
    pipeline.run_demo()
    node.get_logger().info("Motion test complete.")

    os._exit(0)


if __name__ == "__main__":
    main()