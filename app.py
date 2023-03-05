#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('EEj3XSCWHGzG/Gg78aoEg0YeoHiGoBoqwMaiXVYHlLnJmZUiAW/OvMr+OVELsNJoPknz14dk6xvUSx6jKGdEVSqesG1HFi54RXcy10P5/INTMupe+m4XBekw6pzB5GWmTXz58rI4xcSUsD5LvHeBEgdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('2d82f72b9214b10d2394a87c45608799')
	
line_bot_api.push_message('U955160cb9f4dbb928becd2726bebdaa9', TextSendMessage(text='你可以開始了'))
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
  
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
 
    return 'OK'
