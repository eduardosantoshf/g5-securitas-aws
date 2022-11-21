import requests

def trigger_notification (camera_id):
    try:    
        print("make a request to the notification api")        
        return True
    except Exception as e:
        return False