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
line_bot_api = LineBotApi('2xGfM8DqnU7eKhSIJTZsiVpnQmh029oVGCImxhB0liD')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('2d82f72b9214b10d2394a87c45608799')