from mcpi import minecraft, block
import math
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
a = mc.player.getRotation()
b = mc.player.getPitch()
mc.player.setRotation(-180)
#mc.player.setPos(x+1,y,z+1)

print(a,b)