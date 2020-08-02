# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
import sys

reload(sys)  
sys.setdefaultencoding('utf8')
#set config
dr=webdriver.Chrome()

pg = "file:///Users/apple/Documents/cmi/getTicket/page.html"
ticketID = 'ticket_164512'
# pg = "https://kktix.com/events/leehomwang-4hroqlrd-0609/registrations/new"
# ticketID = 'ticket_164496'
account = 'x'
##########
from selenium.common.exceptions import NoSuchElementException             
def check_exists_by_xpath(xpath):
    try:
        dr.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True  
def check_exists_by_css(css):
    try:
        dr.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True
def myfunc():
    global ticketID
    try:
        myElem = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\""+ticketID+"\"]/div/span[4]")))
    except TimeoutException:
        print ("Loading took too much time!")

    a = dr.find_element_by_xpath("//*[@id=\""+ticketID+"\"]/div/span[4]")
    if a.text != u'尚未開賣':
        return True
    else:
        dr.refresh()
def rebot_login():
    global account
    dr.get("https://kktix.com/users/sign_in?back_to=https%3A%2F%2Fkktix.com%2F")
    element_text1 = dr.find_element_by_id('user_login')
    element_text1.send_keys(account)
    element_text2 = dr.find_element_by_id('user_password')
    element_text2.send_keys('xxx')
    dr.find_element_by_xpath('//input[@name="commit"]').send_keys(' ')

def getTicket_pg1():
    global pg, ticketID
    title = dr.title
    dr.get(pg)
    try:
        c = WebDriverWait(dr, 5).until_not(EC.title_is(title))
    except TimeoutException:
        dr.get(pg)
    

    while True:
        a = myfunc()
        if a==True:
            break
    print('a')
    
    try:
        myElem = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\""+ticketID+"\"]/div/span[4]/input")))
    except TimeoutException:
        print ("Loading took too much time!")

    
    a = dr.find_element_by_xpath("//*[@id=\""+ticketID+"\"]/div/span[4]/input")
    a.clear()
    a.send_keys('4')
    ## I agree
    dr.find_element_by_id("person_agree_terms").send_keys(' ')

    

    haveQuestions = False
    haveQuestions = check_exists_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[3]/div/div/div/div/div')
    print(haveQuestions)

    ## nextPage
    if haveQuestions == False:
        dr.find_element_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[5]/button').send_keys(' ')
    else:
        # watting key problem
        Q = dr.find_element_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[3]/div/div/div/div/div/p').text
        Ans = re.findall('([\w]+)', Q)
        if "請填入您所購買的演出日期" in Q:
            Ans ==["0609"]
        print Ans
        try:
            for i in Ans:
                if "請以半形小寫作答" in Q:
                   i = i.lower()
                print i
                dr.find_element_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[3]/div/div/div/div/div/div/div/input').clear()
                
                dr.find_element_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[3]/div/div/div/div/div/div/div/input').send_keys(i)
                dr.find_element_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[5]/button').click()
                if check_exists_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[5]/button')==False:
                    print 'break'
                    break
                else:
                    while True:
                        if dr.find_element_by_xpath('//*[@id="registrationsNewApp"]/div/div[5]/div[3]/div/div/div/div/div/div/div/input').is_enabled() ==True:
                            break
        except:
            pass
        try:
            myElem = WebDriverWait(dr, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="infoModal"]/div[2]/div/div[3]/button')))
        except TimeoutException:
            print ("Loading took too much time!!")

def getTicket_pg2():
    try:
        ## I know Button
        myElem = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="infoModal"]/div[2]/div/div[3]/button')))
    except TimeoutException:
        print ("Loading took too much time!")
    dr.find_element_by_xpath('//*[@id="infoModal"]/div[2]/div/div[3]/button').send_keys(' ')

    try:
        ## OK Button
        myElem = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registrationsShowApp"]/div[2]/div/div/div/ng-include[2]/div/div/div/div[3]/div/button')))
    except TimeoutException:
        print ("Loading took too much time!")
    dr.find_element_by_xpath('//*[@id="registrationsShowApp"]/div[2]/div/div/div/ng-include[2]/div/div/div/div[3]/div/button').send_keys(' ')

    
    try:
        # Finish Button
        myElem = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registrationsShowApp"]/div[2]/div/div/div/ng-include[2]/div/div/div/div[3]/div/div/div/div[1]/a')))
    except TimeoutException:
        print ("Loading took too much time!")

    dr.find_element_by_xpath('//*[@id="registrationsShowApp"]/div[2]/div/div/div/ng-include[2]/div/div/div/div[3]/div/div/div/div[1]/a').click()

def getTicket_pg3():
    try:
        myElem = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id,"field_email_")]')))
    except TimeoutException:
        print ("Loading took too much time!")
    all_elements = dr.find_elements_by_xpath('//*[contains(@id,"field_")]/div/div/input')

    all_elements[0].clear()
    all_elements[0].send_keys(u'蔡心敏')
    all_elements[1].clear()
    all_elements[1].send_keys('0424048@nkust.edu.tw')
    all_elements[2].clear()
    all_elements[2].send_keys('0978136278')
    ## 3.cancel this #
    ## dr.find_element_by_xpath('//*[@id="registrations_controller"]/div[4]/div[2]/div/div[5]/a').click()

# rebot_login()  
getTicket_pg1()
getTicket_pg2()
getTicket_pg3()

print("ok")