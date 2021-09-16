from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
import logging

URL = "https://teams.microsoft.com"

# Initialize driver

def initDriver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver 
    driver = webdriver.Chrome(executable_path=execPath, chrome_options=options)

def parseCreds():
    with open('.config.json') as f:
        jsonObj = json.load(f)
    email = jsonObj['email']
    password = jsonObj['password']
    global execPath
    execPath = jsonObj['chromedriver']
    return email, password

def login(email, password):
    initDriver()
    driver.get(URL)
    time.sleep(5)
    sendEmail = driver.find_element_by_xpath("//form[@id='i0116']")
    sendEmail.click()
    sendEmail.send_keys(email)
    driver.find_element_by_xpath("//form[@id='idSIButton9']").click()
    time.sleep(10)
    sendPassword = driver.find_element_by_xpath("//form[@id='i0118']")
    sendPassword.click()
    sendPassword.send_keys(password)
    driver.find_element_by_xpath("//form[@id='idSIButton9']").click()
    time.sleep(10)

if __name__ == "__main__":
    email, password = parseCreds()
    logging.warning(f"Attempting login with creds: {email} - {password}")
    login(email, password)
    time.sleep(10)
    logging.warning("Log in successful")
    print("Quitting.....")
    driver.quit()