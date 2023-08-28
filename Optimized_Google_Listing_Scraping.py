from datetime import datetime
import re

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver.exe")
load=0
data=pd.DataFrame()
list_name =[]
list_keyword=[]
list_link=[]
list_address=[]
list_city=[]
list_pin=[]
list_phone=[]
list_email=[]
list_site=[]
list_rating_count=[]
list_rating=[]
list_product1=[]
list_product2=[]
list_product3=[]
list_product4=[]
list_product5=[]
list_product6=[]
list_product7=[]
list_product8=[]
list_state=[]
empty=np.nan
iyu = 0
#
product = 'GPS Tracker for Truck'
#Avoid Traders
#,'Importers','Suppliers','Distributors','Manufacturers','Exporters','Wholesalers','Retailers','Traders', 'Associations','Service Providers'
categories = ['Suppliers']#Follow This
#cities = ['Vijayawada', 'Vellore']
cities = ['Vijayawada', 'Vellore', 'Vadodara', 'Thrissur', 'Thiruvananthapuram', 'Thane', 'Surat', 'Secunderabad', 'Rajkot', 'Pondicherry', 'Panipat', 'Noida', 'New Delhi', 'Navi Mumbai', 'Nashik', 'Nagpur', 'Mumbai', 'Mohali', 'Mangalore', 'Madurai', 'Ludhiana', 'Lucknow', 'Kozhikode', 'Kolkata', 'Kochi', 'Kanpur', 'Kanchipuram', 'Kalyan', 'Jalandhar', 'Jaipur', 'Indore', 'Hyderabad', 'Howrah', 'Hooghly', 'Guwahati', 'Gurgaon', 'Greater Noida', 'Goa', 'Delhi', 'Faridabad', 'Ernakulam', 'Dehradun', 'Cuttack', 'Coimbatore', 'Chinchwad', 'Chennai', 'Chandigarh', 'Bikaner', 'Bhopal', 'Bengaluru', 'Belgaum', 'Ahmedabad', 'Agra']
dic = {'Agra': 'Uttar Pradesh', 'Ahmedabad': 'Gujarat', 'Belgaum': 'Karnataka', 'Bengaluru': 'Karnataka', 'Bhopal': 'Madhya Pradesh', 'Bikaner': 'Rajasthan', 'Chandigarh': 'Chandigarh', 'Chennai': 'Tamil Nadu', 'Chinchwad': 'Maharashtra', 'Coimbatore': 'Tamil Nadu', 'Cuttack': 'Odisha', 'Dehradun': 'Uttarakhand', 'Delhi': 'Delhi', 'Ernakulam': 'Kerala', 'Faridabad': 'Haryana', 'Ghaziabad': 'Uttar Pradesh', 'Goa': 'Goa', 'Greater Noida': 'Uttar Pradesh', 'Gurgaon': 'Haryana', 'Guwahati': 'Assam', 'Hooghly': 'West Bengal', 'Howrah': 'West Bengal', 'Hyderabad': 'Telangana', 'Indore': 'Madhya Pradesh', 'Jaipur': 'Rajasthan', 'Jalandhar': 'Punjab', 'Kalyan': 'Maharashtra', 'Kanchipuram': 'Tamil Nadu', 'Kanpur': 'Uttar Pradesh', 'Kochi': 'Kerala', 'Kolkata': 'West Bengal', 'Kozhikode': 'Kerala', 'Lucknow': 'Uttar Pradesh', 'Ludhiana': 'Punjab', 'Madurai': 'Tamil Nadu', 'Mangalore': 'Karnataka', 'Mohali': 'Punjab', 'Mumbai': 'Maharashtra', 'Nagpur': 'Maharashtra', 'Nashik': 'Maharashtra', 'Navi Mumbai': 'Maharashtra', 'New Delhi': 'Delhi', 'Noida': 'Uttar Pradesh', 'Panipat': 'Haryana', 'Pondicherry': 'Puducherry', 'Rajkot': 'Gujarat', 'Secunderabad': 'Telangana', 'Surat': 'Gujarat', 'Thane': 'Maharashtra', 'Thiruvananthapuram': 'Kerala', 'Thrissur': 'Kerala', 'Vadodara': 'Gujarat', 'Vellore': 'Tamil Nadu', 'Vijayawada': 'Andhra Pradesh'}
path="D:/I2/Project2/F/" + product+"/"+product+"_"+str(categories[0])+".xlsx"
try:
    for category in categories:
        for city in cities:
            keyword_original = product+" "+category+" in "+city
            keyword_search = keyword_original.replace(' ', '+')
            driver.get("https://www.google.com/search?q=" + keyword_search + "&start=" + str(0))
            while (str(driver.title).split(" "))[-1] != "Search":
                print("0")
            try:
                driver.find_element(By.XPATH, "//div[@class = 'dbg0pd OSrXXb']").click()
                z = 1
            except:
                z = 0
            if z==1:
                while len(driver.find_elements(By.XPATH, "//div[@class = 'dbg0pd OSrXXb eDIkBe']")) ==0:
                    print("1")
                    pass
                brand = driver.find_elements(By.XPATH, "//div[@class = 'dbg0pd OSrXXb eDIkBe']")
                n = 0
                for ele in brand:
                    (driver.find_elements(By.XPATH, "//div[@class = 'dbg0pd OSrXXb eDIkBe']")[n]).click()
                    print((driver.find_elements(By.XPATH, "//div[@class = 'dbg0pd OSrXXb eDIkBe']")[n]).text)
                    truth = 0
                    now = datetime.now()
                    a_time = int(now.strftime("%S"))
                    while truth==0:
                        print("2")
                        try:
                            if (driver.find_element(By.XPATH, "//h2[@data-dtype = 'd3ifr']")).text == (driver.find_elements(By.XPATH, "//div[@class = 'dbg0pd OSrXXb eDIkBe']")[n]).text:
                                truth=1
                                list_name.append((driver.find_element(By.XPATH, "//h2[@data-dtype = 'd3ifr']")).text)
                            else:
                                pass
                        except:
                            pass
                        if truth==0:
                            no = datetime.now()
                            b_time = int(no.strftime("%S"))
                            if b_time<a_time:
                                b_time=b_time+60
                            if b_time-a_time>6:
                                truth=1
                                list_name.append((driver.find_elements(By.XPATH, "//div[@class = 'dbg0pd OSrXXb eDIkBe']")[n]).text)
                    list_keyword.append(keyword_original)
                    list_link.append(driver.current_url)
                    list_city.append(city)
                    list_state.append(dic[city])
                    print(dic[city])
                    try:
                        ad = driver.find_element(By.CSS_SELECTOR,'span.LrzXr')
                        list_address.append(ad.text)
                        try:
                            pin = re.findall('\d\d\d\d\d\d', ad.text)
                            list_pin.append(pin[0])
                        except:
                            list_pin.append(empty)
                    except:
                        if iyu ==0:
                            ad = "Main "+city +" , "+dic[city]
                            iyu = 1
                        elif iyu==1:
                            ad = city + " , INDIA"
                            iyu = 2
                        elif iyu == 2:
                            ad = dic[city] + " in "+city+" , India"
                            iyu = 0
                        list_address.append(ad)
                        list_pin.append(empty)
                    try:
                        list_phone.append(driver.find_element(By.XPATH,"//a[@data-dtype='d3ph']").text)
                    except:
                        list_phone.append(empty)
                    list_email.append(empty)
                    try:
                        if len(driver.find_elements(By.XPATH, "//a[@class ='ab_button CL9Uqc']"))>1:
                            list_site.append((driver.find_element(By.XPATH, "//a[@class ='ab_button CL9Uqc']")).get_attribute("href"))
                        else:
                            list_site.append(empty)
                    except:
                        list_site.append(empty)
                    try:
                        list_rating.append(driver.find_element(By.XPATH, "//span[@class='Aq14fc']").text)
                    except:
                        list_rating.append(empty)
                    try:
                        a=str(driver.find_element(By.XPATH,'//a[@data-sort_by="qualityScore"]').text)
                        list_rating_count.append(a[0])
                    except:
                        list_rating_count.append(empty)
                    try:
                        if len(driver.find_elements(By.CLASS_NAME, 'zPcHee')) > 0:
                            prods = driver.find_elements(By.CLASS_NAME, 'zPcHee')
                            try:
                                list_product1.append(prods[0].text)
                            except:
                                list_product1.append(empty)
                            try:
                                list_product2.append(prods[1].text)
                            except:
                                list_product2.append(empty)
                            try:
                                list_product3.append(prods[2].text)
                            except:
                                list_product3.append(empty)
                            try:
                                list_product4.append(prods[3].text)
                            except:
                               list_product4.append(empty)
                            try:
                                list_product5.append(prods[4].text)
                            except:
                                list_product5.append(empty)
                            try:
                                list_product6.append(prods[5].text)
                            except:
                                list_product6.append(empty)
                            try:
                                list_product7.append(prods[6].text)
                            except:
                                list_product7.append(empty)
                            try:
                                list_product8.append(prods[7].text)
                            except:
                                list_product8.append(empty)
                        else:
                            list_product1.append(empty)
                            list_product2.append(empty)
                            list_product3.append(empty)
                            list_product4.append(empty)
                            list_product5.append(empty)
                            list_product6.append(empty)
                            list_product7.append(empty)
                            list_product8.append(empty)
                    except:
                        list_product1.append(empty)
                        list_product2.append(empty)
                        list_product3.append(empty)
                        list_product4.append(empty)
                        list_product5.append(empty)
                        list_product6.append(empty)
                        list_product7.append(empty)
                        list_product8.append(empty)
                    n=n+1
