from flask import Flask, render_template, jsonify
import json
from waitress import serve


app = Flask(__name__)

@app.route('/')
def home():
    import requests
    # שליחת בקשה ל-API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=kaspa&vs_currencies=ils"
    response = requests.get(url)
    data = response.json()

    # חישוב הערך
    price_per_kaspa = data["kaspa"]["ils"]
    quantity = 350
    total_in_ils = price_per_kaspa * quantity

    return str(total_in_ils)



# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)

