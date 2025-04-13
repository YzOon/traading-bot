from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

# معلومات البوت
BOT_TOKEN = '7948997743:AAH77y46rqNrJEJE1uk_sZJlk1f95fV7SKk'
CHAT_ID = '6280184532'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    symbol = data.get('symbol', 'Unknown')
    rsi = float(data.get('rsi', 0))
    price = float(data.get('price', 0))

    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    signal = ""
    if rsi <= 40:
        signal = "إشارة <b>شراء</b>"
    elif rsi >= 60:
        signal = "إشارة <b>بيع</b>"
    else:
        signal = "لا توجد إشارة واضحة حالياً"

    message = f"""
<b>تنبيه RSI</b>
العملة: <b>{symbol}</b>
RSI: <b>{rsi}</b>
السعر الحالي: <b>{price}$</b>
الإشارة: {signal}
التاريخ: {date}
الوقت: {time}
"""

    send_telegram_message(message)
    return 'OK', 200

if name == '__main__':
    app.run(debug=True)
