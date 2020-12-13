from flask import Flask
from flask import jsonify
from devices.dht import DhtDevice
from time import sleep

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/stream')
def stream():
    pass


@app.route('/dht/temperature')
def dht_temperature():
    while True:
        try:
            dht = DhtDevice()
            celsius = dht.get_celsius()
            fahrenheit = dht.get_fahrenheit()
            break
        except:
            sleep(1)

    return jsonify(
        celsius=celsius,
        fahrenheit=fahrenheit,
    )


@app.route('/dht/humidity')
def dht_humidity():
    while True:
        try:
            dht = DhtDevice()
            humidity = dht.get_humidity()
            break
        except:
            sleep(1)

    return jsonify(
        humidity=humidity
    )


if __name__ == '__main__':
    app.run()
