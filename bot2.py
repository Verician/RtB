from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import time
import datetime


def sleep ():
    time.sleep(2)


def NextB ():
    Next = browser.find_element_by_id("NextButton")
    Next.click()

def buttons ():
    choice = browser.find_element_by_class_name("radioSimpleInput")
    choice.click()
    sleep()
    NextB()
    sleep()

browser = webdriver.Firefox()
browser.get("https://www.helpraisethebar.co.uk/")

#Generates the visit time and day
today = datetime.datetime.now()
h = random.randrange(12,today.hour)
m = random.randrange(00,today.minute)
d = random.randrange(1,today.day)
#print(h)
#print(d)

sleep()
NextB()
sleep()

link = browser.find_element_by_link_text("Invite Card")
link.click()
sleep()

code = browser.find_element_by_id("InputStoreNum")
code.send_keys("92444")

date = browser.find_element_by_id("Index_VisitDateDatePicker")
date.click()
sleep()
date = browser.find_element_by_link_text(str(d))
date.click()

sleep()

time1 = browser.find_element_by_id("InputHour")
time1.click()
time1.send_keys(str(h))
time1.click()

time2 = browser.find_element_by_id("InputMinute")
time2.click()
time2.send_keys(str(m))
time2.click()

sleep()

NextB()
sleep()

button = browser.find_elements_by_id("surveyForm")
for b in button:
    print(b)
