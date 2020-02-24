---
title: Start Web Scraping (1/10)
subtitle: Learn the basics of web scraping
summary: EXPLORING THE BASICS
authors:
- Xiaoou WANG
tags: ["WebScraping","Python"]
categories: []
date: "2020-01-01"
# lastMod: "2019-09-05T00:00:00Z"
featured: false
draft: false
# markup: blackfriday

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ""
  focal_point: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["Python"]
---

{{% toc %}}


## basic approach using urlopen from request


```python
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())
```

```
## b'<html>\n<head>\n<title>A Useful Page</title>\n</head>\n<body>\n<h1>An Interesting Title</h1>\n<div>\nLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n</div>\n</body>\n</html>\n'
```

## Use beautiful soup here. Compared to urlopen, there is no need to call `read` to access the website's content.



```python
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
```

```
## <h1>An Interesting Title</h1>
```

## Same output with several expressions



```python
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'html.parser')
# same output using the following lines
print(bs.h1)
```

```
## <h1>An Interesting Title</h1>
```

```python
print(bs.html.h1)
```

```
## <h1>An Interesting Title</h1>
```

```python
print(bs.html.body.h1)
```

```
## <h1>An Interesting Title</h1>
```

```python
print(bs.body.h1)
# lxml parser (replace html.parser with lxml) has some advantages over html.parser in that it is generally better at parsing “messy” or malformed HTML code. It is forgiving and fixes problems like unclosed tags, tags that are improperly nested, and missing head or body tags. It is also somewhat faster than html.parser, although speed is not necessarily an advantage in web scraping, given that the speed of the network itself will almost always be your largest bottleneck.  P.S. html5lib is also possible
```

```
## <h1>An Interesting Title</h1>
```

## handle webpage adress error



```python
# handle erros This HTTP error may be “404 Page Not Found,” “500 Internal Server Error,” and so forth
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html22")
except HTTPError as e:  # this is actually a more layman understanding of URLError. HTTPError is a predefined name so that you can't replace it with other names
    print(e)
except URLError as e:
    print("The server could not be found!")
    # the server error means there is no such website as This HTTP error may be “404 Page Not Found,” “500 Internal Server Error,” and so forth
else:
    print(html.read())
```

```
## HTTP Error 404: Not Found
```

## write a function to handle url error problems (very important to group usual patterns)



```python
# access a non existent tag
print(bs.nonexistent)
# this would return error, can't have two none nested
# print(bs.nonexistent.tag)
```

```
## None
```


```python
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

# check if an element is none

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
```

```
## <h1>An Interesting Title</h1>
```
