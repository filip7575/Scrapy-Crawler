# coding=utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import string
from fake_useragent import UserAgent
from datetime import datetime

#Random useragent, modify profile firefox
useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.random)

driver = webdriver.Firefox(firefox_profile=profile, executable_path="/home/selenium/drivers/geckodriver")
driver.set_window_size(800,600)
driver.get("https://dev.to/search?q=Selenium")
driver.get('https://chollometro.com')

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#using the JavaScriptExecutor to scroll down to bottom of window
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
 
time.sleep(3)

#we get the internal html code of the body        
body = driver.execute_script("return document.body")
source = body.get_attribute('innerHTML')

#print(source)

soup = BeautifulSoup(source, "html.parser")

result = soup.find_all('a', {'class' :'cept-tt thread-link linkPlain thread-title--card'})

print("=== Articule =====")
for txt in result:
    print(txt.text)


result = soup.find_all('span', {'class' :'thread-price text--b vAlign--all-tt cept-tp size--all-l'})
#result = soup.find_all("span")

print("=== price =====")

for txt in result:
    if txt.text == "":
       print("vacio")
    #print(txt.text)


result = soup.find_all('div', {'class' :'gridLayout-item threadCardLayout--card'})
for bl in result:
    name = bl.find('a', {'class' :'cept-tt thread-link linkPlain thread-title--card'})
    #name1 = name.get('title')
    price = bl.find('span', {'class' :'thread-price text--b vAlign--all-tt cept-tp size--all-l'})
    print("=====")
    if not name:  
       #print("Sin Nombre")
       name = ""
    else:
       print(name.text)
       article = name.text
    if not price:
       price = "Empty"
       #print("Sin Precio")
    else:
       #print(price.text)
       price = price.text

    createt = datetime.now().isoformat();
    python_dict = {
              "Plaform" : "chollometro",
              "articulo" : name.text,
              "precio" : price,
              "dcreate" : createt                
        }

    print(python_dict)
driver.close()
