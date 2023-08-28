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
data_url = pd.read_excel('URLs.xlsx')

list_url = list(data_url['url'])
list_date = list(data_url['date'])
list_type = list(data_url['session type'])
list_start = list(data_url['start'])
list_end = list(data_url['end'])
list_title = list(data_url['title'])
li_session = []
li_session_type = []
li_loc = []
li_date = []
li_start = []
li_end = []
li_article = []
li_auth = []
li_aff = []
li_url = []
li_text = []
li_id = []
for url_count in range(len(list_url)):#Begin from 15
    print("REACHED - ",url_count)
    url1= list_url[url_count]
    print(url1)
    driver.get(url1)
    sleep(3)
    date1 = list_date[url_count]
    type1 = list_type[url_count]
    session_start = list_start[url_count]
    session_end = list_end[url_count]
    session_title = list_title[url_count]
    loc_xpath = '//div[@class="col"]/span'
    locs = driver.find_elements(By.XPATH, loc_xpath)
    try:
        loc1 = locs[2].text
        if len(loc1.split(' '))>4:
            loc1 = ''
    except:
        loc1 = ''
    auth_aff_xpath = '//ul[@class="list-unstyled mb-0"]/li'
    auth_aff = driver.find_elements(By.XPATH,auth_aff_xpath)
    auth_aff = [x.text for x in auth_aff]
    auth_aff = [x.replace('Moderator: ','') for x in auth_aff]
    auth1 = ""
    aff1 = ''
    for x in auth_aff:
        y = x.split('(',1)
        auth1 += '; ' + (str(y[0])).strip()
        try:
            aff1 += '; ' +((str(y[1])).replace(')','')).strip()
        except:
            pass
    text1 = ''
    text_xpath = '//div[@class="row pt-2"]/div[@class ="col"]'
    text1 = driver.find_elements(By.XPATH,text_xpath)
    text1 = text1[1].text
    if text1.strip()==session_title.strip():
        type1 += '; ' + str(text1).strip()
        text1=''
    else:
        text1 = 'Sponsored by ' + str(text1 )
    li_session.append(session_title)
    li_session_type.append(type1)
    li_loc.append(loc1)
    li_date.append(date1)
    li_start.append(session_start)
    li_end.append(session_end)
    li_article.append(session_title)
    li_auth.append(auth1[2:])
    li_aff.append(aff1[2:])
    li_url.append(url1)
    li_text.append(text1)
    li_id.append('')

    article_auth = []
    article_aff = []
    article_title_xpath = '//div[@class="presentation pt-2"]/div/div/a'
    article_title = driver.find_elements(By.XPATH,article_title_xpath)
    list_articles = [x.text for x in article_title]
    list_articles_new = []
    article_ids = []
    for art100 in list_articles:
        art101 = art100.split(' ',1)
        if '-' in str(art101[0]):
            article_ids.append(str(art101[0]))
            list_articles_new.append(art101[1])
        else:
            article_ids.append('')
            list_articles_new.append(art100)
    list_articles = list_articles_new
    article_url = [x.get_attribute('href') for x in article_title]
    time_xpath = '//div[@class="col time text-right"]'
    times = driver.find_elements(By.XPATH,time_xpath)
    times = [x.text for x in times]
    times = [(x.split('\n',1))[0] for x in times]
    article_start = [(x.split('–'))[0] for x in times]
    article_end = [(x.split('–'))[1] for x in times]
    auth_aff_xpath = '//div[@class="presentation pt-2"]/div'
    auth_aff = driver.find_elements(By.XPATH,auth_aff_xpath)
    auth_aff = [x.text for x in auth_aff]
    for x in auth_aff:
        try:
            z = ((x.split('\n')))[1]
            if '(' in z:
                y = (z.split(':',1))[1]
                auth0 = (y.split('('))[0]
                article_auth.append(auth0)
                try:
                    aff0 = (y.split('(',1))[1]
                    aff0 = aff0.replace(')','')
                    article_aff.append(aff0)
                except:
                    article_aff.append('')
            else:
                article_auth.append('')
                article_aff.append('')
        except:
            article_aff.append('')
            article_auth.append('')
    article_title_xpath2 = '//div[@class="presentation pt-2 pb-2"]/div/div/a'
    article_title = driver.find_elements(By.XPATH, article_title_xpath2)
    if len(article_title) > 0:
        article_url += [x.get_attribute('href') for x in article_title]
        article_title = [x.text for x in article_title]
        for x in article_title:
            y = x.split(' ', 1)
            if len(y) > 1 and '-' in str(x):
                article_ids.append(y[0])
                list_articles.append(y[1])
            else:
                article_ids.append('')
                list_articles.append(x)

    article_title_xpath2 = '//div[@class="presentation pt-2 pb-2"]'
    article_title = driver.find_elements(By.XPATH, article_title_xpath2)
    if len(article_title) > 0:
        article_title = [x.text for x in article_title]
        for x in article_title:
            xx = x.split('\n')
            if len(xx) > 1:
                z == xx[1]
                if '(' in z:
                    y = (z.split(':', 1))[1]
                    auth0 = (y.split('('))[0]
                    article_auth.append(auth0)
                    try:
                        aff0 = (y.split('(', 1))[1]
                        aff0 = aff0.replace(')', '')
                        article_aff.append(aff0)
                    except:
                        article_aff.append('')
                else:
                    article_auth.append('')
                    article_aff.append('')
            elif 'Discussion' in str(x):
                article_auth.append('')
                article_aff.append('')

    article_session = [session_title for x in article_url]
    article_types = [type1 for x in article_url]
    article_date = [date1 for x in article_url]
    article_loc = [loc1 for x in article_url]
    article_text = ['' for x in article_url]

    li_session+= article_session
    li_session_type+= article_types
    li_loc+= article_loc
    li_date+= article_date
    li_start+= article_start
    li_end+= article_end
    li_article+= list_articles
    li_auth+= article_auth
    li_aff+= article_aff
    li_url+= article_url
    li_text+= article_text
    li_id+= article_ids

print('l - ',len(li_auth))
print(li_auth)
data = pd.DataFrame()
data['ID'] = li_id
data['article'] = li_article
data['url'] = li_url
data['auth'] = li_auth
data['aff'] = li_aff
data['Text'] = li_text
data['date'] = li_date
data['start'] = li_start
data['end'] = li_end
data['loc'] = li_loc
data['session'] = li_session
data['type'] = li_session_type
data.to_excel('excel_102.xlsx',index = False)
