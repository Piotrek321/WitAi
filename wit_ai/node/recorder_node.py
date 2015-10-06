#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Program do wysyłania

import json, subprocess, rospy, re, urllib, pycurl, os, sys, time, numpy

from std_msgs.msg import String
from recording import record

czasMowy = 4
numberOfWavFiles = 1

if __name__ == "__main__":



    pub = rospy.Publisher('recorder', String, queue_size=10)
    rospy.init_node('rec', anonymous=True)
    rate = rospy.Rate(10) # 10hz


    while not rospy.is_shutdown(): #While(True)

        record(czasMowy,numberOfWavFiles)

        print numberOfWavFiles
        rospy.loginfo(numberOfWavFiles)
        print (" ")
        pub.publish(str(numberOfWavFiles))
        rate.sleep()

        if (numberOfWavFiles >=5):
            numberOfWavFiles = 1
        else:
            numberOfWavFiles += 1
