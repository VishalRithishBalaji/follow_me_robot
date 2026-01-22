import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_path = get_package_share_directory('follow_me_robot')
    
    # Process Xacro
    robot_desc = xacro.process_file(os.path.join(pkg_path, 'urdf', 'robot.urdf.xacro')).toxml()
    cyl_desc = xacro.process_file(os.path.join(pkg_path, 'urdf', 'cylinder.urdf.xacro')).toxml()

    # Gazebo Sim
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
        launch_arguments={'gz_args': f'-r {os.path.join(pkg_path, "worlds", "follow_me.sdf")}'}.items(),
    )

    return LaunchDescription([
        gazebo,
        Node(package='ros_gz_sim', executable='create', arguments=['-name', 'follower_bot', '-string', robot_desc, '-z', '0.1']),
        Node(package='ros_gz_sim', executable='create', arguments=['-name', 'blue_cylinder', '-string', cyl_desc, '-x', '2.0', '-z', '0.3']),
        Node(package='ros_gz_bridge', executable='parameter_bridge', arguments=['/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist', '/camera@sensor_msgs/msg/Image@gz.msgs.Image']),
    ])

