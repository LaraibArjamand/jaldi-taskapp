## Setup Guide

#### Clone Taskapp Repository
1. Clone this repository to your local machine:
    `git clone https://github.com/your-username/taskapp.git`
2. Navigate to the project directory:
    `cd taskapp`


#### Building and Running the App
1. Build the project and install dependencies:
    `docker-compose build`
2. Once the build is successful, start the application:
    `docker-compose up -d`

#### Running Tests
##### Option 1: From the tests directory
1. To run tests, navigate to the tests directory:
    `cd tests`
2. Run pytest:
    `pytest`
##### Option 1: From the root directory
1. Alternatively, you can run tests directly from the root directory:
    `pytest`

These steps will set up the api, install the required dependencies and run the tests. Access the api at http://localhost:5000 once the setup is complete. 
#### Endpoint Details:
#### Users
* **POST /users/register** : User registration
* **POST /users/login** : User login 
* **POST /users/logout** : User logout

#### Task
* **GET /tasks** : Get list of tasks 
* **POST /tasks** : Create new task
* **GET /tasks/<task_id>** :Retrieve task with id "task_id"
* **PATCH /tasks/<task_id>** : Update exisiting task with id "task_id"
* **DELETE /tasks/<task_id>** : Delete task with id "task_id"

