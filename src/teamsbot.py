from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json




url = "https://teams.microsoft.com"
driver = None

def parseCreds():
    with open('.creds.json') as f:
        jsonObj = json.load(f)
    email = jsonObj['email']
    password = jsonObj['password']
    # print(email, password)
    return email, password

def login(email, password) :
    global driver
    email = driver.find_element_by_xpath("//form[@id='i0116']")
    email.click()
    email.send_keys(email)
    driver.find_element_by_xpath("//form[@id='idSIButton9']").click()
    time.sleep(10)
    password = driver.find_element_by_xpath("//form[@id='i0118']")
    password.click()
    password.send_keys(password)
    driver.find_element_by_xpath("//form[@id='idSIButton9']").click()
    time.sleep(10)



email, password = parseCreds()
login(email, password)