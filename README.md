
<h2>  Unmanned Ground Vehicle (UGV)</h2>


<p>Wirelessly controlled robot that provides live video footage

Author: Samuel Rodriguez ([samuelrprofessional@gmail.com](mailto:samuelrprofessional@gmail.com))

Started: 06/01/21

Last Updated: 06/03/21

Self-Link: [https://tinyurl.com/k3rpch2p](https://tinyurl.com/k3rpch2p)

<h2>Background</h2>


Personally, I am at my university for most of the year, so I do not have the ability to traverse around my house to see my dogs, and I tend to get homesick sometimes.

<h3>Problem</h3>


Humans are limited in how fast they can travel. It is not instant, nor do we have the financial means to travel all the time. We are also limited such that we cannot be in multiple places at the same time either.

<h3>Objective/Solution</h3>




*   Build a wirelessly controlled robot from anywhere in the world
*   Install camera to get live video footage from robot
*   Control robot from a secure site
*   Robot travels on the ground

<h3>Materials</h3>




*   Raspberry Pi 4 Model B : $43
*   Micro HDMI to HDMI cable : $0 (Already have)
*   16BG Micro SD card (x3) : $9.90
*   5V DC 3A power supply adapter with USB type C : $0 (Already have)
*   4 Wheels and 4 motors : $14.99
*   L298N Motor Drive Controller Board DC Dual H-Bridge Robot Stepper Motor Control and dupont cables : $ 6.99

Total Cost: 43 + 0 + 9.90 + 0 + 14.99 + 6.99 = 74.88

<h2>Mock Up</h2>


Website where user controls robot from and views live video

![alt_text](src/remote-robot-control-center.png "image_tooltip")


<h2>Technologies</h2>


<h5>Figma</h5>




*   Design website mockup that will serve as the remote control for the UGV
*   Provide assets from the mockup into the actual website

<h5>Python</h5>




*   Use GPIOZero module to control motors:

[https://gpiozero.readthedocs.io/en/stable/api_output.html?highlight=motor#motor](https://gpiozero.readthedocs.io/en/stable/api_output.html?highlight=motor#motor)



*   Create HTTP Server to handle requests from user to send to UGV and take video data from robot to user

<h5>HTML</h5>




*   Basic website design (refer to mockup) that will show controls and live video

<h5>DC Motors</h5>




*   Gives all 4 wheel drive mobility
*   Activates each motor according to input from Raspberry Pi
*   Level of voltage correlates with rpm
*   One motor per wheel
*   Two motors per motor controller

<h5>Raspberry Pi</h5>




*   Hub for robot
*   Communicates with server
    *   Receives input for how to control UGV
    *   Sends live video output
*   Sends output to motors to move UGV
*   Receives input from camera to send live video

<h5>Camera</h5>




*   Connects to Raspberry Pi
*   Sends video data to Raspberry Pi

<h5>Electric Wire</h5>




*   Connect two per motor

<h5>L298N Motor Drive Controller</h5>




*   Communicate between 2 motors and Pi
*   Controls power delivered to the motors

<h2>Solution/Description</h2>


TODO: Write down each piece of the solution, i.e. break it down into smaller pieces

<h3>Who will do what?</h3>


I, Samuel Rodriguez, will be doing all of the work

<h3>When will it be done?</h3>


<h4>Week 1</h4>




*   Order all materials to practice with Raspberry Pi without constructing robot
*   Create website mockup on Figma
*   Finish design doc
*   Create static web page following mockup

<h4>Week 2</h4>




*   Connect to Raspberry Pi to control via laptop’s monitor and keyboard
*   Create local http-server with Python
*   Connect motors to power source to test that they are running

<h4>Week 3</h4>




*   Configure motor drive controller to Pi and motors
*   Send local signals to Pi to control motors via Pi
*   Configure camera to Pi (might need camera module)

<h4>Week 4</h4>




*   Configure camera to Pi
*   Create client for Pi to connect to http-server (with Python)
*   Control Pi via server (ensure connection even on different networks)

<h4>Week 5</h4>




*   Build robot skeleton and mount all devices

<h4>Week 6</h4>


<h2>Weekly Log</h2>


<h4>Week 1</h4>




*   I bought Raspberry Pi, motors, wheels, and Micro SD cards
*   Research how to setup Raspberry Pi via guidebook 
*   Construct GitHub Repo
*   Wrote some technologies in design doc
*   Create website mockup

<h4>Week 2</h4>


<h4>Week 3</h4>


<h4>Week 4</h4>


<h4>Week 5</h4>


<h4>Week 6</h4>


<h2>Conclusion</h2>

