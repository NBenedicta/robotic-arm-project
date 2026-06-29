# System Architecture

## Overview

This project uses ROS 2 Jazzy, MoveIt 2, and MoveItPy to plan robotic arm trajectories for the Franka Panda robot.

## Main Components

### `move_robot.py`

Main ROS 2 entry point. It initializes the robot controller and starts the demo pipeline.

### `robot_api.py`

Provides the robot interface. It initializes MoveItPy, loads the Panda robot configuration, connects to the `panda_arm` planning group, and plans trajectories to named poses or Cartesian XYZ targets.

### `pick_and_place.py`

Defines a multi-step pick-and-place planning sequence:
1. Approach object
2. Lower to pick point
3. Lift object
4. Move to place area
5. Lower to place point

## Motion Planning Flow

```text
User / Demo Pipeline
        ↓
RobotAPI
        ↓
MoveItPy
        ↓
OMPL Planner
        ↓
Inverse Kinematics
        ↓
Trajectory Display in RViz