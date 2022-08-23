import os
import time
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\kunal\\PycharmProjects\\pythonProject\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome()
driver.get('https:google.com')
print(type(driver))
driver.maximize_window()
myPageTitle = driver.title
print(myPageTitle)
# Banking browser
driver.find_element(By.xpath, "/html/body/div/div/div[1]/button[1]").click()
driver.find_element(By.xpath, "/html/body/div/div/div[1]/strong").send_keys("XYZ Bank")
time.sleep(2)