except:
    load=1
    data['Search Keyword'] = list_keyword
    data['Storefront Link'] = list_link
    data['Company Name'] = list_name
    data['Address'] = list_address
    data['State'] = list_state
    data['City'] = list_city
    data['Pincode'] = list_pin
    data['Phone'] = list_phone
    data['Email Id'] = list_email
    data['Website'] = list_site
    data['Rating'] = list_rating
    data['Total Reviews']=list_rating_count
    data['Product 1'] = list_product1
    data['Product 2'] = list_product2
    data['Product 3'] = list_product3
    data['Product 4'] = list_product4
    data['Product 5'] = list_product5
    data['Product 6'] = list_product6
    data['Product 7'] = list_product7
    data['Product 8'] = list_product8
    data.to_excel(path)
if load==0:
    data['Search Keyword'] = list_keyword
    data['Storefront Link'] = list_link
    data['Company Name'] = list_name
    data['Address'] = list_address
    data['State'] = list_state
    data['City'] = list_city
    data['Pincode'] = list_pin
    data['Phone'] = list_phone
    data['Email Id'] = list_email
    data['Website'] = list_site
    data['Rating'] = list_rating
    data['Total Reviews']=list_rating_count
    data['Product 1'] = list_product1
    data['Product 2'] = list_product2
    data['Product 3'] = list_product3
    data['Product 4'] = list_product4
    data['Product 5'] = list_product5
    data['Product 6'] = list_product6
    data['Product 7'] = list_product7
    data['Product 8'] = list_product8
    data.to_excel(path)
