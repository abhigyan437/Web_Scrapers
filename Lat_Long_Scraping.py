import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

data = pd.read_excel("2nd assignment.xlsx")
browser = webdriver.Chrome('C:\Drivers\chromedrive.exe')
list_url = []
list_lat = []
list_long = []
browser.get("https://www.google.co.in/maps/")
for x in data.Address:
    browser.find_element(By.ID, "searchboxinput").send_keys(str(x))
    browser.find_element(By.ID, "searchbox-searchbutton").click()
    time.sleep(1)  # Depends entirely on the speed of the Internet & the processor speed
    url = browser.current_url
    latlong = url.split("/")[6]
    list_url = latlong.split(",")
    list_lat.append(str(list_url[0])[1:])
    list_long.append(list_url[1])
    browser.find_element(By.CLASS_NAME, "gsst_a").click()
data.Latitude = list_lat
data.Longitude = list_long
browser.close()
data.to_csv("2nd assignment_Abhigyan.csv")
