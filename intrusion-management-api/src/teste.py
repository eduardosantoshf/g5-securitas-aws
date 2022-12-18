import requests

with open(f"../videos/download-video.mp4", 'rb') as f:
    response = requests.post('http://localhost:8000/intrusion-management-api/cameras/store-video', files={'file': f})
    print(response.status_code)
    print(response.text)