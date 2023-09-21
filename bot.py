import telegram
from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = '5743359307:AAH-N6tqfjG-3pEuQ8U2N04c7ihsk_NyI9E'
bot = telegram.Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message_text = update.message.text
    bot.send_message(chat_id=chat_id, text=message_text)
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    app.run(debug=True)
