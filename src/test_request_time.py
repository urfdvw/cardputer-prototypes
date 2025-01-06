import ipaddress
import socketpool
import ssl
import wifi
# installed module
import adafruit_requests
# custom module
import secrets

wifi.radio.connect(secrets.wifi["ssid"], secrets.wifi["password"])
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

JSON_TIME_URL = "http://worldtimeapi.org/api/timezone/America/New_York"
response = requests.get(JSON_TIME_URL)
print("New York Time: ", response.json()["datetime"])