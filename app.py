from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

from mongodb_func import *
from economics import *
from futu import *
from response import *
from fed import *
from youtube import *


YOUR_CHANNEL_ACCESS_TOKEN = '+Qnngs1qVk30BNjSm7loQkaIgAh3fqks4ztR/AvWU7cLwJgkgUdLxJWWkz5HO/yBkqlc34NDfuYDfJAnZEJHJDR9zSCcg7SNZmsKLGuhQUY5axVYKkdrsH51f46WfIDWsVW/l8F5yZitJqhpRv9fuAdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = '2e1037f03f3f69dfba07efbf5083b3b7'


line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

import threading
import requests
import time

def wakeup():
    while True:
        url = 'https://line-robot-market.herokuapp.com/' + 'heroku_wake_up'
        res = requests.get(url)
        if res.status_code == 200:
            print('200')
        else:
            pass
        time.sleep(28*60)

threading.Thread(target=wakeup).start()
        


body = None
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    global body
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    dicts = get_body_info(body, line_bot_api)
    write_to_data(dicts)
    msg = event.message.text
    if 'cpi' in msg.lower():
        text = '最新的美國cpi數據如下' + "\n" + cpi_index_inv() + '詳情請見:' + "\n" + 'https://www.bls.gov/news.release/cpi.nr0.htm'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif 'gdp' in msg.lower():
        text = '最新的美國gdp數據如下' + "\n" + gdp_index_inv() + '詳情請見:' + "\n" + gdp_index()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif 'retail sales' in msg.lower():
        text = '最新的美國Retail Sales ' + "\n" + sales_index_inv() + '詳情請見:' + "\n" + sales_index()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif '市場新聞' in msg:
        text = '最新的10則市場新聞如下' + futu_news()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif 'fed' in msg.lower() or '聯準會' in msg:
        text = '最新有關聯準會10則市場新聞如下' + "\n" + fed_news()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif '經濟數據' in msg:
        message = buttons_econs()
        line_bot_api.reply_message(event.reply_token, message)
    elif '所有功能' in msg:
        message = buttons_total()
        line_bot_api.reply_message(event.reply_token, message)
    elif '其他' in msg or 'other' in msg.lower():
        message = other()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'yt' in msg.lower() or '油土伯' in msg:
        text = '最新youtuber的市場影片如下' + "\n" + youtube() + "\n" + '其他正在施工中，請洽朱鴻埕'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif '不帥' in msg:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='你才不帥，小王八蛋'))
    elif '不醜' in msg:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='誰不醜? 朱鴻埕的字典只有帥'))
    elif '醜' in msg:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='你超醜，噁心稀巴爛'))
    elif '帥' in msg:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='你說我很帥嗎? 這很正常啊'))
    elif '屌' in msg:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='哪裡屌? 我超勇的好嗎'))
    elif '朱鴻埕' in msg:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='找我幹嘛? 有屁快放'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='看不懂你說的，請輸入「所有功能」查看你要的內容'))



@handler.add(PostbackEvent)
def handle_message(event):
    if isinstance(event, PostbackEvent):

        if event.postback.data[0:1] == "e":
            econ = event.postback.data[2:].lower()
            if econ != 'gofind':
                if econ == 'cpi':
                    text = '最新的美國cpi數據如下' + "\n" + cpi_index_inv() + '詳情請見: ' + "\n" + 'https://www.bls.gov/news.release/cpi.nr0.htm'
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
                elif econ == 'gdp':
                    text = '最新的美國gdp數據如下' + "\n" + gdp_index_inv() + '詳情請見: ' + "\n" + gdp_index()
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
                elif econ == 'sales':
                    text = '最新的美國Retail Sales ' + "\n" + sales_index_inv() + '詳情請見: ' + "\n" + sales_index()
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
            else:
                text = '我幫你導到相關網站，請自行搜尋: ' + 'https://hk.investing.com/economic-calendar/'
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))

        elif event.postback.data[0:1] == "t":
            total = event.postback.data[2:].lower()
            if total == 'econs':
                message = buttons_econs()
                line_bot_api.reply_message(event.reply_token, message)
            elif total == 'news':
                text = '最新的10則fed新聞如下' + "\n" + fed_news()
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
            elif total == 'futunews':
                text = '最新的10則市場新聞如下' + "\n" + futu_news() + "\n" + '其他正在施工中，請洽朱鴻埕'
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
            elif total == 'youtube':
                text = '最新youtuber的市場影片如下' + "\n" + youtube() + "\n" + '其他正在施工中，請洽朱鴻埕'
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    


if __name__ == "__main__":
    app.run()