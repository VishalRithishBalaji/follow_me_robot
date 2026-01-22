#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')
        self.subscription = self.create_subscription(Image, '/camera', self.image_callback, 10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.bridge = CvBridge()
        self.kp_d = 0.005; self.target_w = 180; self.kp_s = 0.002

    def image_callback(self, msg):
        cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array([100, 150, 50]), np.array([130, 255, 255]))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        drive = Twist()
        if contours:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            drive.linear.x = float((self.target_w - w) * self.kp_d)
            drive.angular.z = float((cv_img.shape[1]/2 - (x + w/2)) * self.kp_s)
            drive.linear.x = float(np.clip(drive.linear.x, -0.5, 0.5))
        self.publisher.publish(drive)
        cv2.imshow("Vision", cv_img); cv2.waitKey(1)

def main():
    rclpy.init(); rclpy.spin(FollowerNode()); rclpy.shutdown()

if __name__ == '__main__':
    main()

