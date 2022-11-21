import requests

def trigger_notification (camera_id):
    try:    
        print("Request to Notification API")
        return True
    except Exception as e:
        return False