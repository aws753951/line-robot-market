from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

from mongodb_func import *
# from cpi import cpi_index
# from gdp import gdp_index, gdp_index_inv
# from futu import futu_news, futu_news_us

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
    # if 'cpi' in msg.lower():
    #     text = '最新的美國cpi數據如下' + cpi_index() + '詳情請見: ' + 'https://www.bls.gov/news.release/cpi.nr0.htm'
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    # elif 'gdp' in msg.lower():
    #     text = '最新的美國gdp數據如下' + gdp_index_inv() + '詳情請見: ' + gdp_index()
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    # elif '中文新聞' in msg:
    #     text = '最新的10則市場新聞如下' + futu_news()
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
    # elif '英文新聞' in msg:
    #     text = '最新的10則市場新聞如下' + futu_news_us()
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))    
    # else:
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()