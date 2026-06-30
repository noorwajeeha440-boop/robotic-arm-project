"""
Robotic Arm Project - Simple 6-DOF Simulation Example
Intern: Wajeeha Noor
"""

import math

# Example target position (x, y, z) in meters
target_x = 0.4
target_y = 0.3
target_z = 0.2

# Robotic arm link lengths (meters)
L1 = 0.3
L2 = 0.3

def inverse_kinematics(x, y, z):
    """Calculate basic joint angles for a 2-link robotic arm."""
    theta1 = math.atan2(y, x)

    r = math.sqrt(x**2 + y**2)
    D = (r**2 + z**2 - L1**2 - L2**2) / (2 * L1 * L2)

    if abs(D) > 1:
        raise ValueError("Target point is out of reach.")

    theta3 = math.atan2(math.sqrt(1 - D**2), D)

    theta2 = math.atan2(z, r) - math.atan2(
        L2 * math.sin(theta3),
        L1 + L2 * math.cos(theta3)
    )

    return math.degrees(theta1), math.degrees(theta2), math.degrees(theta3)

try:
    joint1, joint2, joint3 = inverse_kinematics(
        target_x, target_y, target_z
    )

    print("Target Position:", (target_x, target_y, target_z))
    print(f"Joint 1 Angle: {joint1:.2f} degrees")
    print(f"Joint 2 Angle: {joint2:.2f} degrees")
    print(f"Joint 3 Angle: {joint3:.2f} degrees")

except ValueError as e:
    print("Error:", e)
