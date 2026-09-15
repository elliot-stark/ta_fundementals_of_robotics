import rclpy
from std_msgs.msg import Float32
from turtlesim.msg import Pose
from rclpy.node import Node

class Pose_subscriber(Node):
    def __init__(self):
        super().__init__('pose_sub')
        self.pos_publisher = self.create_publisher(Float32, 'distance_traveled', 10)
        self.pos_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_subscriber_callback, 10)
        self.previous_location = None
        self.total_distance = 0.0
        
    def pose_subscriber_callback(self, msg):
        current_location = msg

        if self.previous_location is not None:
            dist_traveled = abs(current_location.x - self.previous_location)
            self.total_distance += dist_traveled

        self.previous_location = current_location.x

        self.publish_distance()


    def publish_distance(self):
        msg = Float32()
        msg.data = self.total_distance
        self.pos_publisher.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    pose_sub = Pose_subscriber()
    rclpy.spin(pose_sub)
    pose_sub.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()