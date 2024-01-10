import requests
import settings
import json
import base64

def get_token():
    auth_string = settings.spotify_client_id + ':' + settings.spotify_client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token


if __name__ == '__main__':
    token = get_token()
    print(token)