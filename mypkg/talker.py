#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 松本翼
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(Int16, 'countup', 10)
        self.create_timer(0.5, self.cb)
        self.n = 0

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
