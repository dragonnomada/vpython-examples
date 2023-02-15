# 
# VPython Example 111 - Rotation
#
# Display a gear extruded in rotation
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

e = shapes.gear(n=10, radius=0.5)

f = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=e)

while True:
    f.rotate(angle=radians(10), axis=vector(0, 1, 0))
    sleep(0.05)