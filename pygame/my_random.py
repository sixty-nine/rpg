import random
import math

def rnd():
    return random.uniform(0, 1)

def getRandomPointInCircle(radius):
    t = 2 * math.pi * rnd()
    u = rnd() + rnd()
    r = 2 - u if u > 1 else u
    return [
        int(radius * r * math.cos(t)),
        int(radius * r * math.sin(t))
    ]

def getRandomPointInEllipse(width, height):
    t = 2 * math.pi * rnd()
    u = rnd() + rnd()
    r = 2 - u if u > 1 else u
    return [
        width * r * math.cos(t) / 2,
        height * r * math.sin(t) / 2
    ]
