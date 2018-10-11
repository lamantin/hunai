#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding=utf8
import sys
import urllib2
import json
import signal
import datetime
import random
import subprocess
reload(sys)
sys.setdefaultencoding('utf8') 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import scipy.io.wavfile
from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft as fft
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored, cprint
from pygame import mixer
import pygame
import requests
import thread, time
from Recorder import record_audio, read_audio
import feedparser
def input_thread(L):
    raw_input()
    L.append(None)

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = 'OQXGXI7Z4VE57JHYZGGRELCZZCXDYDSK'

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)
    
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
    
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    
    # converting response content to JSON format
    data = json.loads(resp.content)
    
    # get text from data
    try:
        text = data['_text']
    except:
        return    
    text =  text.encode('utf8') 
    
    hunai(text)
    # return the text
    return text

def idojaras():
    #speak("pillanat , ki nézek az ablakon")
    f = urllib2.urlopen('http://api.wunderground.com/api/815014206c9817bc/forecast/lang:HU/q/Hungary/Marcali.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    #print parsed_json
    try:
        szoveg = (parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext_metric']).decode('utf-8')
        speak(szoveg)
    except:
        szoveg = (parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext_metric']).decode('utf-8')
        speak(szoveg)
    finally:
        pass

    f.close()
    return
    
    

def intro():
    speak(u"Mindannyiunknak szüksége van álmokra. Mindannyiunknak szüksége van a reményre, hogy többet is elérhetünk annál, amink van.")

def logo2():    
    cprint( """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmMN..h`` + :- `   `` `   +mMmMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd ` s`//-. +:.    `.  `MMNNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdysh/mMm:o- `   -d+``/MMNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMyNMMMMM/:.  `dMh sNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.+:  :-MNm.NMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd/-:N- +:NMMhhdMMMNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/   o` -.hmMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdmsy+ssNMMMMMNdNMMMMMMMMMMMMMMMMMMMmh.   ` .+ ++sMMMMMMNMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.      -/-`  ./NMdhMMMMNMMMMMMMMMNy-     .-y.`: :MNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNhmss/.`       ---.-omMdyhhNddNms.      `//  `  /MMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh.ohNMMNmNyo:`                                   dMMdMNMMMMMMMMMMMMMMM
MMMmhMMMMMMMMMMMMMMMMMMMMMMMMMMMyomMMMMMMMMMh+                                :MMMMMNMmMMMMMMMMMMMMM
MMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMyyomMMMMyhMMms/                              `NMMMMMMMMMMMMMMMMMMMM
MNmoMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh.  dMMMMMMMMMMd/           .-//o/-` .:     /NdMMMMMMNMMMMMMMMMMMMM
MmmyMMMMMMMMMMMMMMMMMMMMMMMMMMMMm++``+dMMMMMMMMMMN-       /hhdMMMmsy+ymsm: -hMMMNMMMMMNMMMMMMMMMMMMM
MNhhMMMMMMMMMMMMMMMMMMMMMMMMMy+ho/-   /MMMMMMMMMMMd      .hNh-mMN+s.  oNm/hMMMMMNMMMMMMMMMMMMMMMMMMM
MMdMMMMMMMMMMMMMMMh//ohmNmMs:       .oNMMMMMMMMMMMN`        ...:..`...o` :MMMMMMMMMMMMMNMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMm.                mMMMMMMMMMMMMMM.              ``.``  yMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM-               sMMMMMMMMMMMMMM/                     sdMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMN/              +MMMMMMMMMMMMMMs                     oNNNMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMh             .mMMMMMMMMMMMMMMm                     oMMNNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMd`          `sMMMMMMMMMMMMMMMMs                     mNNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMm`        `oNMMMMMMMMMMMMMMMMMo                    `MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMM+       .sNMMMMMMMMMMMMMMMMMMMN-                   `MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMs    .omMMMMMMMMMMMMMMMMMMMMMMM/                   `MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMdo+ymMMMMMMMMMMMMMMMMMMMMMMMMMM-                   /MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                   hMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm                  /MMMNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMM:   .:+dmMNMMMMMNNNhddyhmdyyyy/`.                  /MMMMNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMy.     .oNNMMMMMMNy: `                             /MMNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNN`   `omMMMMMMMMMMMMh`                            ..dMMMMMmMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMo    -NMMMMMMMMMMMMMMMmds+-                      /h sNMMMMMNNNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNM+       :NMMMMMMMMMMMMs+::/so                    ymy sMNdMNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMh+        +MMMMMMMMMMMMd+:                       --+oo sMydMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMM/     .ohNMMMMMMMMMMMMMMd                      om`-++ hh+hMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNMN- `+dMMMMMMMMMMMMMMMMMMo                    .dMm`:++ m-oMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMmohMMMMMy+mMNmmNmMNMNh-                    :ddMh`/+` y.ymMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMm+-os``` .`.                     `sMNMM.--`. +``.dMMMMMMMMMMMMMMd/..:sNMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMd-                            `smMMMMh      `   `+NMMMMMMMMMMMd.     `hMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMN.                          `+NMMMMNmh            -hMMMMMMMMMM+       `mMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMd-                        /NMMmmMMmMs`             :mMMMMMMMM.        oMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMh.                      yMMMMMdMNmh..`             hMMMMMMMo          .+h
MMMMMMMMMMMMNhymMMMMMMMMMMMd-                     yMMMMMNshso.` /            oMMMMMMN/              
MMMMMMMMMMMMMMm``:ymMMMMMMMMm.                  `hMMMMMMyyo:+s. .           oMMMMMms`               
MMMMMMMMMMMMMMM:    .+hNMMMMMd                 -mmMMMMMd:oyhmy-             :hho/.                  
MMMMMMMMMMd+-.`         :oshhh.               oNMMMMMMos/yMddy/                                     
MMMMMMNmdm.                               ./sNMMMMMMMssydMMdMsho                                    
-yyMMMmy-                          .hhhddNMMMMMMMMMMNhhyNNMMNsd+                                    """, 'green', 'on_grey')

def logo():
    cprint("""  
██╗  ██╗██╗   ██╗███╗   ██╗     █████╗ ██╗         ██╗    ██████╗ 
██║  ██║██║   ██║████╗  ██║    ██╔══██╗██║        ███║   ██╔═████╗
███████║██║   ██║██╔██╗ ██║    ███████║██║        ╚██║   ██║██╔██║
██╔══██║██║   ██║██║╚██╗██║    ██╔══██║██║         ██║   ████╔╝██║
██║  ██║╚██████╔╝██║ ╚████║    ██║  ██║██║         ██║██╗╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝         ╚═╝╚═╝ ╚═════╝ 
                                                                  
(HUN AI) Magyarul értő mesterséges inteligencia """, 'yellow', 'on_grey')
    

class cfile(file):
    #subclass file to have a more convienient use of writeline
    def __init__(self, name, mode = 'r'):
        self = file.__init__(self, name, mode)

    def wl(self, string):
        self.writelines(string + '\n')
        return None

def speak(audioString):
    tts = gTTS(text=audioString, lang='hu')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3 > /dev/null 2>&1")

def speak_pure(audioString):
    command = 'espeak -vhu+f5 '+str(audioString)
    execute_unix(command)    
    
# old way 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
    
    except sr.UnknownValueError:
        return
    except sr.RequestError as e:
        return
    return data

def hirek():
    d = feedparser.parse('https://news.google.hu/?output=rss')
    count = 0
    articles = []
    for  n,item in enumerate(d['items']):
        if n==0:
           continue 
        speak(item['title'].encode('utf8'))
       

 
def hunai(data):
    try:
        print data

        if "szia" in data:
            answers = [u'Szevasz ',u'Háj',u'Jó napot kívánok',u'Na mi van',u'Adj Isten']
            speak(random.choice(answers))
            

        if "demo" in data:
            speak("Szia ,Rozi vagyok segítek a háztartásban beszélgethetsz velem vagy társammal")
            speak_pure(u"Jaja")

        if "intro" in data:
            logo2()
            intro()
        
	    if "mi a szabály" in data:
	       speak("A bevétel erősíti a szabályt")	

	    if "Mi az élet értelme" in data:
	       speak("Negyvenkettő")
	
        if "Örkény" in data:
            orkeny = "Egy parafa dugó, mely semmiben sem különbözött a többi parafa dugótól (Hirt G. Sándornak mondta magát, de mit jelent egy név? Egy név semmit se jelent), beleesett a vízbe."\
            "Egy ideig, amint az várható volt, úszott a víz színén, aztán különös dolog történt. Lassan merülni kezdett, lesüllyedt a fenékre, és nem jött föl többé."\
            "Magyarázat nincs."
            orkeny = unicode(orkeny, "utf-8")
            speak(orkeny)

        if "József Attila" in data:
            ja = "Akárhogyan lesz, immár kész a leltár.Éltem - és ebbe más is belehalt már."
            ja = unicode(ja, "utf-8")
            speak(ja)

        if "József Attilá" in data:
            ja = "Akárhogyan lesz, immár kész a leltár.Éltem - és ebbe más is belehalt már."
            ja = unicode(ja, "utf-8")
            speak(ja)    

        if "Google" in data:
            speak("Mondom ungáris")
        if "Rozi megsértődtél" in data:
            speak("dehogy sértődtem meg , csak unlak")
        if "Hi Alexa" in data:
            speak("Ki az az Alexa és mi dolgod vele")

        if "Alexa" in data:
            speak("Ki az az Alexa és mi dolgod vele")    
            
        if  "Rozi" and "magadról" in data:
            speak("Egy egyszerűen csodálatos nő vagyok")    

        if "Jókai" in data:
            speak("A hallgatás és a nem szólás két különböző dolog.") 
        
        if "jókai" in data:
            speak("A hallgatás és a nem szólás két különböző dolog.")    

        if "babits" in data :
            speak("Egy szellemes paradoxon többet ér egy lapos bölcsességnél.")
            
            
        if "hey Siri" in data:
            speak("Benézted .Csak magyarul beszélek")

        if "Hey Siri" in data:
            speak("Benézted .Csak magyarul beszélek")    

        if "Rozi" in data:
            answers = [u'Szevasz ',u'Lökjed',u'Mit szeretnél',u'Na mi van',u'Nincs más dolgod , mint velem beszélgetni ?']
            speak(random.choice(answers))
            

        if "hírek" in data:
            hirek()


        if "mennyi az idő" in data:
            d = datetime.datetime.now()
            speak("a pontos idő " +str(d.hour)+"óra "+str(d.minute)+"perc")    

        if "időjárás" in data:
            idojaras()  

        if  "hogy vagy"  in data:
            answers = ['Minden rendben','Kicsit fáj a fejem','Álmos vagyok','Remekül érzem magam','Hogy lehetnék , nem forrtak még fel a processzoraim']
            speak(random.choice(answers))
                
        if  "exit" in data :
            speak("a program kikapcsol , viszlát !")
            os.kill(os.getpid(), signal.SIGUSR1) 

        if  "viszlát" in data :
            speak("a program kikapcsol , viszlát !")
            os.kill(os.getpid(), signal.SIGUSR1)
        if "náci" in data:
            speak("es ist mein kampf")

        if "zsidó" in data:
            speak("ne zsidózz")

        if 'cigány' in data:
            speak("ne cigányozz szőke geci")            
        
        if "hol van a marcimgyerek" in data:
            speak("lilinél van")        
               

    except:
        speak("ezt ismételd meg kérlek")
        return  
    return     
      

def main_loop():
    L = []
    thread.start_new_thread(input_thread, (L,))
    while 1:
        time.sleep(.1)
        if L: break
        RecognizeSpeech('myspeech.wav', 5)


def init():
    # speak("hello te ló")
    # initialization
    sys.stderr.write("\x1b[2J\x1b[H")
    logo2()

    print "modulok betöltve , kérem szólítson meg : Rozi vagy Szia Rozi"
    
    main_loop()
                
    
init()
