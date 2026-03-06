# ACEest Fitness DevOps Pipeline

This project implements a simple gym management web application using Flask and demonstrates DevOps practices including GitHub Actions CI/CD and Docker containerization.

## Features

- Login page
- Gym dashboard
- Automated testing using Pytest
- Docker containerization
- CI pipeline using GitHub Actions
- Jenkins build integration

## Run Application

python app.py

Open:
http://localhost:5000

## Run Tests

pytest

## Docker

Build image:

docker build -t aceest-gym .

Run container:

docker run -p 5000:5000 aceest-gym

## CI/CD Pipeline

GitHub Actions automatically runs tests and builds the Docker image on every push.

Jenkins pulls the repository and performs the build for additional validation.
