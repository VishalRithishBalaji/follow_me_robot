# Follow-Me Robot Project
**Milestone 1: Perception and Environment Setup**

## Overview
A ROS 2 Jazzy robot that identifies a blue cylinder using OpenCV and tracks it in Gazebo Harmonic.

## Setup
- **ROS 2**: Jazzy Jalisco
- **Simulator**: Gazebo Harmonic

## Build Instructions
```bash
colcon build --packages-select follow_me_robot
source install/setup.bash
## How to Run the Project

### 1. Launch the Simulation
This command starts Gazebo Harmonic, spawns the robot, and sets up the communication bridge:
```bash
source install/setup.bash
ros2 launch follow_me_robot robot_launch.py
###2. Run the Simulation
source install/setup.bash
ros2 run follow_me_robot follower_node.py

