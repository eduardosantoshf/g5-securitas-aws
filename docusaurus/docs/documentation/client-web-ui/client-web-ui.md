---
sidebar_position: 1
---

# Front-end

The [React](https://reactjs.org/) was the tool chosen to develop the Client Web UI.

First we created two pages, one to list cameras and another to list the client's alarms, so you can see their characteristics.
For this, we implemented a component "Cameras" and another component "Alarms". In each component we develop code from a table, which contains information about the cameras/alarms.
![](./img/listCameras.png)
![](./img/listAlarms.png)

We perform the functionality of adding and removing a camera on the cameras page, and on the alarms page we implement the functionality of adding and removing an alarm.

On the cameras page, we developed a button at the top of the page with the label "Add". We create a Popup, which appears when we click on the "Add" button, with a form suitable for creating a camera.
![](./img/addCameras.png)
On the alarms page we did the same thing for the alarms.
![](./img/addAlarms.png)

On the cameras page, in each row of the camera table (in each camera) we create a "Delete" button, and a Popup associated with the button that works as confirmation of the camera's deletion.
![](./img/deleteCameras.png)
We did the same for the alarms page. 
![](./img/deleteAlarms.png)