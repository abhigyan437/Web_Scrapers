import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
data = pd.read_csv('url1.csv')
final_data=pd.DataFrame()
product_name_list=[]
cost1_list=[]
cost2_list=[]
memory_size_list=[]
delivery_list=[]
url_list=[]
chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-popup-blocking')
driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver1.exe",options=chrome_options)
driver.get('https://www.bestbuy.com/site/samsung-galaxy-z-fold3-5g-512gb-phantom-black-at-t/6471912.p?skuId=6471912')
time.sleep(5)
country = driver.find_element(By.XPATH,"//img[@alt='United States']")
country.click()
time.sleep(3)
z = 0
for x in data['URL']:
    z = z+1
    print(z)
    try:
        driver.get(x)
        time.sleep(2.5)
        (driver.find_element(By.XPATH, "//button[@aria-labelledby='Cell_Phones_Internal_Memory variation-dropdown-Cell_Phones_Internal_Memory']")).click()
        time.sleep(1.5)
        ele = driver.find_elements(By.XPATH, "//a[@role='option']")
        n = 0
        while n<len(ele):
            memory_size_list.append(ele[n].text)
            ele[n].click()
            time.sleep(5)
            url_list.append(x)
            try:
                product_name_list.append((driver.find_element(By.XPATH, "//h1[@class='heading-5 v-fw-regular']")).text)
            except:
                product_name_list.append("Product Name Missing")
            try:
                cost_1 = (driver.find_element(By.XPATH, "//div[@class='priceView-hero-price priceView-customer-price']")).text
                a = cost_1.split('\n')
                cost_1_part2 = (driver.find_element(By.XPATH, "//span[@class='priceView-price-disclaimer__activation']")).text
                cost1=str(a[0])+str(a[2])+str(cost_1_part2)
                cost1_list.append(cost1)
            except:
                cost1_list.append("Cost 1 Missing")
            try:
                cost_2 = (driver.find_element(By.XPATH, "//button[@class='activated-pricing__button ']")).text
                cost2_list.append(cost_2)
            except:
                cost2_list.append("Cost 2 Missing")
            try:
                try:
                    get_day = driver.find_element(By.XPATH, "//div[@style='color:#318000;margin-bottom:8px']")
                except:
                    get_day = driver.find_element(By.XPATH, "//div[@style='color:#BB0628;margin-bottom:8px']")
                delivery_list.append(get_day.text)
            except:
                delivery_list.append('Earliest Delivery Missing')
            n=n+1
            try:
                (driver.find_element(By.XPATH, "//button[@aria-labelledby='Cell_Phones_Internal_Memory variation-dropdown-Cell_Phones_Internal_Memory']")).click()
                time.sleep(1.5)
                ele = driver.find_elements(By.XPATH, "//a[@role='option']")
            except:
                break
    except:
        url_list.append(x)
        product_name_list.append(" ")
        cost1_list.append(" ")
        cost2_list.append(" ")
        memory_size_list.append(" ")
        delivery_list.append(" ")

try:
    final_data['URL']=url_list
    final_data['Product Name']=product_name_list
    final_data['Memory Size']=memory_size_list
    final_data['Cost 1']=cost1_list
    final_data['Cost 2']=cost2_list
    final_data['Earliest Delivery']=delivery_list
    final_data.to_excel('Output.xlsx')
    print("URL - ", len(url_list))
    print("Memory Size - ", len(memory_size_list))
    print("Cost 1 - ", len(cost1_list))
    print("Cost 2 - ", len(cost2_list))
    print("Earliest - ", len(delivery_list))
    print("Prodcu - ", len(product_name_list))
except:
    print("URL - ",len(url_list))
    print("Memory Size - ",len(memory_size_list))
    print("Cost 1 - ",len(cost1_list))
    print("Cost 2 - ",len(cost2_list))
    print("Earliest - ",len(delivery_list))
    print("Prodcu - ",len(product_name_list))