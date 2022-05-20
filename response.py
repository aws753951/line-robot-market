from linebot.models import *

def buttons_total():
    message = TemplateSendMessage(
        alt_text='想要查甚麼呢?',
        template=ButtonsTemplate(
            thumbnail_image_url="https://generisonline.com/wp-content/uploads/2022/04/MarketingResources_Thumbnail_Search.width-1200.jpg",
            title="目前僅開放以下功能",
            text="也可以直接輸入關鍵字「Fed」、「經濟數據」、「市場新聞」、「油土伯」、「其他」",
            actions=[
                PostbackTemplateAction(
                    label="最新有關聯準會的新聞",
                    data='t&news'
                ),
                PostbackTemplateAction(
                    label="美國重要經濟數據",
                    data='t&econs'
                ),
                PostbackTemplateAction(
                    label="其他市場新聞",
                    data='t&futunews'
                ),
                PostbackTemplateAction(
                    label="最新股市博主講了啥",
                    data='t&youtube'
                ),
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

def other():
    message = TemplateSendMessage(
        alt_text='其他市場資訊',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/1e40FmU.png",
                    action=URITemplateAction(
                        label="今天的股市是漲還是跌呢?",
                        uri="https://finviz.com/map.ashx"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/xbEwmxR.jpg",
                    action=URITemplateAction(
                        label="機構大佬們近期交易狀況?",
                        uri="https://dataroma.com/m/home.php"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/ZQVJ9Tm.jpg",
                    action=URITemplateAction(
                        label="fed的記者會又說了啥?",
                        uri="https://www.federalreserve.gov/newsevents/pressreleases.htm"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Gx7toTB.jpg",
                    action=URITemplateAction(
                        label="近期的恐慌指數到哪呢了?",
                        uri="https://edition.cnn.com/markets/fear-and-greed"
                    )
                )
            ]
        )
    )
    return message

