


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z,=mc.player.getPos()
mc.setSign(x,y,z,63,0,"1;2;3","2;4;6","3;6;9"," ")