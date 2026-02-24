# SPDX-FileCopyrightText: 2025, FANUC America Corporation
# SPDX-FileCopyrightText: 2025, FANUC CORPORATION
#
# SPDX-License-Identifier: Apache-2.0

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    robot_model = LaunchConfiguration("robot_model")

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("fanuc_description"),
                    "urdf",
                ]
            ),
            "/",
            robot_model,
            ".urdf.xacro",
        ]
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[{"robot_description": robot_description_content}],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="both",
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "robot_model",
                description="The FANUC robot model to visualize.",
                choices=[
                    "crx5ia",
                    "crx10ia",
                    "crx10ia_l",
                    "crx20ia_l",
                    "crx30ia",
                ],
            ),
            robot_state_publisher_node,
            rviz_node,
        ]
    )
