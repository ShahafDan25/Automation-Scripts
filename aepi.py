import os
import random
import time
import selenium
import webdriver_manager

#selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.firefox.options import Options

#recaptcha libraries
import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub
import time
import sys

# ---------------- RECAPTCHA SOLVER CODE AND FUNCTIONS ---------------------
def delay ():
    time.sleep(random.randint(2,3))


    
def fucker_solver(driver):
    #switch to recaptcha frame
    # frames=driver.find_elements_by_tag_name("iframe")
    # driver.switch_to.frame(frames[0]);
    delay()

    #click on checkbox to activate recaptcha
    # driver.find_element_by_class_name("recaptcha-checkbox-border").click() #-----------------------------------

    #switch to recaptcha audio control frame
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()    # frames=driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe") #-----------------------------------
    # frames=driver.find_elements_by_tag_name("iframe") #-----------------------------------
    # driver.switch_to.frame(frames[0]) #-----------------------------------
    delay() #-----------------------------------

    #click on audio challenge   
    print ("--------------------------- 1 -------------------------------")
        #switch to recaptcha audio challenge frame
    driver.switch_to.default_content()
    frames= driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(frames[-1])
    delay()

    # #click on the play button
    # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge']")))
    WebDriverWait(driver, random.randint(4,5)).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(3).rc-autiochallenge-play-control div.rc-audiochallenge-play-button button.rc-button-default"))).click()    
    # frames=driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe") #-----------------------------------
    print ("--------------------------- 2 -------------------------------")
    delay()

    #get the mp3 audio file
    src = driver.find_element_by_id("audio-source").get_attribute("src")
    print("[INFO] Audio src: %s"%src)
    #download the mp3 audio file from the source
    urllib.request.urlretrieve(src, os.getcwd()+"\\sample.mp3")
    sound = pydub.AudioSegment.from_mp3(os.getcwd()+"\\sample.mp3")
    sound.export(os.getcwd()+"\\sample.wav", format="wav")
    sample_audio = sr.AudioFile(os.getcwd()+"\\sample.wav")
    r= sr.Recognizer()

    with sample_audio as source:
        audio = r.record(source)

    #translate audio to text with google voice recognition
    key=r.recognize_google(audio)
    print("[INFO] Recaptcha Passcode: %s"%key)

    #key in results and submit
    driver.find_element_by_id("audio-response").send_keys(key.lower())
    driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
    driver.switch_to.default_content()
    delay()
    driver.find_element_by_id("recaptcha-demo-submit").click()
    delay()









driver = webdriver.Firefox(executable_path = "/Users/shahafdan/Document/Projects/scripts/drivers/geckodriver") # define a driver browser to open
delay()
total = ""
i = 0
names = ["Levi", "Levin", "Levis", "Leviss", "Rosen", "Rosenn", "Stein", "Goldberg", "Goldstein", "Cohen", "Cohan", "Lerman", "Herman", "Shulman", "Goldman", "Silverman", "Ossman", "Canter", "Meyer", "Miller", "Miler", "Katz", "Kats", "Kahn", "Weissman", "Weiss", "Gross", "Greissman", "Rothstein", "Steinberg", "Goldberg", "Aaron", "Aaronson", "Rubin", "Mandelbaum", "Baum", "Arenson", "Barber", "Becker", "Becher", "Siegal", "Lavi", "Gold", "Lieberman", "Lieb", "Leah", "Rubin", "Lewenberg", "Levinsky", "Hakim", "Shapiro", "Green", "Shapira", "Berg", "Greenberg"]
while i < len(names):
    url =  'https://www.bu.edu/phpbin/directory/?q='+names[i]  # set URL  
    driver.get(url) #open in browser
    time.sleep(2)
    fucker_solver(driver) #resolve recaptcha with designtaed function
    time.sleep(2) #let it load
    html = driver.page_source #load HTML hardcode frmo the page
    total += html #concating it. TODO: later, manipulate it here instead of later
    print(html)
    print("------------------------------------------------")

    i += 1 #next jewish last name in the list, please


# close web browser
outputFile = open('aepi.txt', "w+") #open output file
outputFile.write(total) #write all html code (manipulated, prefereable) inthere
driver.quit() #close browser, done

