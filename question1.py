import urllib.request
import re
import matplotlib.pyplot as plt
import numpy as np

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

years = []
# use all page url to get html content
for u in urls :
    content = urllib.request.urlopen(u)
    html_str = content.read().decode('utf-8')
    # get announced year
    pattern = author + '[\s\S]*?originally announced[\s\S]*?</p>'
    result = re.findall(pattern, html_str)
    for r in result :
        ptn = 'originally announced[\s\S]*?</p>'
        r = re.findall(ptn, r)[0]
        years.append(r.split("</span>")[1].split(" ")[2].split(".")[0])

years = sorted(years)
# count year number
year = []
num = []
for y in years :
    if y not in year :
        year.append(y)
        num.append(years.count(y))
# plot bar graph
plt.bar(range(len(num)), num, tick_label=year)
plt.title('Author : ' + author.replace('+', ' '))
plt.show()
