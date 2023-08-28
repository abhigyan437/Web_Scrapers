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
url = 'https://program.eventact.com/Agenda/Program?Event=35472&agenda=14169&lang=en'
driver.get(url)
input('click')
li_session = []
li_start = []
li_end = []
li_date = []#######################
li_article = []
li_loc = []
li_auth = []
li_aff= []
dates = ['August 29, 2023','August 30, 2023','August 31, 2023','September 01, 2023']
tab_xpath = '//ul[@class="col-12 pv-days"]/li/a'
tabs = driver.find_elements(By.XPATH,tab_xpath)
for tab_count in range(len(tabs)):
    date1 = dates[tab_count]
    tabs = driver.find_elements(By.XPATH, tab_xpath)
    driver.execute_script("arguments[0].click();", tabs[tab_count])
    sleep(3)
    session_xpath = '//div[@class="session-wrapper ng-scope"]'
    click_xpath = '//a[@title="Click to expand"]'
    clicks = driver.find_elements(By.XPATH,click_xpath)
    loc_xpath = '//p[@class="pv-session-hall ng-scope"]'
    sessions = driver.find_elements(By.XPATH,session_xpath)
    print('SSSSSSSSS  - ',len(sessions))
    sessions_text = [x.text for x in sessions]
    session_time = [(x.split('\n'))[0] for x in sessions_text]
    session_titles = [(x.split('\n'))[1] for x in sessions_text]
    for sess_count in range(len(sessions)):
        print('SESSION COUNT - ',sess_count)
        sessions = driver.find_elements(By.XPATH, session_xpath)
        sess = sessions[sess_count]
        click_xpath = '//a[@title="Click to expand"]'
        clicks = driver.find_elements(By.XPATH, click_xpath)
        driver.execute_script("arguments[0].click();", clicks[sess_count])
        sleep(1)
        article_xpath = '//div[@class="pv-lecture ng-scope"]'
        sessions = driver.find_elements(By.XPATH, session_xpath)
        sess = sessions[sess_count]
        session_title = session_titles[sess_count]
        li_session.append(session_title)
        li_date.append(date1)
        this_time = session_time[sess_count].split(' - ',1)
        session_start = this_time[0]
        session_end = this_time[1]
        li_start.append(session_start)
        li_end.append(session_end)
        li_article.append(session_title)
        try:
            loc = (driver.find_element(By.XPATH,loc_xpath)).text
        except:
            loc = ''
        li_loc.append(loc)
        li_auth.append('')
        li_aff.append('')
     #   driver.execute_script("arguments[0].click();", sess)
        article_times = [x.text for x in driver.find_elements(By.XPATH,'//div[@class="pv-lecture ng-scope"]/div[@ng-if="lecture.timeDisplay"]')]
        print("ARTICLE TIMES - ",len(article_times))
        li_start += [(x.split(' - ',1))[0] for x in article_times]
        li_end += [(x.split(' - ',1))[1] for x in article_times]
        li_session += [session_title for x in article_times]
        li_loc += [loc for x in article_times]
        li_date += [date1 for x in article_times]
        li_article += [x.text for x in driver.find_elements(By.XPATH,'//div[@class="lecture-title ng-scope"]')]
        auth_xpath = '//div[@class="pv-speakers ng-scope"]/div[1]/div/div/div[1]'
        aff_xpath = '//div[@class="pv-speakers ng-scope"]/div[1]/div/div/div[2]'
        li_auth += [x.text for x in driver.find_elements(By.XPATH,auth_xpath)]
        li_aff += [x.text for x in driver.find_elements(By.XPATH,aff_xpath)]

        click_xpath = '//a[@title="Click to expand"]'
        clicks = driver.find_elements(By.XPATH, click_xpath)
        driver.execute_script("arguments[0].click();", clicks[sess_count])
        sleep(1)

data = pd.DataFrame()

data['Article'] = li_article
data['Auth'] = li_auth
data['aff'] = li_aff
data['date'] = li_date
data['start'] = li_start
data['end']  = li_end
data['loc'] = li_loc
data['session'] = li_session

data.to_excel('2.xlsx',index=False)