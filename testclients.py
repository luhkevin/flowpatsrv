from time import sleep
import requests
import threading

speeds=['http://54.152.245.102:8886/', 'http://54.152.245.102:8887/']
reqSize=100

#We don't delay slow because there's already a delay from server response
delay=[0.5,0]

def requestWorker(speed, delay):
    for i in range(reqSize):
        req=requests.get(speed)
        print "Req: " + req.text
        sleep(delay)

threads=[]
for i in range(2):
    t=threading.Thread(target=requestWorker, args=(speeds[i],delay[i]))
    threads.append(t)
    t.start()

