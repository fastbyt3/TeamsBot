from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
import logging

URL = "https://teams.microsoft.com"

logging.basicConfig(filename='testing.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Initialize driver

def initDriver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver 
    driver = webdriver.Chrome(executable_path=execPath, chrome_options=options)

def parseCreds():
    with open('.config.json') as f:
        jsonObj = json.load(f)
    global email, password
    email = jsonObj['email']
    password = jsonObj['password']
    global execPath
    execPath = jsonObj['chromedriver']

def login():
    driver.get(URL)
    time.sleep(3)
    logging.debug("Loaded site... attempt log in....")
    # Input : email
    element = driver.find_element_by_name("loginfmt")
    element.send_keys(email)
    element = driver.find_element_by_id("idSIButton9")
    element.click()
    logging.debug("Passed username page ✔")

    # Input: password
    time.sleep(3)
    element = driver.find_element_by_name("passwd")
    element.send_keys(password)
    element = driver.find_element_by_id("idSIButton9")
    element.click()
    logging.debug("Password page passed ✔✔")

    # "Stay signed in" page
    time.sleep(3)
    element = driver.find_element_by_id("idSIButton9")
    element.click()
    logging.debug("Stay signed in - YES ✔")

def joinClass():
    # Jumps to Calender which shows all classes scheduled for that week
    # driver.get("https://teams.microsoft.com/_#/calendarv2")
    # allTeams = driver.find_element
    # print(allTeams)
    # ids = driver.find_elements_by_xpath('//*[@id]')
    # for i in ids:
    #     print(i)
    pass

if __name__ == "__main__":
    parseCreds()
    logging.debug(f"Attempting login with creds: {email} - {password}")
    initDriver()
    login()
    logging.debug("Log in successful")
    time.sleep(10)
    logging.debug("Switching over to teams calender")
    joinClass()
    time.sleep(5)
    logging.debug("Quitting")
    # driver.quit()