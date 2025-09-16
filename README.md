# Repository Summary

Based on the provided repository context, particularly the app.py file, this repository appears to be for a simple Flask-based web application designed to run on Kubernetes. Here's a summary of its purpose and main components:

1. Purpose:
The repository contains a basic backend web application that serves a "Hello" message when accessed. It's designed to be containerized and deployed on a Kubernetes cluster.

2. Main components:

a. Flask Application (app.py):
- This is the core of the application, using the Flask framework.
- It sets up a single route ("/") that returns a greeting message.
- The application is configured to run on host '0.0.0.0' and port 5000.
- Debug mode is explicitly set to False for production safety.
- Logging is set up to record when the home route is accessed.

b. Kubernetes Deployment (deployment.yaml):
- While not fully visible in the provided context, this file likely contains the Kubernetes deployment configuration for the application.

c. Kubernetes Service (service.yaml):
- Exposes the application as a NodePort service on port 30080.

d. CI/CD Pipeline (pipeline.yml):
- Though not fully visible, this file likely contains the CI/CD configuration for building, testing, and deploying the application.

e. Dependencies (requirements.txt):
- Specifies the exact version of Flask (2.3.2) required for the application.

The repository demonstrates best practices such as disabling debug mode in production, using environment variables for configuration, and pinning dependency versions. It's structured to support containerization and Kubernetes deployment, suggesting it's intended for a scalable, cloud-native environment.

## Tech Stack
Based on the repository context provided, the main tech stack includes:

1. Python: This is the primary programming language used, as evidenced by the Flask application in app.py.

2. Flask: A Python web framework used for the backend application, as seen in app.py and requirements.txt (flask==2.3.2).

3. Docker: Used for containerization, as indicated by the Docker-related steps in pipeline.yml.

4. Kubernetes: Used for container orchestration and deployment, as shown in deployment.yaml and service.yaml.

5. GitHub Actions: The CI/CD pipeline is implemented using GitHub Actions, as seen in pipeline.yml.

6. pytest: Used for running unit tests, as mentioned in pipeline.yml.

7. flake8: Used for linting Python code, as seen in pipeline.yml.

8. kubectl: The Kubernetes command-line tool, used in pipeline.yml for applying Kubernetes manifests.

These components form the core of the tech stack used in this project, covering the application framework, containerization, orchestration, and CI/CD pipeline.

## Workflow
Here's a detailed developer guide for this repository:

1. Project Overview:
This repository contains a simple Flask-based backend application that's containerized and deployed to Kubernetes. The main application file is `app.py`, which serves a basic "Hello" message.

2. Setup and Installation:
   a. Clone the repository
   b. Install dependencies:
      - Use `pip install -r requirements.txt` to install the required packages (flask==2.3.2) as specified in `requirements.txt`.

3. Local Development:
   - Run the Flask application locally using `python app.py`
   - The app will run on `http://localhost:5000`
   - Note: Debug mode is disabled in production (see `app.py`)

4. Docker:
   - The `Dockerfile` specifies how to build the Docker image:
     - Uses Python 3.9-slim as the base image
     - Copies and installs requirements
     - Copies the application code
     - Exposes port 5000
     - Runs the app using `python -u app.py`
   - Build the Docker image: `docker build -t ashwanth01/ashapp-backend:latest .`
   - Run the container: `docker run -p 5000:5000 ashwanth01/ashapp-backend:latest`

5. CI/CD Pipeline:
   The `pipeline.yml` file defines the GitHub Actions workflow:
   - Runs on self-hosted runners
   - Steps include:
     a. Linting with flake8
     b. Running unit tests with pytest
     c. Building and pushing the Docker image to Docker Hub
     d. Applying Kubernetes manifests
     e. Verifying the deployment
     f. Testing the application
   - Note: The pipeline uses GitHub Secrets for Docker Hub credentials

6. Kubernetes Deployment:
   The `deployment.yaml` file defines the Kubernetes deployment:
   - Deploys 2 replicas of the application
   - Sets resource limits and requests
   - Configures readiness and liveness probes
   - Uses a rolling update strategy

7. Best Practices and Notes:
   - The Flask version is pinned to 2.3.2 in `requirements.txt` for consistency
   - Debug mode is disabled in production in `app.py`
   - The Kubernetes deployment includes resource limits and health checks
   - The CI/CD pipeline includes linting and testing steps before deployment
   - Docker image tags use both 'latest' and the Git SHA for versioning

8. Troubleshooting:
   - Check Kubernetes logs: `kubectl logs <pod-name>`
   - Verify service: `kubectl get services`
   - Check deployment status: `kubectl rollout status deployment/ashapp-backend`

This guide provides an overview of the project structure, setup instructions, and key aspects of the development and deployment process based on the files in the repository.
