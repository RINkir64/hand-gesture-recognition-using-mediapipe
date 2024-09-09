from pynput import mouse,keyboard

import time
import math

from threading import Thread
from queue import Queue

mouse_q = Queue()
key_q = Queue() 



time.sleep(10)
mymouse = mouse.Controller()
mykeyboard = keyboard.Controller()
lcl_s = 1
rcl_s = 1
j_s = 1
shift_s = 1

threshold = 10 #視点移動か停止かの閾値

def running():
 i = 5 #視点移動倍率
 key_q1=[]
 cl=[]
 mq = [0,0]
 
 while True:
  if not mouse_q.empty():
   mq=mouse_q.get_nowait
  mq1=mq[0]
  if mq[1]:
   mymouse.move(int(i*math.cos(mq1)),int(i*math.sin(mq1))) 
  if not (key_q.empty): 
   for k in keyq1:
    mykeyboard.release(k)
   keyq1=key_q.get_nowait
   for k in keyq1:
    mykeyboard.pressed(k)





 


def m(x1,y1,x2,y2): #視点移動 x1,yiからx2,y2への向きを計算
 radian = math.atan2(y2-y1,x2-x1)
 degree = radian * (180 / math.pi)
 distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
 mouse_q.put_nowait([degree,(threshold <= distance)])

def move(a) :
 if  -22.5 <= a <= 22.5:
  key_q.put(["w"])
 elif 22.5 <= a <= 67.5:
  key_q.put(["w","d"])
 elif 67.5 <= a <= 112.5:
  key_q.put(["d"])
 elif 112.5 <= a <= 157.5: 
  key_q.put(["s","d"])
 elif 157.5 <= a <= 180 or  -180<= a <=-157.5:
  key_q.put(["s"])
 elif -67.5 <= a <= -22.5:
  key_q.put(["w","a"])
 elif -112.5 <= a <= -67.5:
  key_q.put(["a"])
 elif -157.5 <= a <= 122.5:
  key_q.put(["s","a"])        

  

def j():
 if j_s:
  mykeyboard.pressed(keyboard.Key.space)
  j_s = 0
 else:
  mykeyboard.release(keyboard.Key.space)  
  j_s = 1 
def rcl():
 if rcl_s:
  mymouse.press(mouse.right)
  rcl_s = 0
 else:
  mymouse.release(mouse.right)
  rcl_s = 1 
 
def lcl():
 if lcl_s:
  mymouse.press(mouse.left)
  lcl_s = 0
 else:
  mymouse.release(mouse.left)
  lcl_s = 1 
def shift():
 if shift_s:
  mykeyboard.pressed(keyboard.Key.shift)
  shift_s = 0
 else:
  mykeyboard.release(keyboard.Key.shift)
  shift_s = 1   


thread = Thread(target=running)
thread.start()  

def no():
 mouse_q.put_nowait([0,0])
 key_q.put([])  
 if not(j_s):
    mykeyboard.release(keyboard.Key.space)  
    j_s = 1 
 if not(lcl_s):
  mymouse.release(mouse.left)
  lcl_s = 1 
 if not(rcl_s):
  mymouse.release(mouse.right)
  rcl_s = 1   
 if not(shift_s):
  mykeyboard.release(keyboard.Key.shift)
  shift_s = 1    