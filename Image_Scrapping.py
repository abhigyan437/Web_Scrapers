from datetime import datetime
import re
import time
from selenium.webdriver import ActionChains
import numpy as np
from urllib.request import urlretrieve
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/drivers/chromedriver.exe")
driver.get("https://www.google.com/search?q=Konica%20Minolta%20Toner%20Cartridges%20Importers%20in%20Kozhikode&tbs=lf:1,lf_ui:2&tbm=lcl&rflfq=1&num=10&rldimm=8224764845842473269&lqi=CjZLb25pY2EgTWlub2x0YSBUb25lciBDYXJ0cmlkZ2VzIEltcG9ydGVycyBpbiBLb3poaWtvZGWSARJjb21tZXJjaWFsX3ByaW50ZXKqATEQASotIilrb25pY2EgbWlub2x0YSB0b25lciBjYXJ0cmlkZ2VzIGltcG9ydGVycygA&ved=2ahUKEwjO7KqVkNz1AhWAgtgFHaawBgkQvS56BAgLEDU&rlst=f#rlfi=hd:;si:13062469072224787122,l,CjZLb25pY2EgTWlub2x0YSBUb25lciBDYXJ0cmlkZ2VzIEltcG9ydGVycyBpbiBLb3poaWtvZGVIrZO6p8yPgIAIWkgQABABEAIQAxAEGAIYAxgGIjZrb25pY2EgbWlub2x0YSB0b25lciBjYXJ0cmlkZ2VzIGltcG9ydGVycyBpbiBrb3poaWtvZGWSARh0b25lcl9jYXJ0cmlkZ2Vfc3VwcGxpZXKqATEQASotIilrb25pY2EgbWlub2x0YSB0b25lciBjYXJ0cmlkZ2VzIGltcG9ydGVycygA;mv:[[11.304348899999999,75.790934],[11.243601799999999,75.7815782]]")
#action = ActionChains(driver)
# right click operation

driver.get("https://www.youtube.com")
"""while(driver.title!="good morning - Google Search"):
    pass
driver.find_element(By.XPATH,'//div[@class="bRMDJf islir"]').click()
time.sleep(5)
ele=driver.find_element(By.XPATH,"//img[@class='n3VNCb']")
time.sleep(5)
src = ele.get_attribute('src')
print(src)
time.sleep(5)
urlretrieve(src, "captcha.png")"""
