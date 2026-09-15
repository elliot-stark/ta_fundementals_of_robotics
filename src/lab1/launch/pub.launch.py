from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription ([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle1'
        ),
        Node(
            package='lab1',
            namespace='turtlesim1',
            executable='lab1_publisher',
            name='publisher_square'
        ),
    ])