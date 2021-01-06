import os
import random
import time
import datetime
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

def delay():
    time.sleep(random.randint(2,3))

def network(company, limit):
    counter = 0
    # connect_btns = driver.find_elements_by_xpath(//button/span[@value = Connect]")
    divs = driver.find_elements_by_xpath("//div[@class = 'entity-result__item']")
    
    # setting up the message ----- END
    write_out = ""
    iterator = 0
    while (iterator < divs.len() & counter < limit):
        if (divs[iterator].find_element_by_xpath(".//button[@data-control-name = 'entity_action_primary']/span").text == "Connect"):
            name = "" #GET THE NAME
            first_name = "" #set name using substring of the above name ^
            # setting up the message ----- BEGIN
            msg = "Hi " + first_name + ", \n I hope you’re doing well. I’m Shahaf, a Junior CS student at BU - nice to meet you! I’m interested in applying for the Summer '21 SE Intern role at " + company + " and was wondering if you had 15 minutes to talk about your time at the company. \n Please let me know what works! \n\n Thank you, Shahaf"
            divs[iterator].find_element_by_xpath(".//button[@data-control-name = 'entity_action_primary']").click() #click the connect btn
            delay() #push a little
            divs[iterator].find_element_by_xpath(".//button[@label = 'Add a note']").click() #click the add a note btn
            delay()
            divs[iterator].find_element_by_xpath(".//textarea[@id = 'custom-message']").send_keys(msg) # WRITE THE NOTE OUT
            delay()
            divs[iterator].find_element_by_xpath(".//button[@aria-label = 'Send Now']").click() #CLICK THE SEND BUTTON
            delay()
            counter += 1
            write_out = counter + "\t : \t" + name  + "\t" + company + "\t" + datetime.datetime.now().isoformat() + "\n"
        iterator += 1
        if (iterator == divs.len()): #press next page
            driver
            delay()
            divs = driver.find_elements_by_xpath("//button[@aria-label = 'next']") # go to the next page
            delay()
            iterator = 0
    return write_out



driver = webdriver.Firefox(executable_path = "/Users/shahafdan/Documents/Projects/scripts/drivers/geckodriver") # define a driver browser to open

#1 --- define automation credentials, initiate
url = "https://www.linkedin.com/search/results/people/?currentCompany=%5B%2210667%22%5D&keywords=software%20engineer&origin=FACETED_SEARCH"; # DEFINE URL BASED ON COMPANY
company = "Facebook" # DEFINE COMPANY BASED ON DESIRED SEARCH
limit = 50
delay() #AGAIN

#2 --- log in
driver.get(url)
delay() 
divs = driver.find_elements_by_xpath("//p/a[@data-tracking-control-name = 'cold_join_sign_in']").click() # CLICK SIGN IN LINK(instead of sign up)
delay()
driver.find_element_by_xpath("/html/body/div/main/div/form/div/input[@id = 'username']").send_keys("dan.shachaf@gmail.com") # type email
driver.find_element_by_xpath("/html/body/div/main/div/form/div/input[@id = 'password']").send_keys("Sdan3189@LNKD") # type password
driver.find_element_by_xpath("/html/body/div/main/div/form/div/button[@aria-label = 'Sign in']").click() # click login
delay()





#3 --- network
records = network(company, limit)

outputFile = open('networking.txt', "w+") #open output file
outputFile.write(records) #write all html code (manipulated, prefereable) inthere
driver.quit() #close browser, done