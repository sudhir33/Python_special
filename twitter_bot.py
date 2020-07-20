from selenium import webdriver
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

 

usr = "marnalaashok8055@gmail.com"
pwd = "Don@8055"
image_path ="img.jpg"

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

sleep(5)#error here
usr_box=driver.find_element_by_xpath("//input[@type='text']")
usr_box.send_keys(usr)
sleep(3)

pwd_box = driver.find_element_by_xpath("//input[@type='password']")
pwd_box.send_keys(pwd)
sleep(3)

login_button = driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div""")
login_button.submit()
sleep(3)

img_icon = driver.find_element_by_xpath('//input[@accept="image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm"]')
img_icon.send_keys("C:/Users/admin/Desktop/img.jpg");


tags = driver.find_element_by_xpath('''//div[@class='notranslate public-DraftEditor-content']''')
tags.send_keys('''#pawankalyan #ramchran''')
sleep(3)
"""
text_box = driver.find_element_by_id('tweet-box-home-timeline')
text_box.send_keys('automation with image and text #getsetpython')
sleep(3)

tweet_button = driver.find_element_by_css_selector('button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn')
tweet_button.click()
"""
