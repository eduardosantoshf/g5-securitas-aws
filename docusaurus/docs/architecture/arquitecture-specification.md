---
sidebar_position: 2
---

# Architecture Specification

More detailed information about the architecture of the Intrusion Detection System, can be found in the following table:

| Component      | Description |
| ----------- | ----------- |
| Human Detection Module (HDM)      | This module analyzes the frames sent by the security cameras, to detect if there is a human on-site or not       |
| In-memory Database   | This database should be used by the HDM to evaluate if there are N consecutive frames where a human was detected        |
| Video Clips Archive   | The Video Clips Archive should store the video recordings of the intrusions. The Intrusion Management API should request the video clips from the cameras and they should be stored in AWS S3        |
| Intrusion Management API   | This API will be used to act whenever an intrusion is detected. It will get the intrusion video clips from the cameras, activate the alarms, and trigger a new notification in the Notifications API        |
| Sites Management API   | This API should be used to track all properties being monitored, along with all the logic regarding the “owners” of each property. It should make available endpoints for the creation/update/deletion of new properties, creation/update/deletion of new property owners, etc...        |
| Notifications API   | This API is responsible for informing the property owners and the police whenever an intrusion is detected        |
| Management Web UI   | Via this graphical interface, the platform’s admins should be able to see all properties being monitored, the intrusions that took place, a list of each property cameras and sensors (also their health), and all data regarding the platform’s clients. Basically, this UI is used to manage the entire platform    |
| Client’s UI   | This UI is solely offered to the owners of the properties. Through it, the property owners should be able to see a listing of all cameras, sensors, intrusion events, etc. Besides this, the property owners should be able to update their information through this UI        |
| Service Discovery   | Every time a new camera or sensor is added to a property, the camera/sensor should register itself in the Service Registry, listing how it can be accessed        |
| Identity Provider (IDP)   | The IDP provides authentication and authorization mechanisms for all the aforementioned APIs and UIs        |
| Logs Monitor   | All system logs should be centralized in this entity        |
| ParaMetrics Monitorgraph   | All system metrics should be centralized in this entity        |