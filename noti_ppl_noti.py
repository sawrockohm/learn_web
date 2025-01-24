import requests
import json
from datetime import datetime
import google.auth.transport.requests
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/firebase.messaging"]


def _get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.

    :return: Access token.
    """
    credentials = service_account.Credentials.from_service_account_file(
        "service-account_ppl_noti.json", scopes=SCOPES
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials.token


headers = {
    "Authorization": "Bearer " + _get_access_token(),
    "Content-Type": "application/json; UTF-8",
}

map_alarm = {
    "1": {
        "channel_id": "high_importance_channel_new",
        "sound": "alarm.caf",
    },
}

index_map = "1"

dt = datetime.now()
ts = int(str(datetime.timestamp(dt)).split(".")[0])

body = {
    "message": {
        "token": "eCsUKObg1UomtL4FMb9RZH:APA91bGHePnLFK3IxyJLn5KYBLgRqfFxjXhLL21leJbT3XCZc0d7nxsYkNlKkmO_vlRXOtDCE3-eZGwXTOnbHBWmayJwWYn-nIpYgVImnpiyHUMF97ob23M",
        "notification": {
            "body": "lnwza",
            "title": "lnwza 123",
        },
        "apns": {
            "payload": {
                "route": "/home",
                "aps": {
                    # "sound": map_alarm[index_map]['sound'],
                },
            },
        },
        "android": {
            "notification": {
                "click_action": "TOP_STORY_ACTIVITY",
                "title": "xxx",
                "body": "zzz",
                "channel_id": map_alarm[index_map]["channel_id"],
            }
        },
        "data": {
            "route": "/home"
            # "sound" : map_alarm[index_map]['sound'],
        },
    }
}
print(
    map_alarm[index_map]["sound"],
)

response = requests.post(
    "https://fcm.googleapis.com/v1/projects/ppl-noti/messages:send",
    headers=headers,
    data=json.dumps(body),
)
print(response)
data = response.json()
print(data)
