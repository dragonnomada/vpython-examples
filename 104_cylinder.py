# 
# VPython Example 104 - Cylinders
#
# Display 3 cylinders of different colors on each axis
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

c1 = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), length=1, radius=0.1, color=color.red)
c2 = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), length=1, radius=0.1, color=color.green)
c3 = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=1, radius=0.1, color=color.blue)