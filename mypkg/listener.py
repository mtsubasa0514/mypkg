#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 松本翼
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.create_subscription(Int16, 'countup', self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f'Listen: {msg.data}')

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
