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


def network(company, counter, limit):
    # connect_btns = driver.find_elements_by_xpath(//button/span[@value = Connect]")
    divs = driver.find_elements_by_xpath(//div[@class = "entity-result__item"])
    first_name = "" #set name
    
    # setting up the message ----- BEGIN

    msg = "Hi " + first_name + ", \n I hope you’re doing well. I’m Shahaf, a Junior CS student at BU - nice to meet you! I’m interested in applying for the Summer '21 SE Intern role at " + company + " and was wondering if you had 15 minutes to talk about your time at the company. \n Please let me know what works! \n\n Thank you, Shahaf"

    # setting up the message ----- END
    iterator = 0
    while (iterator < divs.len() & counter < limit):
        if (divs[iterator].find_element_by_xpath(".//button[@data-control-name = 'entity_action_primary']/span").text == "Connect"):
            divs[iterator].find_element_by_xpath(".//button[@data-control-name = 'entity_action_primary']").click() #click the connect btn
            delay() #push a little
            divs[iterator].find_element_by_xpath(".//button[@label = 'Add a note']").click() #click the add a note btn
            textarea = divs[iterator].find_element_by_xpath(".//textarea[@id = 'custom-message']")
            textarea.send_keys(msg)

        #connection process CODE here ------

        #connection process CODE done ------
        counter, iterator += 1
        if (iterator == connect_btns.len()):
            #press next page

    return



def delay:
    time.sleep(random.randint(2,3))

driver = webdriver.Firefox(executable_path = "/Users/shahafdan/Document/Projects/scripts/drivers/geckodriver") # define a driver browser to open
url = ""; # DEFINE URL BASED ON COMPANY
company = "" # DEFINE COMPANY BASED ON DESIRED SEARCH
driver.get(company, 0, 50)
delay() 


outputFile = open('networking.txt', "w+") #open output file
outputFile.write(all_text) #write all html code (manipulated, prefereable) inthere
driver.quit() #close browser, done