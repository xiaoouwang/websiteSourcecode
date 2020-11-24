---
title: Scraping project 1 - grab french news and audio every day at 20:10
summary:
subtitle:
authors:
- Xiaoou WANG
tags: ["Python","Web Scraping Projects"]
# categories: [""]
date: "2020-03-18"
# lastMod: "2019-09-05T00:00:00Z"
featured: false
draft: false
markup: blackfriday
toc: true
# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ""
  focal_point: ""

---



{{% toc %}}

## Why and What

As a French lover I am a fan of a news broadcasting program called `journal en francais facile` (news in easy french), so I deciced to crawl automatically :

1. The news script
2. The mp3 file

## Logic


```python
# declare some global variables #

# automatic filename changement
today = str(datetime.date.today()).replace("-","_")
# where the file is stored
rfi_path = "/Users/rosingle/Documents/rfi/"

article_url = "https://savoirs.rfi.fr"+ getRecentArticleUrl("https://savoirs.rfi.fr/fr/recherche/rubrique/apprendre/thematique/langue-francaise-2721")
audio_url = getAudioUrl(article_url)
article_text = getArticleText(article_url)
writeArticleText(article_text)
downloadAudio(audio_url)
```

## Libraries used

```python
import os  # check file exists
import datetime # automatically create filename to avoir file deletion
import requests # download mp3 and get html code
from urllib.request import urlopen # these three contain some useful help functions to handle exceptions
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup # web scraping
```
## Get the most recent article url


```python
def getRecentArticleUrl(url):
    '''return the most recent rfi news url'''
    try:
        rfi_total_url = urlopen(url)
    except HTTPError as e:
        print("the site adress may have been changed")
    rfi_total_html = BeautifulSoup(rfi_total_url, "html.parser")
    rfi_recent = rfi_total_html.find(class_='results').article.h2.a['href'] # always the first element
    return rfi_recent
```

## Get the audio url


```python
def getAudioUrl(url):
    try:
        audio_html = urlopen(url)
    except HTTPError as e:
        print("audio url not valid")
    audio_url = BeautifulSoup(audio_html,"html.parser")
    audio_url = audio_url.audio.source['src']
    return audio_url
```
## Get the script text


```python
def getArticleText(url):
    try:
        text_html = urlopen(url)
    except HTTPError as e:
        print("text url not valid")
    text_url = BeautifulSoup(text_html,"html.parser")
    body_txt = text_url.find(text="Transcription").parent.parent.parent.next_sibling.find_all('p')
    return body_txt
```
## Write the text to a file and download the mp3 by downloading each time some small chunks

{{% alert success %}}
Note that I keep the html markdown here because it's useful to me
{{% /alert %}}


```python
def writeArticleText(text):
    text_path = rfi_path + today + '_rfi.html'
    if os.path.exists(text_path):
        os.remove(text_path)
    with open(text_path,'a+') as f:
        for line in text:
            f.write(str(line)+"\n")

def downloadAudio(mp3_url):
    mp3 = requests.get(mp3_url,stream = True)
    mp3_path = rfi_path + today + "_rfi.mp3"
    if os.path.exists(mp3_path):
        os.remove(mp3_path)
    with open(mp3_path,"wb") as audio:
        for chunk in mp3.iter_content(chunk_size=1024):
             if chunk:
                audio.write(chunk)
```

## Bonus (Automatic scheduling on mac)

See [this article](https://www.iexplain.org/how-to-add-a-cronjob-in-macos/) for some detailed information.

In short,fire up your terminal and type `crontab -e`. Then you can make some commands run at a regular interval, for example mine is :

![](img/2020-03-18-17-49-14.png)

which means `every day on every month of every year`.

For some task generation see [here](https://crontab.guru/)


{{< figure library="true" src="enjoy.png" lightbox="true" >}}
