---
sidebar_position: 2
---

# Management Web UI

The [React](https://reactjs.org/) was the tool chosen to develop the Management Web UI.

## User story "List all users"
In order to implement the "List all users" user story, we create a "Users" component.
In this component we develop code from a table, which contains information from all users (user data is still static).

## User story "Add/remove users"
In the realization of the user story "Add/remove users", we work on the component previously created, the component "Users".
We implemented a button at the top of the page with the label "Add". We create a Popup, which appears when we click on the "Add" button, with a suitable form for creating a user.  
In each row of the users table (in each user) we create an "Eliminate" button, and a Popup associated with the button that works as confirmation of the user's elimination. 