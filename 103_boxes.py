# 
# VPython Example 103 - Boxes
#
# Display 3 boxes on different places
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

box(pos=vector(0, 0, 0), length=2, height=0.5, width=1)

box(pos=vector(1, 1, 1), up=vector(1, 0, 0), size=vector(2, 0.5, 1), color=color.red)
box(pos=vector(1, 1, 1), up=vector(0, 1, 0), size=vector(2, 0.5, 0.9), color=color.green)
box(pos=vector(1, 1, 1), up=vector(0, 0, 1), size=vector(1.9, 0.5, 1), color=color.blue)