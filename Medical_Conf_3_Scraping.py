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
str1 = """https://apacrs2023.org/s5-the-cataract-metaverse-1/
https://apacrs2023.org/s11-iiic-lectures-the-perfect-save/
https://apacrs2023.org/zeiss-surgical-video-symposium/
https://apacrs2023.org/alcon-surgical-video-symposium/
https://apacrs2023.org/johnson-johnson-vision-surgical-video-symposium/
https://apacrs2023.org/s1-angle-closure-surgery-new-insights/
https://apacrs2023.org/mc1-mastering-toric-iols/
https://apacrs2023.org/mc2-mastering-pterygium-surgery/
https://apacrs2023.org/mc3-mastering-paediatric-cataract-surgery/
https://apacrs2023.org/mc4-mastering-biometry/
https://apacrs2023.org/mc6-what-they-dont-teach-you-in-residency/
https://apacrs2023.org/mc5-mastering-refractive-surgery-complications/
https://apacrs2023.org/mc7-mastering-phaco-alternatives/
https://apacrs2023.org/mc8-mastering-corneal-endothelial-transplantation/
https://apacrs2023.org/mc9-mastering-phakic-iols/
https://apacrs2023.org/mc12-mastering-migs-complications/
https://apacrs2023.org/mc11-mastering-vitrectomy-for-anterior-segment-surgeons/
https://apacrs2023.org/mc10-mastering-iol-fixation/
https://apacrs2023.org/s2-updates-on-infectious-keratitis/
https://apacrs2023.org/s15-holistic-eye-care-a-multidisciplinary-approach-part-2/
https://apacrs2023.org/s14-faster-than-the-speed-of-light-changing-patterns-in-refractive-surgery/
https://apacrs2023.org/s13-glitch-in-the-matrix-challenging-cataract-cases/
https://apacrs2023.org/s7-holistic-eye-care-a-multidisciplinary-approach-part-1/
https://apacrs2023.org/s4-whats-new-in-cornea/
https://apacrs2023.org/s3-myopia-associated-optic-neuropathy-or-glaucoma/
https://apacrs2023.org/s17-anterior-segment-innovations/
https://apacrs2023.org/s9-the-new-black-in-presbyopia-correction/
https://apacrs2023.org/s8-the-network-is-down-managing-cataract-complications/
https://apacrs2023.org/s16-the-cataract-metaverse-2-everything-everywhere-all-at-once/
https://apacrs2023.org/zeiss-lunch-symposium/"""
urls =str1.split('\n')
li_main_session = []
li_main_date = []
li_main_article = []
li_main_start = []
li_main_end = []
li_main_loc = []
li_main_abs = []
li_main_auth = []
li_main_aff = []
li_main_url = []
print('URL COUNT - ',len(urls))
for url_count in range(25,len(urls)):#6
    print("URL = ",url_count)
    url = urls[url_count]
    print(url)
    driver.get(url)
    print('REACHED URL')
    li_session = []
    li_date = []
    li_article = []
    li_start = []
    li_end = []
    li_loc = []
    li_abs = []
    li_auth = []
    li_aff = []
    li_url = []
    date_xpath = '//div[@class="wt-date-text"]'
    date1 = (driver.find_element(By.XPATH, date_xpath)).text
    if '9' in str(date1):
        date1 = 'June 09, 2023'
    if '8' in str(date1):
        date1 = 'June 08, 2023'
    if '10' in str(date1):
        date1 = 'June 10, 2023'
    session_xpath = '//h1'
    session_title = (driver.find_element(By.XPATH,session_xpath))
    loc_xpath = '//div[@class="wt-venue-container"]'
    loc1 = (driver.find_element(By.XPATH,loc_xpath)).text
    text_xpath = '//div[@class="fusion-text fusion-text-1"]/p[1]'
    try:
        text = (driver.find_element(By.XPATH,text_xpath)).text
    except:
        text = (driver.find_element(By.XPATH,'//div[@class="fusion-text fusion-text-1"]')).text
    sess_auth_xpath = '//div[@class="fusion-text fusion-text-1"]/p[2]/a'
    sess_auth = driver.find_elements(By.XPATH,sess_auth_xpath)
    auth1 = ''
    aff1 = ''
    for x in sess_auth:
        y = (x.text).split(',',1)
        auth1+= '; ' + (str(y[0])).strip()
        try:
            aff1 += '; ' + (str(y[1])).strip()
        except:
            pass
    if auth1.strip() == '':
        auth_aff_xpath = '//span[@class="wt-mc-speakers-text"]'
        auth_aff = driver.find_elements(By.XPATH,auth_aff_xpath)
        for auth__ in auth_aff:
            auth100 = auth__.text
            auth101 = auth100.split('\n')
            auth1 += '; ' + auth101[0].strip()
            try:
                aff1 += '; ' + auth101[1].strip()
            except:
                pass
    time_xpath = '//div[@class="wt-time-text"]'
    time1 = (driver.find_element(By.XPATH,time_xpath)).text
    time1 = time1.split('–')
    end_time = str(time1[1])
    end_time  = end_time.replace('hrs','')
    li_article.append(session_title.text)
    li_start.append(time1[0])
    li_end.append(end_time)
    li_abs.append(text)
    li_auth.append(auth1[2:])
    li_aff.append(aff1[2:])

    time_xpath ='//tr/td[1]'
    times = driver.find_elements(By.XPATH,time_xpath)
    title_xpath ='//tr/td[2]'
    titles = driver.find_elements(By.XPATH,title_xpath)
    auth_aff_xpath ='//tr/td[3]'
    auth_aff = driver.find_elements(By.XPATH,auth_aff_xpath)
    for count in range(1,len(auth_aff)):
        time1 = times[count].text
        time2 = time1.split('-',1)
        if len(time2) == 1:
            time2 = time1.split('–',1)
        try:
            li_end.append(time2[1].replace('hrs',''))
            li_start.append(time2[0])
            title1 = titles[count].text
            li_article.append(title1)
            auth_aff_1 = auth_aff[count].text
            auth_aff_2 = auth_aff_1.split('\n')
            try:
                li_auth.append(auth_aff_2[0])
            except:
                li_auth.append('')
            try:
                li_aff.append(auth_aff_2[1])
            except:
                li_aff.append('')
        except:
            pass

    li_loc = [loc1 for x in li_article]
    li_date = [date1 for x in li_article]
    li_session = [session_title.text for x in li_article]
    li_abs += ['' for x in range(len(li_session)-1)]
    li_url = [driver.current_url for x in li_session]

    li_main_session += li_session
    li_main_date += li_date
    li_main_article +=li_article
    li_main_start +=li_start
    li_main_end +=li_end
    li_main_loc +=li_loc
    li_main_abs +=li_abs
    li_main_auth +=li_auth
    li_main_aff +=li_aff
    li_main_url +=li_url

data = pd.DataFrame()
data['Article'] = li_main_article
data['URL'] = li_main_url
data['Auth'] = li_main_auth
data['Aff'] = li_main_aff
data['Text'] = li_main_abs
data['Start'] = li_main_start
data['End'] = li_main_end
data['date'] = li_main_date
data['Loc'] = li_main_loc
data['Session'] = li_main_session
data.to_excel('Program_12.xlsx',index = False)

