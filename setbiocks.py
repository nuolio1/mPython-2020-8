# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:19:11 2020

@author: user
"""

import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
time.sleep(5)

x,y,z,=mc.player.getTilePos()

color=random.randrange(0,16)
mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,color)