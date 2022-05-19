from linebot.models import *

def buttons_total():
    message = TemplateSendMessage(
        alt_text='想要查甚麼呢?',
        template=ButtonsTemplate(
            thumbnail_image_url="https://generisonline.com/wp-content/uploads/2022/04/MarketingResources_Thumbnail_Search.width-1200.jpg",
            title="目前僅開放以下功能",
            text="也可以直接輸入關鍵字「經濟數據」、「籌碼」、「新聞」",
            actions=[
                PostbackTemplateAction(
                    label="美國經濟數據",
                    data='t&econs'
                ),
                PostbackTemplateAction(
                    label="大佬籌碼資料",
                    data='t&chips'
                ),
                PostbackTemplateAction(
                    label="最新新聞(請給我30秒)",
                    data='t&news'
                ),
            ]
        )
    )
    return message

def buttons_chips():
    message = TemplateSendMessage(
        alt_text='想查詢哪位大佬近期交易狀況呢?',
        template=ButtonsTemplate(
            thumbnail_image_url="https://cdn2.ettoday.net/images/2689/2689375.jpg",
            title="你可能會想知道以下幾位",
            text="註:僅限有向13Filings申報",
            actions=[
                PostbackTemplateAction(
                    label="Warren Buffet",
                    data="c&Warren Buffet"
                ),
                PostbackTemplateAction(
                    label="Chase Coleman",
                    data="c&Chase Coleman"
                ),
                PostbackTemplateAction(
                    label="Bill Ackman",
                    data="c&Bill Ackman"
                ),
                PostbackTemplateAction(
                    label="我自行輸入",
                    data="c&wait"
                )
            ]
        )
    )
    return message

def buttons_econs():
    message = TemplateSendMessage(
        alt_text='想查詢哪項經濟數據呢?',
        template=ButtonsTemplate(
            thumbnail_image_url="https://d28wu8o6itv89t.cloudfront.net/images/EconomicCalendarjpg-1595313765137.jpeg",
            title="你可能會想知道以下這些",
            text="可直接輸入",
            actions=[
                PostbackTemplateAction(
                    label="美國最新GDP資料",
                    data="e&gdp"
                ),
                PostbackTemplateAction(
                    label="美國最新CPI資料",
                    data="e&cpi"
                ),
                PostbackTemplateAction(
                    label="美國最新Retail Sales資料",
                    data="e&sales"
                ),
                PostbackTemplateAction(
                    label="我不依我不依，我自己找",
                    data="e&gofind"
                ),
            ]
        )
    )
    return message

