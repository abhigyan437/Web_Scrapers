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
url = 'https://tfigroup.eventsair.com/bsg-live-2023'
driver.get(url)
sleep(2)
ele1 = driver.find_elements(By.XPATH, '//div[@class="link"]')
li_session = []
li_article = []
li_date = []
li_start = []
li_end = []
li_auth = []
li_aff = []
li_loc = []
a = 0
print('len  - ',len(ele1))
for count in range(len(ele1)):
    print('REached - ',count)
    driver.execute_script("arguments[0].click();", ele1[count])
    sleep(1)
    session_xpath = '//div[@id="GenericModalHeaderContent"]'
    session_title= (driver.find_element(By.XPATH,session_xpath)).text
    session_title = (session_title.split('\n',1))[0]
    if session_title not in li_session:
        print('accepted - ',session_title)
        a+=1
        date_xpath = '//div[@class="agenda-details-section1"]/div[1]'
        date1 = (driver.find_element(By.XPATH,date_xpath)).text
        date1 = ((date1.split(',',1))[-1]).strip()
        session_time_xpath = '//div[@class="agenda-details-section1"]/div[2]'
        session_times = (driver.find_element(By.XPATH,session_time_xpath)).text
        session_times_1 = session_times.split('-')
        session_end = time_converter(session_times_1[1])
        session_start = time_converter(session_times_1[0])
        loc_xpath = '//div[@class="agenda-details-section1"]/div[3]'
        try:
            loc1 = (driver.find_element(By.XPATH,loc_xpath)).text
        except:
            loc1 = ''
        li_session.append(session_title)
        li_article.append(session_title)
        li_date.append(date1)
        li_start.append(session_start)
        li_end.append(session_end)
        li_loc.append(loc1)
        row_xpath = '//div[@class="row"]/div[2]'
        auth_aff_xpath = '//div[@class="col-sm-3"]'
        auth_aff = driver.find_elements(By.XPATH,auth_aff_xpath)
        auth_aff = [x.text for x in auth_aff]
        auths = [(x.split('\n',1))[0] for x in auth_aff]
        affs = []
        for x in auth_aff:
            y = x.split('\n',1)
            try:
                affs.append(y[1])
            except:
                affs.append('')
        rows = driver.find_elements(By.XPATH,row_xpath)
        rows = [x.text for x in rows]
        try:
            auth1 = str(auths[0])
            aff1 = str(affs[0])
        except:
            auth1 = ''
            aff1 = ''
        article_auth = []
        article_aff = []
        actual_row_count = 1
        for row_count in range(1,len(rows)):
            x = rows[row_count]
            if x.strip()!='':
                x = x.split('\n',1)
                if x[0].strip()=='Chair' or x[0].strip()=='Session lead':
                    auth1 += '; ' + auths[actual_row_count]
                    if affs[actual_row_count].strip() != '':
                        aff1 += '; ' + affs[actual_row_count]
                else:
                    article_auth.append(auths[actual_row_count])
                    article_aff.append(affs[actual_row_count])
                    li_session.append(session_title)
                    li_article.append(x[0])
                    li_date.append(date1)
                    li_loc.append(loc1)
                    try:
                        article_time = x[1]
                        article_time = article_time.split('-',1)
                        li_end.append(time_converter(article_time[1]))
                        li_start.append(time_converter(article_time[0]))
                    except:
                        li_start.append(session_start)
                        li_end.append(session_end)
                actual_row_count+=1

        li_auth.append(auth1)
        li_aff.append(aff1)
        li_auth += article_auth
        li_aff += article_aff

data = pd.DataFrame()
data['Session'] = li_session
data['Article'] = li_article
data['date'] = li_date
data['Start'] = li_start
data['End'] = li_end
data['auth'] = li_auth
data['aff'] = li_aff
data['loc'] = li_loc
data.to_excel('SIte_10.xlsx',index=False)
print('A FInal valeu - ',a)