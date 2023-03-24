---

name: EKF SLAM From Scratch
tools: [ROS2, C++, EKF, SLAM]
image: ../images/slam_good_overhead.png
description: Extended Kalman filter SLAM algorithm implemented from scratch in C++ with ROS2 for the Turtlebot3

---

# EKF SLAM from Scratch

[*View on GitHub*](https://github.com/nmarks99/turtlebot3-ekf-slam)

In this project, I implement an extended Kalman filter (EKF) simultaneous localization
and mapping (SLAM) algorithm from scratch for the Turtlebot3 using C++ and ROS2.
This includes a simulator so the algorithm can be tested in simulation before being 
tested on the real robot. 

The video below shows a demonstration which compares the performance of the SLAM estimate
versus the odometry estimate. In this demonstration, the red robot is the true/simulated
position of the robot. The blue robot is the position of the robot based solely on
wheel odometry. The green robot is the position of the robot based on the EKF SLAM 
algorithm assuming a know data association.

{% include image.html path="../images/slam_demo_known.gif" caption="Demo with known data association" width="800" %}

Towards the beginning before hitting the obstacle, because of simulated wheel slipping,
the odometry estimate slowly drifts from the true position of the robot while the pose
estimate from SLAM remains good. Once the robot runs into an obstacle, during the
collision, wheel rotation does not result in the motion that is 
expected by the odometry model, so the odometry pose estimate becomes even more
incorrect. However, you can see that the SLAM pose estimate remains quite good.



