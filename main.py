from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request

username = str(input('Enter Username: '))
driver = webdriver.Chrome()

driver.get('https://www.instagram.com/' + username + '/')

# for scrolling
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

posts = []
links = driver.find_elements_by_tag_name('img')
for link in links:
    post = link.get_attribute('src')
    posts.append(post)
posts.pop()
driver.quit()
print("Links are here \n links Start :: \n")
for i in range(len(posts)):
    print(posts[i])
    sleep(2)
    urllib.request.urlretrieve(posts[i], 'media' + str(i) + '.jpg')
