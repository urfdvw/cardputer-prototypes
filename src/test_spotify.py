import binascii
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



client_id = secrets.spotify['client_id']
client_secret = secrets.spotify['client_secret']

auth_string = f"{client_id}:{client_secret}"
auth_bytes = auth_string.encode('utf-8')
# b2a_base64 returns bytes that include a newline at the end
auth_base64 = binascii.b2a_base64(auth_bytes).strip().decode("utf-8")

url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {auth_base64}'
}
data = {
    'grant_type': 'client_credentials'
}


# Make the POST request
response = requests.post(url, headers=headers, data=data)

# Check the response
if response.status_code == 200:
    body = response.json()
    TOKEN = body.get('access_token')
    print("Access token:", TOKEN)
else:
    print("Request failed with status code:", response.status_code)
    print("Response body:", response.text)

SPOTIFY_TRACK_URL = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'

response = requests.get(
    SPOTIFY_TRACK_URL,
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    },
)

print(response.json())