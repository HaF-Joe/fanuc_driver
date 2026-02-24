<!-- SPDX-FileCopyrightText: 2025 FANUC America Corp.
     SPDX-FileCopyrightText: 2025 FANUC CORPORATION

     SPDX-License-Identifier: Apache-2.0
-->
<!-- markdownlint-disable MD013 -->
# fanuc_driver

![FANUC ROS 2 Control Driver](/images/FANUC_ros2_ControlDriver.jpg "FANUC ROS 2 Control Driver")

## About

This repository hosts the source code of the FANUC ROS 2 Driver project, a ros2_control high-bandwidth streaming driver.
This project will allow users to develop a ROS 2 application to control a FANUC virtual or real robot.

## Supported ROS 2 Distributions

| Distribution | Full Driver | Hardware Interface | Robot Description |
|---|---|---|---|
| **Humble** | ✅ | ✅ | ✅ |
| **Jazzy** | — | ✅ | ✅ |

### ROS 2 Jazzy Support

The following packages are compatible with ROS 2 Jazzy:

- **`fanuc_hardware_interface`** — The ros2_control hardware interface plugin for communicating with FANUC robots. This enables real-time joint streaming and GPIO control on Jazzy.
- **`fanuc_libs`** — Core C++ libraries (built automatically as a dependency).
- **`fanuc_description`** — Standalone robot description package containing URDF, SRDF, and reference MoveIt configuration files. Designed specifically for use with the **MoveIt Setup Assistant** on Jazzy.

To use on Jazzy, build only the supported packages:

```bash
cd ~/ros2_ws
colcon build --packages-up-to fanuc_hardware_interface fanuc_description
```

See the [`fanuc_description/README.md`](fanuc_description/README.md) for detailed instructions on using the MoveIt Setup Assistant with Jazzy.

## Installation

See the [FANUC ROS 2 Driver Documentation](https://fanuc-corporation.github.io/fanuc_driver_doc/) for instructions.

## Licensing

The original FANUC ROS 2 Driver source code and associated documentation
including these web pages are Copyright (C) 2025 FANUC America Corporation
and FANUC CORPORATION.

Any modifications or additions to source code or documentation
contributed to this project are Copyright (C) the contributor,
and should be noted as such in the comments section of the modified file(s).

FANUC ROS 2 Driver is licensed under
     [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

Exceptions:

- The sockpp library is licensed under the terms of the [BSD 3-Clause License](https://opensource.org/license/BSD-3-Clause).

- The readwriterqueue library is licensed under the terms of
  the [Simplified BSD License](https://opensource.org/license/BSD-2-Clause).

- The reflect-cpp and yaml-cpp libraries are licensed under the
  terms of the [MIT License](https://opensource.org/license/mit).

Please see the LICENSE folder in the root directory for the full texts of these licenses.
