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
data = pd.read_excel('URLs.xlsx')
list_title = list(data['Title'])
list_url = list(data['URL'])
list_date = list(data['date'])
list_start = list(data['Start'])
list_end = list(data['End'])
list_loc = list(data['LOC'])
li_session = []
li_article = []
li_url = []
li_date = []
li_start = []
li_end = []
li_loc = []
li_auth = []
li_aff = []
li_type = []
li_cate = []
file_var = 9
driver.get('https://cm.eusem.org/cmPortal/Searchable/EXA/config/normal/redirectconfig/normal/redirectconference/EUSEM23#!sessiondetails/0000014560_0')
input('CLIKC')
for url_count in range(140,len(list_url)):
    print('COUNT - ',url_count)
    url1 = list_url[url_count]
    driver.get(url1)
    sleep(10)
    print(url1)
    for scroll_count in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
    date1 = list_date[url_count]
    session_start = list_start[url_count]
    session_end = list_end[url_count]
    loc1 = list_loc[url_count]
    id_title_type_xpath = '//span[@style="padding:0px 5px;"]'
    id_title_type = driver.find_elements(By.XPATH,id_title_type_xpath)
    id1 = id_title_type[0].text
    title = id_title_type[1].text
    session_title = str(id1) + ': ' + str(title)
    type1 = id_title_type[2].text
    try:
        cate1 = id_title_type[3].text
        if type1 in cate1:
            cate1 = ''
    except:
        cate1= ''
    li_auth.append('')
    li_aff.append('')
    li_session.append(session_title)
    li_article.append(session_title)
    li_url.append(url1)
    li_date.append(date1)
    li_start.append(session_start)
    li_end.append(session_end)
    li_loc.append(loc1)
    li_type.append(type1)
    li_cate.append(cate1)
    article_xpath = '//span[@style="font-style:italic"]'
    articles = driver.find_elements(By.XPATH, article_xpath)
    li_article += [x.text for x in articles]
    article_time_xpath = '//div[@style="padding-top:5px;display:"]'
    article_times = driver.find_elements(By.XPATH,article_time_xpath)
    article_times = [x.text for x in article_times]
    li_start += [((x.strip()).split('-'))[0] for x in article_times]
    li_end+= [((x.strip()).split('-'))[1] for x in article_times]
    if len([((x.strip()).split('-'))[0] for x in article_times])<len([x.text for x in articles]):
        diff1= len([x.text for x in articles]) - len([((x.strip()).split('-'))[0] for x in article_times])
        for time_count in range(diff1):
            li_start.append(session_start)
            li_end.append(session_end)
    article_auth_aff_xpath = '//div[@class="media-body"]/div[2]'
    article_auth_aff = driver.find_elements(By.XPATH,article_auth_aff_xpath)
    article_auth_aff = [x.text for x in article_auth_aff]
    auth_count= 0
    for x in article_auth_aff:
        if 'Speaker:' in x:
            y = (x.strip()).replace('Speaker:','')
            z = y.split(',',1)
            auth1 = z[0]
            li_auth.append(auth1)
            try:
                aff1 = z[1]
                li_aff.append(aff1)
            except:
                li_aff.append('')
            auth_count+=1
            li_session.append(session_title)
            li_url.append(url1)
            li_date.append(date1)
            li_loc.append(loc1)
            li_type.append(type1)
            li_cate.append(cate1)

    if auth_count<len([x.text for x in articles]):
        print('LESS AUTHS')
        print(session_title)
        print(url1)
        diff1 = len([x.text for x in articles])-auth_count
        for x in range(diff1):
            li_auth.append('')
            li_aff.append('')
            li_session.append(session_title)
            li_url.append(url1)
            li_date.append(date1)
            li_loc.append(loc1)
            li_type.append(type1)
            li_cate.append(cate1)

data = pd.DataFrame()
data['article_title'] = li_article
data['url'] = li_url
data['authors'] = li_auth
data['author_affiliation'] = li_aff
data['date'] = li_date
data['start_time'] = li_start
data['end_time'] = li_end
data['location'] = li_loc
data['session_title'] = li_session
data['session_type'] = li_type
data['category'] = li_cate
file_name = 'SITE_'+str(file_var) + '.xlsx'
data.to_excel(file_name,index=False)
