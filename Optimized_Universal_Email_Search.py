import re
import numpy as np
from numpy.core.defchararray import lower
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

pattern = "\w+@\w+.\w+"
product="Delrin Sheet"
empty=" "
category="b"
cate="a"
path="D:/I2/Project2/F/" + product+"/"+product+"_"+str(category)+".xlsx"
path_new="D:/I2/Project2/F/" + product+"/"+product+"_Email_"+str(category)+".xlsx"
got_path="D:/I2/Project2/F/" + product+"/"+product+"_Email_"+str(cate)+".xlsx"
got=pd.read_excel(got_path)
list_pre_site=list(got['Website'])
list_pre_email=got['Email']
m=0
dic1={}
while m<len(list_pre_site):
    list_pre_site[m]=str(list_pre_site[m])
    dic1[str(list_pre_site[m])]=str(list_pre_email[m])
    m=m+1
data=pd.read_excel(path)
list_website=data['Website']
list_company=[]
list_site=[]
list_email=[]
data_created=0
driver=webdriver.Chrome(executable_path="C:/Drivers/chromedriver.exe")
n=0
try:
    for ele in list_website:
        print(n+1)
        if len(str(ele))>5:
            if 'indiamart' in str(ele) or 'business.site' in str(ele) or 'business.google' in str(ele):
                print("Exceptional")
                list_email.append(empty)
                print("ADDING NAN")
            elif str(ele) in list_pre_site:
                print("ALREADY")
                list_email.append(dic1[ele])
            else:
                print(ele)
                email_found=0
                contact_us_found=0
                site_infound=0
                try:
                    driver.get(ele)
                except:
                    site_infound=1
                if site_infound==0:
                    try:
                        body_text=driver.find_element(By.TAG_NAME,'body').text
                        z = re.search(pattern, body_text)
                        if z:
                            print("EMAIL FOUND at home page")
                            email_found=1
                            list_email.append(z.group(0))
                            dic1[str(ele)]=str(z.group(0))
                        else:
                            print("EMAIL NOT FOUND at home page")
                        if email_found==0:
                            qwe=driver.find_elements(By.TAG_NAME,'a')
                            for we in qwe:
                                if lower(str(we.text))=="contact us":
                                    contact_us_found=1
                                    print("CONTACT US")
                                    driver.get(we.get_attribute('href'))
                                    try:
                                        body_text = driver.find_element(By.TAG_NAME, 'body').text
                                        z = re.search(pattern, body_text)
                                        if z:
                                            print("EMAIL FOUND at CONTACT page")
                                            email_found=1
                                            list_email.append(z.group(0))
                                            dic1[str(ele)]=str(z.group(0))
                                        else:
                                            print("EMAIL NOT FOUND at CONTACT page")
                                        break
                                    except:
                                        break
                            if contact_us_found==0:
                                print("NO CONTACT US")
                            if email_found==0:
                                list_email.append(empty)
                                dic1[str(ele)] = empty
                    except:
                        list_email.append(empty)
                        print("ADDING NAN")
                        dic1[str(ele)] = empty
                else:
                    list_email.append(empty)
                    dic1[str(ele)] = empty
                    print("SITE INVALID")
        else:
            print("NO WEBSITE")
            list_email.append(empty)
            print("ADDING NAN")
            dic1[str(ele)] = empty
        list_company.append(data['Company Name'][n])
        list_pre_site.append(str(ele))
        list_site.append(ele)
        n=n+1
except:
    print("Error")
    data_created=1
    new = pd.DataFrame()
    new['Company'] = list_company
    new['Website'] = list_site
    new['Email'] = list_email
    new.to_excel(path_new)
if data_created==0:
    new=pd.DataFrame()
    new['Company']=list_company
    new['Website']=list_site
    new['Email']=list_email
    new.to_excel(path_new)
