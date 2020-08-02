# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from difflib import *
import time
#set config
dr=webdriver.Chrome()


def rebot_login():
    dr.get("https://kktix.com/users/sign_in?back_to=https%3A%2F%2Fkktix.com%2F")
    element_text1 = dr.find_element_by_id('user_login')
    element_text1.send_keys('u0424048')
    element_text2 = dr.find_element_by_id('user_password')
    element_text2.send_keys('xxx')
    dr.find_element_by_xpath('//input[@name="commit"]').click()

def myfunc():
    bs4=BeautifulSoup(dr.page_source,'html.parser')
    for name in bs4.findAll('span',class_='ticket-quantity ng-binding ng-scope'):
        if name.getText().find(u'尚未開賣')>0:
            dr.refresh()
        else:
            return True

def getTicket():
    dr.get("https://kktix.com/events/kmahk20190312cec/registrations/new")
    time.sleep(5)
    while True:
        a = myfunc()
        if a==True:
            break
    print('a')
    try:
        ## Change Quantity
        myElem = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ticket_160974"]/div/span[4]/input')))
        ## I agree
    except TimeoutException:
        print ("Loading took too much time!")
        

    
    a = dr.find_element_by_xpath("//*[@id=\"ticket_160974\"]/div/span[4]/input")
    a.clear()
    a.send_keys('1')
    ## I agree
    dr.find_element_by_id("person_agree_terms").click()
    ## nextPage
    dr.find_element_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[5]/button').click()

rebot_login()  
getTicket()

dr.close()