import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    """
    A simple ROS 2 node that demonstrate both publishing and subcribing

    """
    def __init__(self):
    """
    - publisher that publishes 'std_msgs/String' messages on the 'chatter' topic
    - subscription to listen for messages on the 'chatter' topic
    - timer to publish messages every second
    """
        super().__init__('my_node')

        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.subscription

        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
    """
    Publish message on the 'chatter' topic and logs the message to console
    """
        msg = String()
        msg.data = 'Hello ROS2 %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    def listener_callback(self, msg):
    """
    Logs recieved message on the 'chatter' topic to the console

    @msg (std_msgs.msg.String): The message recieved from the topic
    """
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    """
    Pipeline for publish and subscribe on the 'chatter' topic
    Cleans up resources and shuts down the ROS 2 system when node is stopped

    @args (list, optional): Command-line arguments passed to the node
    """
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main() 
