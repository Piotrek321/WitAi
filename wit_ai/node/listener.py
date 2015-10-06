#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wit
import json
import subprocess
import rospy
import re
import urllib, pycurl, os
from std_msgs.msg import String
import time
from rospy.numpy_msg import numpy_msg
import numpy
from wit_ai.msg import Num

autoTable = [ 'intent','number','whichCommands', 'colour', 'howFast', 'confidence', 'direction', 'whichFunction', 'text', 'fileID']
manualTable = [ 'intent','number','whichCommands', 'colour', 'howFast', 'confidence', 'direction', 'whichFunction', 'text', 'fileID']
manualConfidence = 'confidence'
autoConfidence = 'confidence'
def callback(data):
	global autoTable
	global manualTable
	global autoConfidence
	global manualConfidence
	fileID = data.some_strings[9]
	if fileID == "manual":
		manualTable = data.some_strings
		manualConfidence = data.some_strings[5]
		#print manualTable
	elif fileID == "Auto":
		autoTable = data.some_strings
		autoConfidence = data.some_strings[5]
		#print autoTable
	else:
		print "Sth is wrong"

	if not manualConfidence == 'confidence' and not autoConfidence == 'confidence':
		if manualConfidence >= autoConfidence:
			rospy.loginfo(manualTable)
			print (" ")
			pub.publish(manualTable)
			rate.sleep()
		else:
			rospy.loginfo(autoTable)
			print (" ")
			pub.publish(autoTable)
			rate.sleep()




if __name__ == '__main__':
	rospy.init_node('messanger', anonymous=True)
	#listener = tf.TransformListener()
	pub = rospy.Publisher('messanger', Num, queue_size=10)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		try:
			rospy.Subscriber("chatter", Num, callback)
		except:
			print "COs nie tak"
		rospy.spin()
