import board
import adafruit_dht


class DhtDevice:
    # Init the dht device with pin connected:
    device = adafruit_dht.DHT22(board.D4)

    def get_celsius(self):
        return "{:.1f}".format(self.device.temperature) + ' C'

    def get_fahrenheit(self):
        return "{:.1f}".format(self.device.temperature * (9 / 5) + 32) + ' F'

    def get_humidity(self):
        return str(self.device.humidity) + '%'
