from p5 import *

def draw():
    background(204)
    line((0, 0), (width, height))
    print(frame_rate)

run(frame_rate=30)
