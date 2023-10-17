from selenium import webdriver 
 from bs4 import BeautifulSoup 
 from time import sleep 
 import time 
  
 detail={'name':[],"profile_url":[]} 
 driver=webdriver.Chrome() 
 driver.get("https://www.linkedin.com/login") 
 time.sleep(3) 
 user_name=driver.find_element('xpath','//*[@id="username"]') 
 user_name.send_keys("e-mail") 
 time.sleep(2) 
 pword = driver.find_element("xpath",'//*[@id="password"]')  
 pword.send_keys("password") 
 time.sleep(2) 
 driver.find_element('xpath','//*[@id="organic-div"]/form/div[3]/button').click() 
 time.sleep(2)  
 informations="https://www.linkedin.com/mynetwork/invite-connect/connections" 
 driver.get(informations) 
 time.sleep(2) 
 connections=driver.page_source  
 soup=BeautifulSoup(connections,'html.parser') 
 act=soup.find_all('li',class_="mn-connection-card artdeco-list") 
 for ac in act: 
     profile=ac.find('a',class_='ember-view mn-connection-card__picture').get('href') 
     link = 'https://www.linkedin.com/'+profile 
     detail['profile_url'].append(link) 
     name = ac.find('span', class_="mn-connection-card__name t-16 t-black t-bold").text 
     detail['name'].append(name) 
     sleep(1) 
     info = link + "overlay/contact-info/" 
     driver.get(info) 
     sleep(1) 
 print(detail)
