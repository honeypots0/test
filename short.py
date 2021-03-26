import subprocess as sp 
import time 
import os 
import pyautogui
ifile = "ready.txt"
os.system("service tor start")
inputFile=open(ifile,'r')
for url in inputFile.readlines():
    os.system("service tor reload")
    print(url)
    child = sp.Popen("firefox --private-window %s" % url, shell=True) 
    # print("time sleep") 
    for i in range(60):
        print("Time Sleep: " , i)
        time.sleep(1)
    pyautogui.click(1503,188)
    for i in range(20):
        print("Click Time Sleep: " , i)
        time.sleep(1)    
    browserExe = "firefox" 
    os.system("pkill "+browserExe) 
    print("kill browser")

