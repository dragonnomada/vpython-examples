# 
# VPython Example 105 - Cylinder Cube
#
# Display a cube made of cylinders
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

center = vector(1, 1, 1)

p1 = center + vector(0, 0, 0)
p2 = center + vector(1, 0, 0)
p3 = center + vector(0, 1, 0)
p4 = center + vector(0, 0, 1)
p5 = center + vector(1, 1, 0)
p6 = center + vector(1, 0, 1)
p7 = center + vector(0, 1, 1)
p8 = center + vector(1, 1, 1)

sphere(pos=p1, radius=0.1, color=color.orange)
sphere(pos=p2, radius=0.1, color=color.red)
sphere(pos=p3, radius=0.1, color=color.green)
sphere(pos=p4, radius=0.1, color=color.blue)
sphere(pos=p5, radius=0.1, color=color.yellow)
sphere(pos=p6, radius=0.1, color=color.magenta)
sphere(pos=p7, radius=0.1, color=color.cyan)
sphere(pos=p8, radius=0.1, color=color.purple)

def cylinder_from_to(pos1, pos2):
    d = mag(pos2 - pos1)
    cylinder(pos=pos1, axis=pos2 - pos1, length=d, radius=0.05)

cylinder_from_to(p1, p2)
cylinder_from_to(p1, p3)
cylinder_from_to(p1, p4)
cylinder_from_to(p2, p5)
cylinder_from_to(p2, p6)
cylinder_from_to(p3, p5)
cylinder_from_to(p3, p7)
cylinder_from_to(p4, p6)
cylinder_from_to(p4, p7)
cylinder_from_to(p5, p8)
cylinder_from_to(p6, p8)
cylinder_from_to(p7, p8)