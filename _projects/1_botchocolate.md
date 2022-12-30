---

name: BotChocolate
tools: [ROS2, Python, Franka Emika Panda, Emdedded Systems, Computer Vision]
image: ../images/botchoc1.png
description: A robot arm that makes hot chocolate using ROS2

---

# BotChocolate: A robo-barista using the Franka-Emika Panda and ROS2
Code avaible on GitHub: [BotChocolate](https://github.com/allan-gc/Bot-Chocolate-ROS2)
<br>
<figure>
  <center>
    <video width="800" controls="controls">
        <source src="../images/BotChocolate15.mp4">
    </video>
  </center>
</figure>


## Overview
The goal of this project was to make a cup of hot chocolate using the Franka-Emika Panda robot
arm. To determine the location of all the objects in the environment, the system utilizes an
Intel RealSense D435i camera and AprilTags. Upon initial setup, a calibration process must be
completed. After this, the process consisted of using AprilTags to locate a scoop of cocoa, a
mug, a spoon, and a kettle relative to the robot. Next, using custom ROS2 MoveIt API for Python
developed by our team, the robot is able to perform path planning between all of these objects.
Once we start the program, the robot turns on the kettle, dumps the cocoa powder into the mug, pours
the hot water over the power, and stirs the mixture with the spoon.

## Software
The main challenge of this project was developing a MoveIt! API for ROS2 in Python.
MoveIt! is a ROS library designed to make moving a robot to specified locations simplier,
by handling all the math (forward/inverse kinematics etc.) under the hood. Since an API for 
MoveIt! in ROS2 did not exist yet in Python (one does exist in C++) we decided to write our own 
API since the rest of our project was to use Python. We did this by intercepting MoveIt! action 
messages from the C++ API so we could figure out how to construct the messages in our Python API.

The code for the BotChocolate project as well as the ROS2 Python MoveIt! API
can be found here on the [BotChocolate GitHub](https://github.com/allan-gc/Bot-Chocolate-ROS2) page. A version of the Python API that is ready
for release for others to use is still in the works, however the code may be useful to some as is.

## The Team
Nick Marks  
James Oubre  
Shantao Cao  
David Dorf  
Allan Garcia  

{% include image.html path="../images/botchocolate_team.png" caption="Team with the robot" width="800" %}

