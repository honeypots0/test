import time
from selenium import webdriver  
import os 

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
os.system("service tor start")

def ur(): 
	a = 0	
	for i in inputFile.readlines():
				os.system("service tor reload")
				url = str(i)
				a = int(a) + 1
				try:
					myProxy = "127.0.0.1:9050"

					ip, port = myProxy.split(":")
					driver = webdriver.FirefoxProfile()
					driver.set_preference('network.proxy.type', 1)
					driver.set_preference('network.proxy.socks', ip)
					driver.set_preference('network.proxy.socks_port', int(port))
					# driver = webdriver.Firefox(driver)

					firefox_options = webdriver.FirefoxOptions()
					firefox_options.add_argument("--private")
					browser = webdriver.Firefox(driver , firefox_options=firefox_options)
					browser.get(url)
					try:
						os.system("clear")
						print(Fore.RED + Fore.BOLD +'Link : '+Fore.GREEN +url)			
						print(Fore.RED + Fore.BOLD +'Number : '+Fore.GREEN + str(a) + "\n")
						print(Fore.RED + Fore.BOLD +'Title: '+Fore.GREEN +  browser.title + "\n")
						time.sleep(15)
						print(Fore.RED + Fore.BOLD +'Click : '+Fore.GREEN + " On Skip" + "\n")
						element = browser.find_element_by_id("skip_button")
						element.click()
						time.sleep(10)
						print(Fore.RED + Fore.BOLD +'Click : '+Fore.GREEN + " Close Browser"+ "\n")
						browser.quit()
					except:
						pass
				except:
					print("Something Wrong")

ur()
