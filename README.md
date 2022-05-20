line 聊天機器人
===
需要用到line developers console 與heroku 還有mongodb <br>
### 建立與line機器人的連結<br>
於line developers console 創立channel，並取得id跟token <br>
回到heroku註冊，創立專案後取得domains url<br>
貼回line developers，後面加/callback，並開啟Use webhook <br>
verify成功與否，得看程式加載進去是否有效<br>
### 程式碼的取得<br>
https://github.com/line/line-bot-sdk-python<br>
### 加掛到mongodb
於youtuber maso0310內有說明<br>
Note:在使用mongodb的連結時，得新增第二個使用者，其連結才能正常使用<br>
### 非上傳至heroku也能正常運行程式碼
於youtuber maso0310內有說明<br>
ngrok<br>
Note:在使用時須注意檔案是否已經運行(雙cmd)，LINE上的verify才會成功<br>
Note:不用先上傳至heroku，也可以運行，須注意安裝檔很多時候都已經安裝了，所以網域在主機上時可正常運行，但至heroku卻無法，requirements.txt要加上去，版本問題也要注意<br>
### 虛擬環境應用
於heroku無法使用dotenv等環境變數<br>
webdriver等相關使用selenium時會用到的工具，於heroku後台設定環境變數<br>
![image](https://user-images.githubusercontent.com/101057598/169499362-9e33ab2e-7ff1-4a7b-81b0-243fcd44ad9a.png)
![image](https://user-images.githubusercontent.com/101057598/169499389-073a04d8-4feb-4065-b36f-5f1b74917763.png)
於使用selenium的程式碼內，換上以下的code (此專案為futu.py/ youtube.py 有用到)<br>
![image](https://user-images.githubusercontent.com/101057598/169506465-76bee7a8-e60a-4ab3-a9b8-bde7e74e966a.png)
 ### 使heroku不睡著
 於youtuber maso0310內有說明<br>
 Note: 在本地上運行此招會盪，當要上傳至heroku時在貼相關程式碼<br>
![image](https://user-images.githubusercontent.com/101057598/169506371-63f058ad-69fe-4e19-b215-a8a14d895864.png)
 ### 留言蒐集至mongodb
 於youtuber maso0310內有說明<br>
 Note: 其code有誤，其write_one_data()中間不能加入eval()，會出現錯誤<br>
 Note: 餵進mongodb得是字典型態，故得用json.loads() 把body轉成字典<br>
 dict = json.loads(body) 參考(mongodb_func.py)
 ##### 附加功能
 原先寫入mongodb的資料內無特別轉換成姓名以及我要的資訊，為了方便於資料庫內查看每則留言為誰、以及時間為何，此處調整其寫入方法<br>
 1. gobal body，把body偷渡出來，在我想要的時候才寫入→於使用者打入訊息時寫入，可調整<br>
 2. 由於body被偷渡出來後，可以無視get_group_member_profile()，能抓到body內個人uid就可知道其名字→使用get_profile()<br>
 ![image](https://user-images.githubusercontent.com/101057598/169505722-da6ef391-afc7-4cdd-a245-6ec18f11b073.png)
![image](https://user-images.githubusercontent.com/101057598/169505755-8a15a7df-98c8-4fd2-936d-e541930d8e90.png)
![image](https://user-images.githubusercontent.com/101057598/169505779-62305e56-29b6-4c93-9c78-d4c547340f4e.png)
![image](https://user-images.githubusercontent.com/101057598/169505797-5b33cd8b-216e-4ba1-946a-90ad415a9de6.png)
 ### 其他已研究但未加入的功能
 #### 人名搜尋
 這原本是要寫加載籌碼面相關資料，一開始設計為使用者輸入關鍵字即可找到相關資料，但由於版面設計不佳，故此專案調整為提供網址，讓使用者自行搜尋較為妥當<br>
 未寫入等關鍵code:<br>
 ![image](https://user-images.githubusercontent.com/101057598/169505426-efd0c360-b1e0-4174-b5df-4ea387817e68.png)
 ### 此專案要爬的相關網站
 基本上都是跟市場有關的資訊<br>
 跟聯準會有關的新聞(外國新聞更新速度較快)<br>
 https://api.queryly.com/cnbc/json.aspx?queryly_key=31a35d40a9a64ab3&query=fed&endindex=0&batchsize=10&callback=&showfaceted=false&timezoneoffset=-480&facetedfields=formats&facetedkey=formats%7C&facetedvalue=!Press%20Release%7C&needtoptickers=1&additionalindexes=4cd6f71fbf22424d,937d600b0d0d4e23,3bfbe40caee7443e,626fdfcd96444f28<br>
 市場最新新聞(富途牛牛為中文新聞內最好的平台)<br>
 https://news.futunn.com/hk/main?lang=zh-hk<br>
 經濟數據(串接investing.com的初步資料跟美國經濟數據公布的官網)(美國公布的經濟數據官網為原始資料，內含相關解說以及更細的資料)<br>
 https://www.investing.com/economic-calendar/gdp-375<br>
 https://www.bea.gov/data/gdp/gross-domestic-product<br>
 https://www.census.gov/retail/index.html<br>
 https://www.bls.gov/news.release/cpi.nr0.htm<br>
 觀察每日股市區域板塊<br>
 https://finviz.com/map.ashx<br>
 籌碼資料<br>
 https://dataroma.com/m/home.php<br>
 聯準會記者會說明<br>
 https://www.federalreserve.gov/newsevents/pressreleases.htm<br>
 恐慌指數<br>
 https://edition.cnn.com/markets/fear-and-greed<br>
 外加兩位針對股市變化進行講解的youtuber<br>
 nana說美股 / 陽光財經<br>
 
 
