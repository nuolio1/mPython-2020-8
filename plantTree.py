from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

def plantTree(x,y,z):
    mc.setBlocks(x+1,y+5,z+1,x-1,y+3,z-1,17)
    mc.setBlocks(x,y,z,x-1,y+4,z,18)
for i in range(0,50,3):
    for h in range(0,50,3):
        plantTree(x+h,y,z+i)
