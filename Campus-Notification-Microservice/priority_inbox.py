import requests
from datetime import datetime
from logger import logger

API_URL = "http://4.224.186.213/evaluation-service/notifications"

# Replace with actual token if provided
TOKEN = ""

headers = {
    "Authorization": f"Bearer {TOKEN}"
}


def get_notifications():

    try:

        logger.info("Fetching notifications")

        response = requests.get(
            API_URL,
            headers=headers,
            timeout=10
        )

        logger.info(f"Status Code : {response.status_code}")

        if response.status_code == 200:

            data = response.json()

            return data.get("notifications", [])

        else:

            logger.error(response.text)

            print("Status Code :", response.status_code)
            print(response.text)

            return []

    except Exception as e:

        logger.error(str(e))

        print(e)

        return []


def calculate_priority(notification):

    weights = {
        "Placement": 30,
        "Result": 20,
        "Event": 10
    }

    type_score = weights.get(
        notification["Type"],
        5
    )

    notification_time = datetime.strptime(
        notification["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    current_time = datetime.now()

    minutes_old = (
        current_time -
        notification_time
    ).total_seconds() / 60

    recency_score = max(
        0,
        20 - int(minutes_old)
    )

    return type_score + recency_score


def get_top_notifications(notifications):

    for notification in notifications:

        notification["priority"] = calculate_priority(notification)

    notifications.sort(
        key=lambda x: x["priority"],
        reverse=True
    )

    return notifications[:10]


def display_notifications(notifications):

    print("\nTOP PRIORITY NOTIFICATIONS\n")

    if len(notifications) == 0:

        print("No notifications found.")

        return

    for index, notification in enumerate(
        notifications,
        start=1
    ):

        print("-" * 50)

        print("Rank :", index)

        print("ID :", notification["ID"])

        print("Type :", notification["Type"])

        print("Message :", notification["Message"])

        print("Timestamp :", notification["Timestamp"])

        print("Priority Score :", notification["priority"])


def fetch_and_display():

    notifications = get_notifications()

    top = get_top_notifications(
        notifications
    )

    display_notifications(top)