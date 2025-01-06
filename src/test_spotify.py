import ipaddress
import socketpool
import ssl
import wifi
# installed module
import adafruit_requests
# custom module
from secrets import secrets

wifi.radio.connect(secrets["ssid"], secrets["password"])
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())



SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/***/playlists'
TOKEN = '***'

response = requests.post(
    SPOTIFY_CREATE_PLAYLIST_URL,
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    },
    json={
        "name": "ESP32S3",
        "public": False
    }
)

print(response.json())