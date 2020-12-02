import requests
from selenium import webdriver
import time
from credentials import *

# Get my youtube channel's data
response = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + CHANNEL_ID + "&maxResults=1&order=date&type=video&key=" + API_KEY)
items = response.json()

# Store latest youtube video's link in a variable
latestVideoId = items[u'items'][0][u'id'][u'videoId']
latestVideoLink = 'https://youtu.be/' + latestVideoId

# Open chrome
PATH = "/Users/jeremiah/Documents/Code/update-bios/chromedriver"
driver = webdriver.Chrome(PATH)


def enter_input(xpath, input_text):
    input_element = driver.find_element_by_xpath(xpath)
    if input_element.get_attribute("value") != '':
        input_element.clear()
    input_element.send_keys(input_text)


def click_button(xpath):
    button_element = driver.find_element_by_xpath(xpath)
    button_element.click()


# 1. Navigate to instagram
driver.get("https://www.instagram.com")
time.sleep(1)


# login
enter_input('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input', instaUsername)
enter_input('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input', instaPassword)
click_button('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')  # login button

time.sleep(2)
driver.get('https://www.instagram.com/accounts/edit/')

# update bio with latest video link
enter_input('/html/body/div[1]/section/main/div/article/form/div[3]/div/div/input', latestVideoLink)
click_button('/html/body/div[1]/section/main/div/article/form/div[10]/div/div/button')  # save changes button
time.sleep(2)   # wait for success


print("Instagram bio was updated with:" + latestVideoLink)

# 2. Navigate to twitter
driver.get("https://www.twitter.com")
time.sleep(2)

enter_input('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/label/div/div[2]/div/input',twitterUserName)
enter_input('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[2]/div/label/div/div[2]/div/input',twitterPassword)
click_button('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[3]/div')  # login button

time.sleep(2)
driver.get('https://twitter.com/settings/profile')

time.sleep(1)
enter_input('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[6]/label/div/div[2]/div/input', latestVideoLink)
click_button('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div')# save update


print("Twitter bio was updated with:" + latestVideoLink)

time.sleep(1)  # Allow time for twitter to save
driver.quit()


print('################### Until The Next Time, Jeremiah ##########################')
