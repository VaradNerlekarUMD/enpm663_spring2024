#!/usr/bin/env python3

"""
This script initializes and runs a ROS 2 subscriber node using the rclpy library.

The subscriber node is defined in the `SubscriberNode` class within the `first_package` package.
It subscribes to messages on a specific topic and processes them as defined in the class implementation.

Attributes:
    rclpy (module): The ROS 2 Python client library used to interact with ROS 2 systems.

Functions:
    main(args=None): Initializes the ROS 2 system, creates and spins a subscriber node, and shuts down the system.

Example:
    To run this script, use the following command in a terminal:
    ```
    ros2 run first_package subscriber_node.py
    ```
"""

import rclpy  # ROS 2 Python client library for writing ROS 2 nodes
from first_package.subscriber_node import (
    SubscriberNode,
)  # Import the SubscriberNode class from first_package


def main(args=None):
    """
    Main function to initialize the ROS 2 node and keep it alive until it's manually terminated or receives a shutdown signal.

    Args:
        args (list, optional): Command-line arguments that can be passed to the ROS 2 node. Defaults to None.

    This function performs the following steps:
    1. Initializes the ROS 2 Python client library (rclpy) with any provided arguments.
    2. Creates an instance of `SubscriberNode`, which subscribes to a specific topic.
    3. Spins (i.e., continuously processes messages on all subscribers) the node to keep it alive.
    4. Destroys the node and shuts down the ROS 2 system once the node stops spinning.
    """
    rclpy.init(args=args)  # Initialize the ROS 2 Python client library
    node = SubscriberNode(
        "help_sub_py"
    )  # Create a new instance of SubscriberNode named 'help_sub_py'
    rclpy.spin(node)  # Keep the node alive and processing data until shutdown
    node.destroy_node()  # Cleanly destroy the node instance
    rclpy.shutdown()  # Shut down the ROS 2 Python client library


if __name__ == "__main__":
    main()  # Execute the main function when the script is run