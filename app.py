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

line_bot_api = LineBotApi('wSl8lia+mv4TdYFyzCwQW0gcPEFMcFAdSxNRwSzFhh1QgivrAeYIUjBIgpUZO5u5zWpQv0VrEerkSlMEzrAdIThaBbaO88BSvGjxyEQIAgsmyyW761/xEBcBmDIpg2Mjp+L0SJDVQv4yEiVJvYfOLQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58e467c9b8cee99cb2df8d809deddc6b')


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
    msg = event.message.text
    s = "哈囉!我是Hubway~~~"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()