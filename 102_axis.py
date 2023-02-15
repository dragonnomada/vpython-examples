# 
# VPython Example 102 - Axis
#
# Display 3 arrows on each axis
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

axis_x = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.red)
axis_y = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.green)
axis_z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.blue)