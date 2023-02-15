# 
# VPython Example 106 - Triangle
#
# Display a triangle made by vertices with different colors
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

a = vertex(pos=vector(1, 0, 0), color=color.red)
b = vertex(pos=vector(0, 1, 0), color=color.green)
c = vertex(pos=vector(0, 0, 1), color=color.blue)

t = triangle(v0=a, v1=b, v2=c)