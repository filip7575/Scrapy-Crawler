from bs4 import BeautifulSoup
import datetime
from datetime import date, timedelta
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TWQueryMngr:
    # init method or constructor
    def __init__(self):
        self.search_url = "https://twitter.com/search?q="
        self.dates      = []

        self.driver         = webdriver.Chrome()
        self.search_words   = []
        self.lang           = 'es'
        self.output         = None

    def set_driver(self,_driver):
        self.driver = _driver

    def set_lang(self,_lang):
        self.lang = _lang

    def scroll(self,words, lang, max_time=180):

        languages = {1: 'en', 2: 'it', 3: 'es', 4: 'fr', 5: 'de', 6: 'ru', 7: 'zh'}
        url = self.search_url
        for w in words[:-1]:
            url += "{}%20OR".format(w)
        url += "{}%20".format(words[-1])
        url += "&src=typed_query&f=live"
        if lang != 0:
            url += "l={}&".format(languages[lang])
        print(url)
        live = "css-4rbku5 css-18t94o4 css-1dbjc4n r-1awozwy r-18p3no4 r-rull8r r-wgabs5 r-1loqt21 r-6koalj r-eqz5dr r-16y2uox r-1777fci r-1ny4l3l r-1oqcu8e r-o7ynqc r-6416eg"

        self.driver.get(url)
        start_time = time.time()  # remember when we started

        time.sleep(5)
        element =self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div[2]/div[2]/a/div/span").click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)


    def scrape_tweets(self):
        
        sql = ""

        try:

            obj = BeautifulSoup(self.driver.page_source, "html.parser")

            
            for a in obj.find_all("article"):

                    tw_text = a.find("div", {"lang": "es"})

                    if tw_text != None:

                        tw_obj      = BeautifulSoup(str(tw_text), "html.parser")
                        tw_user     = a.find("a", {"role": "link"})['href'].strip("/")
                        tw_datetime = a.find("time")['datetime']


                        sql = "('%s', '%s', '%s')"%(tw_obj.text,tw_user,tw_datetime)
                        print("====================================")
                        print(sql)

        except Exception as e:
            print("Something went wrong!")
            print(e)
     
        print(sql)


    def tw_search(self,_search_str):

        wordsToSearch = []
        wordsToSearch.append(_search_str)
        self.output = open("output.json","w")

        self.driver = webdriver.Chrome()
        self.scroll(wordsToSearch, 1)
        self.scrape_tweets()
        time.sleep(3)
        #print("The tweets for {} are ready!".format(all_dates[i]))
        self.driver.quit()

        self.output.close()
