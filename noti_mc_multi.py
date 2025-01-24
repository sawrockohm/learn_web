import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging


def send_push_notification(server_key):
    cred = credentials.Certificate(server_key)
    firebase_admin.initialize_app(cred)

    message = messaging.Message(
        notification=messaging.Notification(
            title="Topic Notification Title",  # เปลี่ยน
            body="This is a message sent to all devices subscribed to the topic.",  # เปลี่ยน
        ),
        topic="newscc",  # ห้ามเปลี่ยน
    )

    response = messaging.send(message)
    print("Successfully sent notification:", response)


# Replace with the path to your service account key JSON file
server_key = "service-account_mashares.json"


# Send push notification
send_push_notification(server_key)
