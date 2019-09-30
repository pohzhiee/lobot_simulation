import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
from launch.actions import SetEnvironmentVariable
from launch.actions import UnsetEnvironmentVariable

def generate_launch_description():
    # Get gazebo_ros package path
    gazebo_ros_share_path = get_package_share_directory('gazebo_ros')
    lobot_desc_share_path = get_package_share_directory('lobot_description')
    lobot_urdf_path = os.path.join(lobot_desc_share_path,'robots/biped.urdf')
    # Launch gzserver
    gzserver = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(gazebo_ros_share_path, 'launch',
                    'gzserver.launch.py')),
        launch_arguments={'extra_gazebo_args': '__log_level:=debug'}.items())

    # GAZEBO_MODEL_PATH has to be correctly set for Gazebo to be able to find the model
    spawn_entity = Node(package='gazebo_ros', node_executable='spawn_entity.py',
                        arguments=['-entity', 'lobot','-file',lobot_urdf_path, '-z', "0.22"],
                        output='screen')

    # Launch gzclient
    gzclient = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(gazebo_ros_share_path, 'launch',
                    'gzclient.launch.py')),
             )
    return LaunchDescription([
        gzserver,
        spawn_entity,
        gzclient,
    ])
