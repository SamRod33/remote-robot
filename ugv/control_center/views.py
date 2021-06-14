from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
# import RPi.GPIO as GPIO # uncomment when running on Pi

# uncomment when running on Pi
# GPIO.setmode(GPIO.BOARD) # NOTE: this referes to physical numering of board
# should use instead GPIO.setmode(GPIO.BCM) # TODO: get it working for GPIO.BOARD
# I am currently using Pi model 4 numbering
# Basically,
#  BOARD numbering system. This refers to the pin numbers on the P1 header of
# the Raspberry Pi board. The advantage of using this numbering system is that
# your hardware will always work, regardless of the board revision of the RPi.
# You will not need to rewire your connector or change your code.
# The second numbering system is the BCM numbers. This is a lower level way of
# working - it refers to the channel numbers on the Broadcom SOC. You have to
# always work with a diagram of which channel number goes to which pin on the
# RPi board. Your script could break between revisions of Raspberry Pi boards.
# set up GPIO outputs (where motor driver controller is connected)
# pins on Pi that connect to motors
# Diagram POV: looking at wheels from top down # TODO: revise plz
# 18 --- 27
#  | @@@ |
#  | @@@ |
#  | @@@ |
# 15 --- 17
pins = [18, 17, 27, 15]
# directions that correspond to pin arrangement
left_ = [True, True, False, False]
right_ = [not v for v in left_]
forward_ = [False, True, False, True]
backward_ = [not v for v in forward_]
# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(27, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)


def index(request):
    return render(request, "index.html")


# def go(adict):
#     """
#     Moves Pi according to boolean values in **adict**
#     **adict** is a dictionary such that a key is a valid pin
#     in the Pi that maps to a boolean value according to if that
#     pin should be delivered power or not. A valid pin is such that
#     it is connected to a motor.
#     """
#     [GPIO.output(k, v) for k, v in adict.items()]


def forward(request):
    """
    Pi moves forward and renders index.html page
    """
    # go(dict(zip(pins, forward_)))
    return index(request)


def backward(request):
    """
    Pi moves backward and renders index.html page
    """
    # go(dict(zip(pins, backward_)))
    return index(request)


def left(request):
    """
    Pi moves left and renders index.html page
    """
    # go(dict(zip(pins, left_)))
    return index(request)


def right(request):
    """
    Pi moves right and renders index.html page
    """
    # go(dict(zip(pins, right_)))
    return index(request)


def stop(request):
    """
    Stops Pi renders index.html page
    """
    # go(dict(zip(pins, [False for i in range(4)])))
    return index(request)


def end(request):
    """
    Quits operating Pi
    """
    # GPIO.cleanup()
    # TODO: make a new page to show end of Pi session
