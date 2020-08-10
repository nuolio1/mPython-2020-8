# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:01:24 2020

@author: user
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    
    mc.postToChat("nuoliaoX:"+str(x)+"Y:"+str(y)+"Z:"+str(z))
    time.sleep(0.5)