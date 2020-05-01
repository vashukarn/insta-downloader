# insta-downloader

[![N|Solid](https://vashukarn.github.io/top-logo.png)](https://vashukarn.github.io/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/vashukarn/insta-downloader)

## General Information

A Python automated script that download all instagram photos of a particular user at once. As we know that web scraping doesn't work with BeautifulSoup for Dynamic pages in which that code go on updating.
So, I used the selenium web browser to scrape images from Instagram.

## Prerequisites

These should run without any error: <br>

- Selenium Module should be installed <br>
- Chrome webdriver should be installed <br>
- Path of Chrome Browser should be added to PATH <br>

```sh
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
```

## Methods we use:

#### Being a dynamic site we have to let load all the data present on the site so we have to scroll to bottom to load all the videos on the page of that particular user

```sh
def scroll(SCROLL_PAUSE_TIME, WAIT):
    print('Started Scrolling..')
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    sleep(WAIT)
    print('Reached to the end of page')
```

#### First we get the 'src' links in a 'list' named posts by finding elements for the tags which contains 'img'

```sh
posts = []
links = driver.find_elements_by_tag_name('img')
for link in links:
    post = link.get_attribute('src')
    posts.append(post)
```

#### We download images using urllib module

```sh
for i in range(len(posts)):
    sleep(2)
    urllib.request.urlretrieve(posts[i], 'media' + str(i+1) + '.jpg')
    print('Media' + str(i) + '.jpg downloaded.')
```

#### If you want to go headless just uncomment these two lines

```sh
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
```

## License:

#### MIT

**Free Software, Hell Yeah!**
