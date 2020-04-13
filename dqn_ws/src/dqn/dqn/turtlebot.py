import os
import select
import sys
import termios
import tty

from geometry_msgs.msg import Twist
import rclpy
from rclpy.qos import QoSProfile


TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

msg = """
Control Your TurtleBot3!
---------------------------
This is my first try on doing a circle.
"""

def main():
    settings = termios.tcgetattr(sys.stdin)

    rclpy.init()

    qos = QoSProfile(depth=10)
    node = rclpy.create_node('turtlebot')
    pub = node.create_publisher(Twist, 'cmd_vel', qos)

    status = 0

    target_linear_velocity   = 1.0
    target_angular_velocity  = 1.0

    control_linear_velocity  = 0.0
    control_angular_velocity = 0.0


if __name__ == '__main__':
    main()
