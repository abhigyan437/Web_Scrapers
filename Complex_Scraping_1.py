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
data = pd.read_excel('1.xlsx')
list_title = data['Title'] 
list_url = data['url']
list_type = data['type']
list_cate = data['cate']
list_sub = data['sub']
list_date = data['date']
list_start = data['start']
list_end = data['end']

li_id = []
li_article = []
li_url = []
li_auth = []
li_aff = []
li_text = []
li_date = []
li_start = []
li_end = []
li_loc = []
li_session = []
li_type = []
li_cate = []
li_sub = []
the_int = 6
for url_count in range(100,len(list_url)):#
    print('COUNT  - ',url_count)
    url1 = list_url[url_count]
    print(url1)
    session_title = list_title[url_count]
    session_type = list_type[url_count]
    category = list_cate[url_count]
    subcate = list_sub[url_count]
    date1 = list_date[url_count]
    driver.get(url1)
    sleep(15)
    loc1 = (driver.find_element(By.XPATH,'//span[@class="location"]')).text
    try:
        sess_text = (driver.find_element(By.XPATH,'//li[@class="startTime"]')).text
    except:
        sess_text = ''
    li_id.append('')
    li_article.append(session_title)
    li_url.append(url1)
    li_auth.append('')
    li_aff.append('')
    li_text.append(sess_text)
    li_date.append(date1)
    li_start.append(list_start[url_count])
    li_end.append(list_end[url_count])
    li_loc.append(loc1)
    li_session.append(session_title)
    li_type.append(session_type)
    li_cate.append(category)
    li_sub.append(subcate)

    id_xpath = '//span[@class="presentation-number"]'
    li_id += [x.text for x in driver.find_elements(By.XPATH,id_xpath)]
    article_xpath = '//h3/span[2]'
    li_article += [x.text for x in driver.find_elements(By.XPATH,article_xpath)]
    auth_aff_xpath = '//span[@class="displayName"]'
    auth_aff = driver.find_elements(By.XPATH,auth_aff_xpath)
    auth_aff= [x.text for x in auth_aff]
    auth_xpath = '//span[@class="displayName"]/b'
    auths = driver.find_elements(By.XPATH,auth_xpath)
    auths = [x.text for x in auths]
    time_xpath = '//span[@class="localization"]'
    times = driver.find_elements(By.XPATH,time_xpath)
    times = [x.text for x in times]
    url_xpath = '//a[@class="action__link"]'
    li_url += [x.get_attribute('href') for x in driver.find_elements(By.XPATH,url_xpath)]
    for auth_count in range(len(auth_aff)):
        li_loc.append(loc1)
        li_session.append(session_title)
        li_type.append(session_type)
        li_cate.append(category)
        li_sub.append(subcate)
        li_date.append(date1)
        try:
            print('tt - ',times[auth_count])
            y = str(times[auth_count]).split('-')
            print('yyyyyyyy  - ',y)
            if len(y) == 2:
                try:
                    li_start.append(time_converter(y[0]))
                except:
                    li_start.append(list_start[url_count])
                try:
                    li_end.append(time_converter(y[1]))
                except:
                    li_end.append(list_end[url_count])
            else:
                y = str(times[auth_count]).split('-')
                try:
                    li_start.append(time_converter(y[0]))
                except:
                    li_start.append(list_start[url_count])
                try:
                    li_end.append(time_converter(y[1]))
                except:
                    li_end.append(list_end[url_count])
        except:
            li_start.append(list_start[url_count])
            li_end.append(list_end[url_count])
        try:
            auth1 = (auths[auth_count]).strip()
        except:
            auth1 = ''
        li_auth.append(auth1)
        auth_aff_ent = auth_aff[auth_count]
        aff = auth_aff_ent.replace(auth1,'')
        aff = aff.strip()
        try:
            aff = aff[2:]
            if aff[:2] == ', ':
                aff = aff[2:]
            li_aff.append(aff)
        except:
            li_aff.append('')
        li_text.append('')



data = pd.DataFrame()
data['ID'] = li_id
data['Article'] = li_article
data['url'] = li_url
data['auth'] = li_auth
data['aff'] = li_aff
data['text'] = li_text
data['date'] = li_date
data['start'] = li_start
data['end'] = li_end
data['loc'] = li_loc
data['session'] = li_session
data['type'] = li_type
data['cate'] = li_cate
data['sub'] = li_sub
file_name = '2_' + str(the_int) + '.xlsx'
data.to_excel(file_name,index=False)