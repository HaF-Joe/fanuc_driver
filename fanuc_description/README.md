<!-- SPDX-FileCopyrightText: 2025 FANUC America Corp.
     SPDX-FileCopyrightText: 2025 FANUC CORPORATION

     SPDX-License-Identifier: Apache-2.0
-->
<!-- markdownlint-disable MD013 -->
# fanuc_description

Standalone FANUC robot description package providing URDF, SRDF, and reference MoveIt configuration files for FANUC CRX collaborative robots.

This package is **ROS 2 distro-agnostic** and can be used on **Humble, Jazzy**, or other ROS 2 distributions. It is designed to decouple the robot description from the Humble-specific hardware interface, enabling users on newer ROS 2 distributions (such as Jazzy) to use the FANUC robot models with the **MoveIt Setup Assistant**.

## Supported Robots

| Robot Model | URDF File | SRDF File |
|---|---|---|
| CRX-5iA | `urdf/crx5ia.urdf.xacro` | `srdf/crx5ia.srdf` |
| CRX-10iA | `urdf/crx10ia.urdf.xacro` | `srdf/crx10ia.srdf` |
| CRX-10iA/L | `urdf/crx10ia_l.urdf.xacro` | `srdf/crx10ia_l.srdf` |
| CRX-20iA/L | `urdf/crx20ia_l.urdf.xacro` | `srdf/crx20ia_l.srdf` |
| CRX-30iA | `urdf/crx30ia.urdf.xacro` | `srdf/crx30ia.srdf` |

## Prerequisites

This package requires the external `fanuc_crx_description` package which provides the robot geometry (meshes, visual/collision models, kinematic chain definitions). Ensure it is available in your ROS 2 workspace.

## Using with ROS 2 Jazzy and MoveIt Setup Assistant

Follow these steps to set up your FANUC robot on ROS 2 Jazzy:

### 1. Install Dependencies

```bash
# Install MoveIt 2 for Jazzy
sudo apt install ros-jazzy-moveit

# Clone this repository and the fanuc_crx_description package into your workspace
cd ~/ros2_ws/src
git clone <this-repo-url>
git clone <fanuc_crx_description-repo-url>
```

### 2. Build Only the Description Package

You only need to build `fanuc_description` (and `fanuc_crx_description`). The other packages in this repository are Humble-specific and do not need to be built.

```bash
cd ~/ros2_ws
colcon build --packages-select fanuc_description fanuc_crx_description
source install/setup.bash
```

### 3. Visualize the Robot (Optional)

Verify the robot model loads correctly:

```bash
ros2 launch fanuc_description view_robot.launch.py robot_model:=crx10ia
```

### 4. Launch MoveIt Setup Assistant

Use the URDF with the MoveIt Setup Assistant to generate your own MoveIt configuration:

```bash
ros2 launch moveit_setup_assistant setup_assistant.launch.py
```

In the Setup Assistant:
1. Click **Create New MoveIt Configuration Package**
2. Browse to the URDF xacro file, e.g.: `~/ros2_ws/install/fanuc_description/share/fanuc_description/urdf/crx10ia.urdf.xacro`
3. Follow the Setup Assistant wizard to configure your robot

### 5. Reference Configurations

This package includes reference configuration files in the `config/` directory that can be used as starting points:

- `config/kinematics.yaml` — IK solver configuration
- `config/joint_limits.yaml` — Joint velocity and acceleration limits (CRX-10iA/CRX-10iA/L)
- `config/initial_positions.yaml` — Default joint positions

The `srdf/` directory contains pre-configured SRDF files for each robot model with:
- Manipulator planning group (base_link → flange chain)
- End-effector group (tool0)
- Default group state
- Virtual joint (world → base_link)
- Collision disable pairs

## Package Structure

```
fanuc_description/
├── CMakeLists.txt
├── package.xml
├── README.md
├── urdf/
│   ├── crx_ros2_control_macro.xacro    # Mock ros2_control definition
│   ├── crx5ia.urdf.xacro
│   ├── crx10ia.urdf.xacro
│   ├── crx10ia_l.urdf.xacro
│   ├── crx20ia_l.urdf.xacro
│   └── crx30ia.urdf.xacro
├── srdf/
│   ├── crx5ia.srdf
│   ├── crx10ia.srdf
│   ├── crx10ia_l.srdf
│   ├── crx20ia_l.srdf
│   └── crx30ia.srdf
├── config/
│   ├── kinematics.yaml
│   ├── joint_limits.yaml
│   └── initial_positions.yaml
└── launch/
    └── view_robot.launch.py
```

## Licensing

See the top-level [LICENSE](../LICENSES/) directory for license texts.
