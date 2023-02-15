# 
# VPython Example 110 - Label
#
# Display a gear extruded to a cylinder
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

e = shapes.gear(n=10, radius=0.5)

extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=e)