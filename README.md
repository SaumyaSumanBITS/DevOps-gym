## ACEest Fitness & Gym Application

A Flask-based web application with REST APIs for gym client management, integrated with a complete DevOps CI/CD pipeline using GitHub Actions, Jenkins, and Docker.

---

## Overview

This project demonstrates the development and deployment of a fitness management application using modern DevOps practices. It includes a web interface, RESTful APIs, automated testing, containerization, and continuous integration and deployment pipelines.

---

## Features

* User authentication (login system using Flask templates)
* Dashboard interface
* RESTful API with full CRUD operations
* BMI calculation endpoint
* SQLite database integration
* Automated testing using Pytest
* Docker-based containerization
* CI/CD pipeline using GitHub Actions and Jenkins

---

## Technology Stack

* Backend: Python (Flask)
* Database: SQLite
* Testing: Pytest
* Containerization: Docker
* CI/CD: GitHub Actions, Jenkins
* Version Control: Git and GitHub

---

## API Endpoints

| Method | Endpoint          | Description              |
| ------ | ----------------- | ------------------------ |
| GET    | /api              | API home                 |
| POST   | /api/clients      | Add a new client         |
| GET    | /api/clients      | Retrieve all clients     |
| GET    | /api/clients/<id> | Retrieve a single client |
| PUT    | /api/clients/<id> | Update client details    |
| DELETE | /api/clients/<id> | Delete a client          |
| GET    | /api/bmi          | Calculate BMI            |
| GET    | /health           | Health check endpoint    |

---

## Running the Application

### Using Python

```bash
pip install -r requirements.txt
python app.py
```

---

### Using Docker

```bash
docker build -t aceest-gym .
docker run -d -p 5000:5000 aceest-gym
```

Access the application at:

```
http://localhost:5000
```

---

## Running Tests

```bash
pytest
```

---

## CI/CD Pipeline

### GitHub Actions

* Automatically triggered on every push and pull request
* Installs dependencies
* Executes test cases using Pytest
* Builds Docker image

### Jenkins

* Pulls latest code from GitHub repository
* Installs dependencies
* Runs test suite (acts as quality gate)
* Builds Docker image
* Deploys application as a container

---

## Deployment

The application was successfully deployed and tested in two environments:

* Local development environment
* AWS EC2 virtual machine

The same codebase and pipeline were used without modification, demonstrating portability and consistency across environments.

---

## Screenshots (To be included in submission)

* GitHub Actions pipeline execution
* Jenkins build and console output
* Application running locally
* Application running on AWS EC2
* API responses for GET, POST, PUT, DELETE, and health endpoints

---

## Conclusion

This project demonstrates the implementation of a complete DevOps lifecycle, including application development, automated testing, containerization, and deployment across multiple environments. It highlights the use of CI/CD pipelines to ensure code quality, reliability, and scalability.

---

