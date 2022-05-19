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
from futu import futu_news, futu_news_us
from chip import chip
from response import *


YOUR_CHANNEL_ACCESS_TOKEN = '+Qnngs1qVk30BNjSm7loQkaIgAh3fqks4ztR/AvWU7cLwJgkgUdLxJWWkz5HO/yBkqlc34NDfuYDfJAnZEJHJDR9zSCcg7SNZmsKLGuhQUY5axVYKkdrsH51f46WfIDWsVW/l8F5yZitJqhpRv9fuAdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = '2e1037f03f3f69dfba07efbf5083b3b7'


line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


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
    chiplists = chip()
    for i, c in enumerate(chiplists):
        if msg.lower() in c[0]:
            text = f'{msg.lower()}近期投資部位變化如下' + chiplists[i][1]
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    if 'cpi' in msg.lower():
        text = '最新的美國cpi數據如下' + "\n" + cpi_index_inv() + '詳情請見:' + "\n" + 'https://www.bls.gov/news.release/cpi.nr0.htm'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif 'gdp' in msg.lower():
        text = '最新的美國gdp數據如下' + "\n" + gdp_index_inv() + '詳情請見:' + "\n" + gdp_index()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif 'retail sales' in msg.lower():
        text = '最新的美國Retail Sales ' + "\n" + sales_index_inv() + '詳情請見:' + "\n" + sales_index()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif '新聞' in msg:
        text = '最新的10則市場新聞如下' + futu_news()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    elif 'news' in msg:
        text = '最新的10則市場新聞如下' + futu_news_us()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text)) 
    elif '籌碼' in msg:
        message = buttons_chips()
        line_bot_api.reply_message(event.reply_token, message)
    elif '經濟數據' in msg:
        message = buttons_econs()
        line_bot_api.reply_message(event.reply_token, message)
    elif '所有功能' in msg:
        message = buttons_total()
        line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handle_message(event):
    if isinstance(event, PostbackEvent):
        if event.postback.data[0:1] == "c":
            celebrity = event.postback.data[2:].lower()
            if celebrity != 'wait':
                chiplists = chip()
                # names = [chiplists[i][0] for i, c in enumerate(chiplists)]
                for i, c in enumerate(chiplists):
                    if celebrity in c[0]:
                        text = f'{celebrity}的近期投資部位變化如下' + chiplists[i][1]
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
            else:
                text = '請直接輸入人名(得英文)'
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
        elif event.postback.data[0:1] == "e":
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
            elif total == 'chips':
                message = buttons_chips()
                line_bot_api.reply_message(event.reply_token, message)
            elif total == 'news':
                text = '最新的10則市場新聞如下' + futu_news()
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))







    


if __name__ == "__main__":
    app.run()