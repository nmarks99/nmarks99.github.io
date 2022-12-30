---

name: Reaction Wheel
tools: [Arduino, PID control, C/C++, emdedded systems]
image: ../images/reaction_wheel.png
description: A reaction wheel prototype for active roll control of high-power rockets

---

# Reaction Wheel for Active Roll Control

{% include image.html path="../images/reaction_wheel.gif" 
caption="Reaction wheel demonstration"
width="500"
%}

As an independent project to be counted towards the aerospace concentration portion of my mechanical engineering degree,
I designed, prototyped, and tested this reaction wheel with the goal of securing it inside a high power rocket to
control its roll axis during flight.

The reaction wheel utilizes a proportional-integral-derivative (PID) closed-loop feedback controller to control
the angular position of the system it's attached to by continually adjusting the PWM frequency sent to a DC motor depending
on the measured angular position from an IMU. The angular position of the system over time was logged and sent to a computer
via bluetooth. Finally, a MATLAB program was used to parse the recieved data and generate plots. The below images and text
give a good summary of the success of the prototype.

<br>
<br>

{% include image.html path="../images/result1.png" 
caption=" This plot shows a case where the system
was perturbed by −152.31◦. The reaction wheel actively
responded to this perturbation and brought the system to
within 10◦ of its target angle, −7.69◦, within just 1.12 seconds,
and to within 5◦ of its target angle in 2.44 seconds."
width="600"
%}

<br>
<br>

{% include image.html path="../images/result2.png"
caption="Plot showing the angular position vs. time after
successive perturbations were produced in both directions.
This is similar to the example demonstration shown in the
gif at the top of the page"
width="600"
%}
