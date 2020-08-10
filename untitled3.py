# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:00:33 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()
mc.setBlock(pos,15)