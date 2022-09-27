from http import server
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random

from soupsieve import select

path = "C:\Program Files (x86)"

def signinfb(driver):

    
    # driver.get("facebook.com")
    # time.sleep(2)

    # #Locating element
    # username = driver.find_element(By.ID,"email")
    # username.click()
    # username.send_keys("enter your email id")
    # password = driver.find_element(By.ID,"pass")
    # password.click()
    # password.send_keys("enter your password")



    # sign = driver.find_element(By.XPATH,"//button[@id='u_0_9_NT']").click()  
    # time.sleep(2)

    driver.get("https://www.facebook.com/groups/smartpokies")











if __name__=="__main__":
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #driver_service = Service(executable_path = "C:\Program Files (x86)\chromedriver.exe")
    #driver = webdriver.chrome(service = driver_service) 
    driver = webdriver.Chrome(executable_path = "C:\Program Files (x86)\chromedriver.exe")
    driver.maximize_window()  

    # PostJob(driver)
    # delJob(driver)
    signinfb(driver)
    #driver.close()
