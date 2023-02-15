# 
# VPython Example 112 - Events
#
# Display 3 spheres, one of them rotating.
#
# * When you press `a` key shows the label and `b` hides the label
# * When you press `ctrl+click` and move the mouse 
#   one sphera go to mouse position 
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

s1 = sphere(pos=vec(1, 0, 0), color=color.red, radius=0.5)
s2 = sphere(pos=vec(0, 1, 0), color=color.green, radius=0.5)
s3 = sphere(pos=vec(0, 0, 1), color=color.blue, radius=0.5)

l2 = label(pos=vec(0, 1, 0), text="Hi")

def onmousemove():
    s1.pos = scene.mouse.pos

scene.bind("mousemove", onmousemove)

while True:
    s2.rotate(angle=radians(10), origin=vec(0, 0, 0), axis=vec(-1, 1, -1))
    rate(30)
    k = keysdown() # a list of keys that are down
    #print(k)
    if 'a' in k:
        l2.visible = True
        #print("ok")
    if 'b' in k:
        l2.visible = False
        #print("ok")