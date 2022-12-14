---
sidebar_position: 1
---

# Introduction

This API will be used to act whenever an intrusion is detected. It will get the intrusion video clips from the cameras, activate the alarms, and trigger a new notification in the Notifications API.

:::note

* To interact with the API in a local environment, you need to create a virtual enviroment and install the dependencies. To do so, execute the following commands in the root folder of the API:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

:::

## Video-Clips
The communicaiton between the Intrusion Management API and the Cameras will be done through a message broker, when the API asks the Camera to send the video clips, and then the Camera will send the video clips through HTTP to the API. We choose this approach because, as all cameras are subcribed to the same topic, all receive the information, but only one will process it, and the rest will ignore it. It is simpler that have a API for the cameras.

After the video clips are received, it will be stored in a S3 bucket, this communication is made with the **boto3** library. The video clips will be stored in the S3 bucket with the following structure:

```
intrusion-client_id-camera_id-timestamp_intrusion.mp4
```

Where:
- client_id: The id of the client that owns the camera.
- camera_id: The id of the camera that detected the intrusion.
- timestamp_intrusion: The timestamp when the intrusion was detected.


## Alarms

When the Intrusion-Management API receives the information about a intrusion, it will activate the alarms. This communication will be done via message broker, and the alarms will change its status to **active**.

## Notifications

When the Intrusion-Management API receives the information about a intrusion, it will trigger a new notification in the Notifications API.
