#-*-coding:UTF-8 -*-
import sys
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import importlib
importlib.reload(sys)

def selenium_ergodic():
    f = open("output.html", "r", encoding="utf-8")
    line = f.readline()
    list_url = []
    for url in range(0, 35):
        patterm = re.compile(r'((https|http)\://[a-zA-Z0-9\.\?/&\=\:]+)')
        result = re.findall(patterm, line)
        print(line)
        print(result[0][0])
        list_url.append(result[0][0])
        line = f.readline()

    for i in range(0, 15):
        driver = webdriver.Chrome('/Users/andy/driver/chromedriver')
        driver.get(list_url[i])
        # assert "Python" in driver.title
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("python")
        # elem.send_keys(Keys.RETURN)










