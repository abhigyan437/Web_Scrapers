from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def time_converter(time1):
    time1 = time1.replace(' ', '')
    time1 = time1.lower()
    time1 = time1.strip()
    if 'am' in time1:
        if ':' in time1:
            time1 = time1.replace('am', '')
            if time1[:2] == '12':
                if len((time1.split(':'))[-1]) == 1:
                    return '00:0' + time1[-1]
                else:
                    return '00:' + time1[-2:]
            else:
                if len((time1.split(':'))[0]) == 1:
                    part1 = '0' + (time1.split(':'))[0] + ':'
                else:
                    part1 = (time1.split(':'))[0] + ':'
                if len((time1.split(':'))[-1]) == 1:
                    part2 = '0' + str((time1.split(':'))[-1])
                else:
                    part2 = str((time1.split(':'))[-1])
                return part1 + part2
        else:
            time1 = time1.replace('am', '')
            if int(time1) == 12:
                part1 = 00
            else:
                part1 = int(time1)
            return str(part1) + ':00'
    elif 'pm' in time1:
        if ':' in time1:
            time1 = time1.replace('pm', '')
            if time1[:2] == '12':
                if len((time1.split(':'))[-1]) == 1:
                    return '12:0' + time1[-1]
                else:
                    return '12:' + time1[-2:]
            else:
                part1 = int((str(time1).split(':'))[0])
                part1 += 12
                part1 = str(part1)
                if len((time1.split(':'))[-1]) == 1:
                    part2 = '0' + str((time1.split(':'))[-1])
                else:
                    part2 = str((time1.split(':'))[-1])
                return part1 + ':' + part2
        else:
            time1 = time1.replace('pm', '')
            if int(time1) == 12:
                part1 = 12
            else:
                part1 = 12 + int(time1)
            return str(part1) + ':00'
    else:
        if len(str(time1))==4:
            return '0'+str(time1)
        else:
            return time1



driver = webdriver.Chrome(executable_path="C:/Users/abhig/OneDrive/Documents/Driverchromedriver.exe")
url = 'https://icllm2023.org/en/scientific-program'
driver.get(url)
input('ENTER')
li_date = []
li_start = []
li_end = []
li_loc = []
li_article = []
li_auth = []
li_aff = []
date_xpath = '//div[@class="scientific-date"]'
dates = driver.find_elements(By.XPATH,date_xpath)
dates = [x.text for x in dates]
dates = ['May 12, 2023' if '12' in x else 'May 13, 2023' for x in dates]
dates = dates[:3] + [dates[2]] + dates[3:5]+[dates[4]]+dates[5:]
time_xpath = '//div[@class="scientific-clock-2"]'
time1 = driver.find_elements(By.XPATH, time_xpath)
time1 = [x.text for x in time1]
time1 = time1[:3] + [time1[2]] + time1[3:5]+[time1[4]]+time1[5:]
li_start = [(x.split(' - '))[0] for x in time1]
li_end = [(x.split(' - '))[1] for x in time1]


session_xpath = '//div[@class="scientific-container-program"]/div'
sessions = driver.find_elements(By.XPATH,session_xpath)
loc_xpath = '//div[@class="scientific-container-program"]/div/div[1]'
loc = driver.find_elements(By.XPATH, loc_xpath)
loc = [x.text for x in loc]
session_titles_xpath = '//div[@class="scientific-container-program"]/div/h1'
session_titles = driver.find_elements(By.XPATH,session_titles_xpath)
li_session = [x.text for x in session_titles]
session_auth_aff_xpath = '//div[@class="scientific-container-program"]/div/div[2]'
session_auth_aff = driver.find_elements(By.XPATH,session_auth_aff_xpath)
session_auth_aff = [x.text for x in session_auth_aff]
li_session_auth = []
li_session_aff = []
for x in session_auth_aff:
    print('X - ',x)
    xx = x.split('\n')
    print('xx - ',xx)
    auth1 = ''
    aff1 = ''
    if len(xx)>0:
        auth_count = 1
        while True:
            try:
                xxx = xx[auth_count]
                print('XXX - ',xxx)
                y = xxx.split(',',1)
                print('yyyyyy - ',y)
                aff1 += '; ' + y[1]
                auth1 += '; ' + y[0]
                auth_count+=1
            except:
                break
        li_session_aff.append(aff1[2:])
        li_session_auth.append(auth1[2:])
    else:
        li_session_aff.append('')
        li_session_auth.append('')

data = pd.DataFrame()
data['date'] = dates
data['Start'] = li_start
data['End'] = li_end
data['Loc'] = loc
data['Session Title'] = li_session
data['Auth'] = li_session_auth
data['Aff'] = li_session_aff
data.to_excel('Site_1.xlsx',index = False)