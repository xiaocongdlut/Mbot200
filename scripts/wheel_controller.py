#! /usr/bin/env python2

import traceback

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

import numpy as np
import math

rx = {"fr":0.3, "fl":0.3, "rr":0.3, "rl":0.3}
ry = {"fr":0.24, "fl":0.24, "rr":0.24, "rl":0.24}
wheel_radius = 0.095

fr_pub = None
fl_pub = None
rr_pub = None
rl_pub = None

def cmdVelCB(data):       
  
  global fr_pub, fl_pub, rr_pub, rl_pub

  mat = np.matrix([[ 1, 1, (rx["fr"] + ry["fr"])],
                              [ 1, -1, -(rx["fl"] + ry["fl"])],
                              [ 1, -1,  (rx["rr"] + ry["rr"])],
                              [ 1, 1, -(rx["rl"] + ry["rl"])]])  

  cmd_vel = np.matrix([data.linear.x, data.linear.y, data.angular.z])

  temp = (np.dot(mat, cmd_vel.T).A1).tolist()
  wheel_vel = [x/wheel_radius for x in temp]
 
  wv = Float64()

  wv.data = wheel_vel[0]
  fr_pub.publish(wv)

  wv.data = wheel_vel[1]
  fl_pub.publish(wv)

  wv.data = wheel_vel[2]
  rr_pub.publish(wv)

  wv.data = wheel_vel[3]
  rl_pub.publish(wv)
  

def process():

  global fr_pub, fl_pub, rr_pub, rl_pub

  rospy.init_node('wheel_controller', anonymous=False)

  loop_rate = rospy.Rate(10)

  fr_pub = rospy.Publisher('/right_front_controller/command', Float64, queue_size=10)
  fl_pub = rospy.Publisher('/left_front_controller/command', Float64, queue_size=10)
  rr_pub = rospy.Publisher('/right_back_controller/command', Float64, queue_size=10)
  rl_pub = rospy.Publisher('/left_back_controller/command', Float64, queue_size=10)


  mouse_sub = rospy.Subscriber('/cmd_vel', Twist, cmdVelCB, queue_size=10)

  while not rospy.is_shutdown():

    loop_rate.sleep()




if __name__ == '__main__':

  try:

    process()

  except Exception as ex:
    print(traceback.print_exc())