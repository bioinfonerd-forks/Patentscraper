from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  
from bs4 import BeautifulSoup as bs
import os
import webbrowser
import re


class Scrape():

    def __init__(self, patnum):
        self.patnum = patnum

        
        chrome_options = Options()  
        chrome_options.add_argument("--headless")        
        driver = webdriver.Chrome(executable_path='C:\\Users\\clay.chiang\\AppData\\Local\\Google\\Chrome SxS\\Application\\chromedriver', options=chrome_options)


        driver.get("https://patents.google.com/patent/"+self.patnum)
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#text')))
        self.html = driver.page_source
        driver.quit()



class Get():
    def __init__(self, html):
        self.html = html
        self.soup = bs(self.html,features='html.parser')  

    @classmethod
    def get_html(cls, patnum):
        cls.patnum = patnum
        html = Scrape(cls.patnum).html
        return cls(html)
        

           



class Parse():
    
    def __init__(self):
        self.text = ''

    def abstract(self):
        self.parse('.abstract')

    def claim(self):
        self.parse('.claims > .claim')
        

    def get(self, patnum):
        self.patnum = patnum
        self.soup = Get.get_html(self.patnum).soup
        return self.soup
    
    def parse(self,selector):
        self.selector = selector
        soup = self.soup
        html = soup.select(self.selector)
        text = ''
        for i in html:
            text += i.get_text()
        self.text += (text + '\n')      

    def __str__(self):
        return self.text


        

















