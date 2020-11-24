---
title: Use python to recursively merge files
summary: all the files in a directory with a certain extension
subtitle:
authors:
- Xiaoou WANG
tags: ["Python"]
# categories: [""]
date: "2020-03-17"
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

## What

Use python to recursively merge all the files in a folder with a certain extension (`.js` in this case)

## Why

I have a couple of javascript tutorials with a lot of common functions and methods. These tutorials are in different folders involving sometimes very deep structures.

## How


```python
from os import walk
# initiate a empty string
final_text = ""
# get all the files with extension js, the walk function gives a tuple
for (dirpath,dirname,filenames) in walk("/Users/rosingle/Documents/javascript/modernJavascript/"):
    for file in filenames:
        # the / is important :D
        my_path = dirpath+"/"+file
        if my_path.endswith(".js"):
            with open(my_path) as file:
                # read the whole file
                final_text += file.read()

with open("out.txt","w") as f:
    f.write(final_text)
```


{{< figure library="true" src="enjoy.png" lightbox="true" >}}
