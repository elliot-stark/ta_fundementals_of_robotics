from std_msgs.msg import String
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class Publisher(Node):
    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.turle_movement_publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 1.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.instruction = 'straight'

    def timer_callback(self):
        time.sleep(0.5)
        if self.instruction == 'turn':
            self.turn_turtle()
        else:
            self.go_straight()


    def go_straight(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        self.turle_movement_publisher_.publish(msg)
        self.instruction = 'turn'

    def turn_turtle(self):
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 1.55
            self.turle_movement_publisher_.publish(msg)
            self.instruction = 'straight'


def main(args=None):
    rclpy.init(args=args)
    turtlesim_publisher = Publisher()
    rclpy.spin(turtlesim_publisher)
    turtlesim_publisher.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()


