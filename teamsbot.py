from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time





url = "https://teams.microsoft.com"
login_cred = {'email' : '', 'pass' : ''}
driver = None

def login() :
    global driver
    email = driver.find_element_by_xpath("//form[@id='i0116']")
    email.click()
    email.send_keys(login_cred['email'])
    driver.find_element_by_xpath("//form[@id='idSIButton9']").click()
    time.sleep(10)
    password = driver.find_element_by_xpath("//form[@id='i0118']")
    password.click()
    password.send_keys(login_cred['pass'])
    driver.find_element_by_xpath("//form[@id='idSIButton9']").click()
    time.sleep(10)



