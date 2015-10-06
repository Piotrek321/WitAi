#!/usr/bin/env python
#-*- coding: utf-8 -*-
import alsaaudio, wave, numpy

def record(czasNagrywania, numerPliku):
	RATE = 16000
	CHUNK = 1024
	inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
	inp.setchannels(1)
	inp.setrate(RATE)
	inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
	inp.setperiodsize(CHUNK)
	path = '../Sounds/file' + str(numerPliku) + '.wav'
	w = wave.open(path , 'w')
	w.setnchannels(1)
	w.setsampwidth(2)
	w.setframerate(RATE)
	print "Nagrywanie"


	for x in range(int(RATE / CHUNK * czasNagrywania)):
	    l, data = inp.read()
	    a = numpy.fromstring(data, dtype='int16')
	    #print numpy.abs(a).mean()
	    w.writeframes(data)

	print "Koniec nagrywania"
	return w.writeframes(data)
