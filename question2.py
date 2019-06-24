import urllib.request
import re

# get html content
# author = "Ian+Goodfellow"
author = input('Input Author: ')
author = author.replace(' ', '+')

domain = "https://arxiv.org"
url = domain + "/search/?query=" + author + "&searchtype=author"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')

author = author.replace('+', ' ')

# get all page url
pattern1 = 'pagination-list[\s\S]*?</ul>'
result = re.findall(pattern1, html_str)
urls = []
if len(result) == 0 :
    urls.append(url)
else :
    pattern2 = 'href=[\s\S]*?class'
    urls = re.findall(pattern2, result[0])
    for idx, u in enumerate(urls) :
        urls[idx] = domain + u.split("href=\"")[1].split("class")[0].replace('amp;', '').split("\"\n")[0]

co_authors = []
# use all page url to get html content
for u in urls :
    content = urllib.request.urlopen(u)
    html_str = content.read().decode('utf-8')
    # get authors
    pattern = 'Authors:[\s\S]*?</p>'
    result = re.findall(pattern, html_str)
    for r in result :
        p = '\">[\s\S]*?</a>'
        t = re.findall(p, r)
        for n in t :
            tmp = n.split("\">")[1].split("</a>")[0].strip()
            if tmp == author :
                for x in t :
                    tmp = x.split("\">")[1].split("</a>")[0].strip()
                    co_authors.append(tmp)
                break
# sort co_author with alphabet
s = sorted(co_authors)
# group same author and show time
l = []
author = author.replace('+', ' ')
for x in s :
    if x != author :
        if [x, s.count(x)] not in l :
            l.append([x, s.count(x)])
for el in l :
    print(el[0] + ": " + str(el[1]) + " times")