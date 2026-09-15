from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('lab1'),
                    'pub.launch.py'
                ])
            ])
        ),
        Node(
            package='lab1',
            # namespace='turtlesim1',
            executable='lab1_2_pubsub',
            name='lab1_2_pubsub'

        ),

        ExecuteProcess(
            cmd=[
                'ros2',
                'topic',
                'echo',
                'distance_traveled',
                'std_msgs/Float32'
            ],
            shell=True,
            output='screen'
        )
    ])