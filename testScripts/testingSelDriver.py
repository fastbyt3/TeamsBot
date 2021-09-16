from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"D:\programming\Project-TeamsBot\TeamsBot\src\chromedriver.exe",chrome_options=options)

driver.get('https://pronoun.is/he')

time.sleep(10)

driver.get('https://github.com/fastbyt3')

time.sleep(10)

driver.quit()