cmake_minimum_required(VERSION 3.8)
project(follow_me_robot)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(cv_bridge REQUIRED)

# Install Python package
install(DIRECTORY follow_me_robot/ DESTINATION lib/${PROJECT_NAME} FILES_MATCHING PATTERN "*.py")

# Install URDF, Launch, and Worlds
install(DIRECTORY launch urdf worlds DESTINATION share/${PROJECT_NAME})

# Install the executable node
install(PROGRAMS follow_me_robot/follower_node.py DESTINATION lib/${PROJECT_NAME})

ament_package()

