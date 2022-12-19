---

name: Reaction Wheel
tools: [Arduino, PID control, C/C++, emdedded systems]
image: ../images/reaction_wheel.png
description: A reaction wheel prototype for active roll control of high-power rockets

---

As an independent project to be counted towards the aerospace concentration portion of my mechanical engineering degree,
I designed, prototyped, and tested this reaction wheel with the goal of securing it inside a high power rocket to
control its roll axis during flight.

The reaction wheel utilizes a proportional-integral-derivative (PID) closed-loop feedback controller to control
the angular position of the system it's attached to by continually adjusting the PWM frequency sent to a DC motor depending
on the measured angular position from an IMU. The angular position of the system over time was logged and sent to a computer
via bluetooth. Finally, a MATLAB program was used to parse the recieved data and generate plots. The below images and text
give a good summary of the success of the prototype.


