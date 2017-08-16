#!/usr/bin/env python

import math
import rospy
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


def callback(data):

	twist=Twist()
	if abs(data.axes[7])==1 :
	  if data.axes[5]>0 :
	    twist.linear.x=(3*data.axes[5]+1)*data.axes[7]
	  else :
	    twist.linear.x=data.axes[7]
	else :
	  twist.linear.x=0
	if abs(data.axes[6])==1 :
	  if data.axes[5]>0 :
	    twist.angular.z=(3*data.axes[5]+1)*data.axes[6]
	  else :
	    twist.angular.z=data.axes[6]
	else :
	  twist.angular.z=0

	twist.linear.y= data.buttons[0]
	twist.linear.z= data.buttons[1]
	twist.angular.x= data.buttons[2]
	twist.angular.y= data.buttons[3]
	

	if twist.linear.x==0 and twist.angular.z==0 and twist.linear.y==0 and twist.linear.z==0 and twist.angular.x==0 and twist.angular.y==0:
	  pass
	else : 
	  pub.publish(twist)



if __name__ == '__main__':
	try: 
		rospy.init_node('joyController')
		rospy.Subscriber('smoothData', Joy, callback)
		pub = rospy.Publisher('cmd_vel', Twist,queue_size=3)
		rospy.spin()
	except rospy.ROSInterruptException:
		pass

