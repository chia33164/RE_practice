# Regurlar Expression Practice

## Envirenment

	ubuntu 18.04.2  LTS

## 題目

https://moodle.ncku.edu.tw/pluginfile.php/1364207/mod_resource/content/1/PL_HW2.pdf

### question 1

先用把 input 塞到 author 中
變數 url 為爬蟲的目標 url （ 用來查詢 author ）
用 urllib.request 爬下目標 url 的內容
接著利用 re.finall 來正規化爬下的內容 （ 其實就是從內容中取出需要的字串 ）

正規化 : 

	取出 pagination-list 開頭 </ul> 結尾的字串,接著在每段上述取出的字串中

再截出 href= 開頭 class 結尾的字串，該字串即為對應頁數的 url

這個階段中取出不同頁數的 url ，並存到 urls 這個 list
藉此可以一一爬下每個頁數資訊
接著一一爬下 urls 中的 url 的頁面的內容
一樣用 re.findall 來正規化爬下的內容

正規化 :

	取出由作者名稱開頭中間有 originally announced 結尾有</p> 的字串
	這樣就可以確保該篇的作者中有我們指定的人
	接著將上述的結果切出 originally announced 開頭 </p> 結尾的內容
	然後切出年份後存到 years 這個 list

接著對 years 做排序 （ sort ）
然後對 years 做 group
把相同的 element group 在一起 （ 存在 list year ）
並且算出他的數量 ( 存在 list num )

最後根據 num year 用 matplotlib 畫出 bar graph

**執行程式**

```
$ python3 question1.py
```

**input**

Ian Goodfellow

**output**


![](https://i.imgur.com/ReyOESS.png)

### question 2

先用把 input 塞到 author 中
變數 url 為爬蟲的目標 url （ 用來查詢 author ）
用 urllib.request 爬下目標 url 的內容
接著利用 re.finall 來正規化爬下的內容 （ 其實就是從內容中取出需要的字串 ）

正規化 :

	取出 pagination-list 開頭 </ul> 結尾的字串,接著在每段上述取出的字串中

再截出 href= 開頭 class 結尾的字串，該字串即為對應頁數的 url

這個階段中取出不同頁數的 url ，並存到 urls 這個 list
藉此可以一一爬下每個頁數資訊
若該名作者的文章少於 50 篇 urls 這個 list 就會為空, 因為沒有其他頁碼了
所以就直接把原 url 放進 urls 這個 list 中
接著一一爬下 urls 中的 url 的頁面的內容
一樣用 re.findall 來正規化爬下的內容 （ 只取出 Authors : 後的幾個人名 ）

正規化 :

	取出 Authors: 開頭 </p> 結尾的字串藉此可以把該篇文章的全部作者都取出來
	在把上述的正規化一一再正規化一次取出 author 名稱

然後必須確定該篇的作者中包含我們指定的 author，若有就把該篇的作者都放進 co_author 這個 list
否則就不放入，因為該篇不是由該作者完成，而是名字相似的人完成

接著對 co_author 做排序 （ sort ）並存到 s 
接著對 s 做 group
把相同的 element group 在一起 
並且算出他的數量
一組表示為 [ co_author’s name, the co_author’s number ]
把每一組都 append 到 l
這個過程中，除了 author 自己，其他都要放進去

最後把 l 中的每個元素都印出來
方式： 
el 為 l 中的每一組元素
el[0] 為 co_author’s name
el[1] 為 the co_author’s number
印出 el[0]: el[1] times

**執行程式**
```
$ python3 question2.py
```
