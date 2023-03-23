from flask import Flask, request
from pymongo import MongoClient
import datetime
from MEXC import account_data
account_data()


app = Flask(__name__)
conn = MongoClient()
db = conn.cryptoalerts
collection = db.alerts


@app.route('/alert', methods=['GET', 'POST'])
def test():
    if request.json.get(
            'message') == 'Confirmation message from Cryptocurrency Alerting!':
        collection.insert_one({
            "_type": "initialize",
            "message": "Confirmation message from Cryptocurrency Alerting!"
        })
        return {'status': 'success'}
    collection.insert_one({
        "_type": request.json.get('type'),
        "message": request.json.get('message'),
                          "currency": request.json.get('currency'),
                          "direction": request.json.get('direction'),
                          "percent": request.json.get('percent'),
                          "window": request.json.get('window'),
                          "exchange": request.json.get('exchange'),
                          "alert_condition_id": request.json.get(
            'alert_condition_id')
    })
    return {'status': 'success'}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)
