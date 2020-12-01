import board
import adafruit_dht


class DhtDevice:
    # Init the dht device with pin connected:
    device = adafruit_dht.DHT22(board.D4)


    def get_celsius(self):
        return self.device.temperature


    def get_fahrenheit(self):
        return self.device.temperature * (9 / 5) + 32


    def get_humidity(self):
        return self.device.humidity
