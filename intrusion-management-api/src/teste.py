import requests

with open(f"../videos/people-detection.mp4", 'rb') as f:
    response = requests.post('http://localhost:8000/intrusion-management-api/cameras/store-video', files={'file': f})