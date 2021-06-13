from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
# import RPi.GPIO as GPIO # uncomment when running on Pi

# uncomment when running on Pi
# GPIO.setmode(GPIO.BOARD)
# set up GPIO outputs (where motor driver controller is connected)
a = -1
b = -1
c = -1
d = -1
# pins on Pi that connect to motors
# TODO: place diagram as comment detailing how motors were wired
pins = [a, b, c, d]
# directions that correspond to pin arrangement
left_ = [False, True, True, False]
right_ = [not v for v in left_]
forward_ = [False, True, False, True]
backward_ = [not v for v in forward_]
# GPIO.setup(a, GPIO.OUT)
# GPIO.setup(b, GPIO.OUT)
# GPIO.setup(c, GPIO.OUT)
# GPIO.setup(d, GPIO.OUT)


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
    print("Bruh")
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
