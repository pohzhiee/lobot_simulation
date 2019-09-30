import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get gazebo_ros package path
    lobot_sim_share_path = get_package_share_directory('lobot_simulation')
    # Launch param server
    params_server = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(lobot_sim_share_path, 'launch',
                    'params_server.launch.py')),
             )
    # Launch lobot spawner
    lobot_spawner = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(lobot_sim_share_path, 'launch',
                    'spawn_lobot.launch.py')),
             )
    # Launch GUI to set desired positions
    desired_pos_gui = IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(lobot_sim_share_path, 'launch',
                    'desired_state_gui.launch.py')),
             )
    return LaunchDescription([
        params_server,
        lobot_spawner,
        desired_pos_gui,
    ])
