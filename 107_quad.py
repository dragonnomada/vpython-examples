# 
# VPython Example 107 - Quad
#
# Display a quad made by vertices with different colors
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

o = vertex(pos=vector(0, 0, 0), color=color.white)
a = vertex(pos=vector(1, 0, 0), color=color.red)
b = vertex(pos=vector(1, 1, 0), color=color.yellow)
c = vertex(pos=vector(0, 1, 0), color=color.green)

q = quad(v0=o, v1=a, v2=b, v3=c)