import time
from selenium import webdriver  
import os 
from selenium.webdriver.common.keys import Keys

class Fore:
   PURPLE = '\033[95m'
   MAGENTA = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'
   BGC = '\033[103m'
   WHITE = '\033[37m'
ifile = "ready.txt"
inputFile=open(ifile,'r')	
def ur(): 
	a = 0	
	for i in inputFile.readlines():
				url = i
				a = int(a) + 1
				try:
					firefox_options = webdriver.FirefoxOptions()
					firefox_options.add_argument("--private")
					browser = webdriver.Firefox(options=firefox_options)
					browser.get('http://evolterr.com/3CcY')
					os.system("clear")
					print(Fore.RED + Fore.BOLD +'Link : '+Fore.GREEN +url)			
					print(Fore.RED + Fore.BOLD +'Number : '+Fore.GREEN + str(a) + "\n")
					print(Fore.RED + Fore.BOLD +'Title: '+Fore.GREEN +  browser.title + "\n")
					time.sleep(15)
					print(Fore.RED + Fore.BOLD +'Click : '+Fore.GREEN + " On Skip" + "\n")
					element = browser.find_element_by_id("skip_bu2tton")
					element.click()
					time.sleep(10)
					print(Fore.RED + Fore.BOLD +'Click : '+Fore.GREEN + " Close Browser"+ "\n")
					browser.quit()
				except:
					print("Something Wrong")

import threading

t1 = threading.Thread(target=ur)
t1.start()

    # profile = webdriver.FirefoxProfile()
    # options = webdriver.FirefoxOptions()
    # options.set_preference("dom.webnotifications.serviceworker.enabled", False)
    # options.set_preference("dom.webnotifications.enabled", False)
    # options.add_argument('--headless')

    # browser = webdriver.Firefox(firefox_profile=profile,options=options)
    # return browser
# os.system("sudo service tor start")
# proxyDict = { 
#               "http"  : "http://127.0.0.1:8080", 
#               "https" : "https://127.0.0.1:8080", 
#               "ftp"   : "ftp://127.0.0.1:8080"
#             }
# def ur(): 	
# 	for i in inputFile.readlines():
# 			url = i
# 			for i in range(1):
# 				print("url number : " ,i)
# 				os.system("sudo service tor reload")				
# 				print("url : ", url)
# 				# try:  
# 				r = rq.get(url)
# 				print(r.text) 
# 				try:
# 				# os.system(f"echo '{rw}' | grep 'value='")
# 					a_child_process = subprocess.Popen(args=["firefox", "--private-window", f"{url}"], stdout=subprocess.PIPE)	
# 					print(a_child_process)

# 					# search_bar = driver.find_element_by_name("q")
# 					# search_bar.clear()
# 					# search_bar.send_keys("getting started with python")
# 					# search_bar.send_keys(Keys.RETURN)
# 					# print(driver.current_url)
# 					time.sleep(20)
# 					print("click on skip")
# 					os.system("xdotool mousemove 1520 195 click 1")
# 					time.sleep(10)
# 					os.system("xdotool mousemove 1585 45 click 1")
# 					print("click on menu close")
# 				except:
# 					pass

# import threading

# t1 = threading.Thread(target=ur)
# t1.start()
