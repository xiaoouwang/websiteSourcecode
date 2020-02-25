---
title: Add a floating TOC to R blogdown's academic theme
subtitle: MAKE LIFE BETTER
summary: CUSTOMIZING A HUGO THEME
authors:
- Xiaoou WANG
tags: ["Javascript","Web development","Hugo","R","Front-end"]
categories: ["Front-end","Javascript","Hugo","R"]
date: "2020-02-24"
# lastMod: "2020-01-02"
featured: false
toc: true
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
# projects: ["Python"]
---

{{% alert tip %}}
Note that you can add `toc = false` in the front matter of each post to disable this feature.
{{% /alert %}}

<!-- {{% toc %}} -->

## 1. Basics

In hugo, a theme can be customized by adding and deleting files in the folder `theme`. In the layout subfolder, you can add a `single.html` to define any layout that hasn't been predefined.

## 2. Adding a TOC element to the post template

A floating toc can be useful and beautiful too. Basically two steps are necessary :

1. Add a `single.html` file under `theme/layouts/_default` with the following code :

{{< gist xiaoouwang 5baf36b2df7a85160b02c454ce001915 >}}



2. Delete `theme/layouts/section/post.html`

## 3. Create the toc template

Add a `toc.html` file under `theme/layouts/partials/`

The following gist would be sufficient. I also create a `to top` button at the bottom right corner of every blog post.

There's a little bug that I would probably fix when I have some spare time. The bug is the first h2 tag `table of contents` which is actually a dead link so no jumping would happen when you click it.

Also there are some redundant css in it, but you can just let it go for now.

{{< gist xiaoouwang 706e6eaf96c49b3606ce3a753c05dec8 >}}

## 4. Finally

You can see the final effect on this page. :heart:
![alt text](https://d144mzi0q5mijx.cloudfront.net/img/E/N/Enjoy.png "Logo Title Text 1")