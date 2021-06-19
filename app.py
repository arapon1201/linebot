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

line_bot_api = LineBotApi('r5dc2s3fVR2Ccr6nkbRuOeoRH54ZrmhmxM + YsVz8RyW + dEs7mSwMa8Q6JHfwRjUnZ1oY73aC7499QRqj2WIGr + XJtitfxV19CqievC / lyaVjffrybM + 1fkIoPJF')
handler = WebhookHandler('e44f4a5128f5d71e57bfecc7d4c3e66e')

@app.route("/")
def test():
    return "OK"

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text  == "ありがとう":
        reply_message = "どういたしまして。"

    else :
        reply_message = f"あなたは、{event.message.text}と言いました。")
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message))


if __name__ == "__main__":
    app.run()