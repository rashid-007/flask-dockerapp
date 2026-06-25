<<<<<<< HEAD
# flask-dockerapp
NA
=======
# Flask Dockerized App

A simple Python Flask application containerized with Docker and pushed to DockerHub.

## Tech Stack
- Python 3.12
- Flask 3.1.3
- Docker

## Project Structure
flask-dockerapp/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md

## API Endpoints
| Endpoint  | Method | Response                        |
|-----------|--------|---------------------------------|
| /         | GET    | Welcome message + status        |
| /health   | GET    | App status + uptime             |

## Run Locally
```bash
python3 app.py
```

## Run with Docker
```bash
# Pull from DockerHub
docker pull rashid-007/flask-dockerapp:latest

# Run the container
docker run -d -p 5000:5000 flask-dockerapp
```

## DockerHub
https://hub.docker.com/r/rashid-007/flask-dockerapp
>>>>>>> 51fe78b (My flask dockerized application)
