#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Program do wysyłania
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
from recording import record
from sendSoundToWit import queryAudio, query
czasMowy = 4

#key - Server Access Token from Your wit.ai account
key = 'THAKYMA767MXNDXJOZXDUBGHGFIRW5ER'

#convert adjective to number. It is used in function that repeats commands
def czyKoncoweKomendy (arg):
    return {
        'poprzednią': -1,
        'ostatnią': -1,
        'ostatnia': -1,
        'ostatnio': -1,
        'ostatnich' : -1,
        'ostatni' : -1,
        'pierwsze': 0,
        'pierwszych': 0,
        'ostatnie': 3,
        'ostatnich':3,
        'pierwszą': 4

    }.get(arg,False)



#convert text to number.
def textToNumber (number):
    return {
        'jeden': 1,
        'pierwszy': 1,
        'pierwszym': 1,
        'pierwszego': 1,
        'drugi': 2,
        'drugim': 2,
        'drugiego': 2,
        'dwa': 2,
        'dwie':2,
        'trzy': 3,
        'trzeci': 3,
        'trzecim': 3,
        'trzeciego': 3,
        'cztery': 4,
        'czwarty': 4,
        'czwartym': 4,
        'czwartego': 4,
        'pięć': 5,
        'piąty': 5,
        'piątym': 5,
        'piątego': 5,
        'sześć': 6,
        'szósty': 6,
        'szóstym': 6,
        'szóstego': 6,
        'siedem': 7,
        'siódmy': 7,
        'siódmym': 7,
        'siódmego': 7,
        'ósmy': 8,
        'ósmym': 8,
        'osiem': 8,
        'ósmego': 8,
        'dziewięć': 9,
        'dziewiąty': 9,
        'dziewiątym': 9,
        'dziewiątego': 9,
        'dziesięć': 10,
        'dziesiąty': 10,
        'dziesiątym': 10,
        'dziesiątego': 10,

    }.get(liczba,False)



tableToPublish = ['intent','number','whichCommands', 'colour', 'howFast', 'confidence', 'direction', 'whichFunction', 'text']
numberOfWavFiles = 1


if __name__ == "__main__":
    wit.init()


    pub = rospy.Publisher('chatter', Num, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz


    while not rospy.is_shutdown(): #While(True)


        try:
            dataDict = wit.voice_query_auto(key)
        except:
            print "Sth wrong with end of speech detection"
        if not dataDict:
            continue;


        try:
            intent= dataDict["outcomes"][0]["intent"]
            print ("Try intent")

            try:
                number=dataDict["outcomes"][0]["entities"]['number'][0]['value']
                print ("Try number")
                if(number):
                    if not(number.isdigit()):
                        number = textToNumber(number)
                        print ("Konwersja number")

            except:
                print ("Except number")
                if(str(intent) == 'Zmiana_kontroli'):
                    print("Zmiana kontroli ale brak numberu")
                    number = 0
                else:
                    number = 1

            try:
                whichCommands = dataDict["outcomes"][0]["entities"]['ktore'][0]['value']
                if (whichCommands):
                    print("Ktore komendy: " + str(whichCommands))
                    whichCommands = czyKoncoweKomendy(str(whichCommands))
                else:
                    whichCommands = 3 #ostatnie

            except:
                whichCommands = 3
                print ("Bląd przy whichCommands")

            try:
                howFast = dataDict["outcomes"][0]["entities"]['howFast'][0]['value']
            except:
                howFast = 'normalnie'

            try:
                colour = dataDict["outcomes"][0]["entities"]['colour'][0]['value']
            except:
                colour = 'Brak colouru'
                if(intent == 'Zmiencolour'):
                    colour = 'kolejny'
            try:
                confidence= dataDict["outcomes"][0]["confidence"]
                confidence = confidence * 100
            except:
                confidence = 'Null'

            try:
                direction= dataDict["outcomes"][0]["entities"]['direction'][0]['value']
            except:
                direction = 'Null'

            try:
                whichFunction= dataDict["outcomes"][0]["entities"]['whichFunction'][0]['value']
            except:
                whichFunction = 'Null'

            try:
                "Print text"
                text= dataDict["outcomes"][0]["_text"]
                print text
            except:
                text = 'Null'



            tableToPublish[0] = intent
            tableToPublish[1] = str(number)
            tableToPublish[2] = str(whichCommands)
            tableToPublish[3] = colour
            tableToPublish[4] = howFast
            tableToPublish[5] = str(confidence)
            tableToPublish[6] = direction
            tableToPublish[7] = whichFunction
            tableToPublish[8] = text
            print "intent: " + intent




        except:
            tableToPublish[0] = "NULL"
            print('\n' "Intent: Null" '\n')


        msg_to_send= Num()
        msg_to_send.some_strings = tableToPublish
        rospy.loginfo(msg_to_send)
        print (" ")
        pub.publish(msg_to_send)
        rate.sleep()
