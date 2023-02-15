# 
# VPython Example 109 - Compound
#
# Display a compound object between sphera and cylinder
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

p = vector(1, 1, 1)
s = sphere(pos=p, color=color.yellow, radius=0.1)
c = cylinder(pos=p, axis=vector(1, 0, 0), size=vector(1, 0.05, 0.05))

f = compound([s, c], pos=vector(2, 2, 2), axis=vector(1, 1, 1)) 