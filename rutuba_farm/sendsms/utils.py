import requests
from django.conf import settings
import logging
logger = logging.getLogger(__name__)



def send_sms(phone_number, message):
    headers = {
        "Authorization": f"Basic {settings.SMS_LEOPARD_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "source": "AkiraChix",
        "message": message,
        "destination": [{"number": phone_number}],
    }
    try:
        logger.info(f"Sending SMS with payload: {payload}")
        response = requests.post(
            settings.SMS_LEOPARD_API_URL, json=payload, headers=headers
        )
        logger.info(f"Response received: {response.status_code} - {response.text}")
        response_data = response.json()
        if response.status_code == 201 and response_data.get("success"):
            logger.info(f"SMS sent successfully: {response_data}")
            return response_data
        else:
            logger.error(f"Failed to send SMS: {response_data}")
            return None
    except requests.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return None






