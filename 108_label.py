# 
# VPython Example 108 - Label
#
# Display a label close to one sphera
#
# Author: Alan Badillo Salas <alan@nomadacode.com>
# Created: 2023/02/15
#

from vpython import *

p = vector(1, 1, 1)

sphere(pos=p, radius=1)

label(
    pos=p,                     # vector origin
    text="Hello VPython",      # text
    align="right",             # text align 'left', 'right', or 'center'
    xoffset=100,               # x distance to origin
    yoffset=100,               # y distance to origin
    space=50,                  # radius distance to origin
    box=True,                  # if box is show
    border=16,                 # padding box
    height=16,                 # font size
    color=color.blue,          # font color
    background=color.purple,   # box background color
    opacity=0.4,               # box background transparency
    line=True,                 # if line is show
    linecolor=color.red,       # line color
    linewidth=4,               # line width
    visible=True               # if label is visible
    )