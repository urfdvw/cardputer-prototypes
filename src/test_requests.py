
import ipaddress
import socketpool
import ssl
import wifi

import adafruit_requests

import secrets

#%% connect to wifi
print("Available WiFi networks:")
for network in wifi.radio.start_scanning_networks():
    print("\t%s\t\tRSSI: %d\tChannel: %d" % (str(network.ssid, "utf-8"),
            network.rssi, network.channel))
wifi.radio.stop_scanning_networks()

print("Connecting to %s"%secrets.wifi["ssid"])
wifi.radio.connect(secrets.wifi["ssid"], secrets.wifi["password"])
print("Connected to %s!"%secrets.wifi["ssid"])

#%% status
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
print("My IP address is", wifi.radio.ipv4_address)

#%% ping test
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

#%% init requests
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

#%% fetch text
TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
print("Fetching text from", TEXT_URL)
response = requests.get(TEXT_URL)
print("-" * 8)
print(response.text)
print("-" * 8)
input('Enter to continue')

#%% fetch json
JSON_QUOTES_URL = "https://www.adafruit.com/api/quotes.php"
print("Fetching json from", JSON_QUOTES_URL)
response = requests.get(JSON_QUOTES_URL)
print("-" * 8)
print(response.json())
print("-" * 8)
input('Enter to continue')



# fetch and parsing json
JSON_STARS_URL = "https://api.github.com/repos/adafruit/circuitpython"
print("Fetching and parsing json from", JSON_STARS_URL)
response = requests.get(JSON_STARS_URL)
print("-" * 8)
print("CircuitPython GitHub Stars", response.json()["stargazers_count"])
print("-" * 8)
input('Enter to continue')