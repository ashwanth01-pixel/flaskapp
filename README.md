# Repository Summary

Based on the provided repository context, particularly the app.py file, this appears to be a simple Flask-based backend application designed to run on Kubernetes. Here's a summary of the main components and purpose:

1. Purpose:
   The repository contains a basic web application that serves as a backend, likely part of a larger system called "Ashapp".

2. Main components:

   a. Flask Application (app.py):
   - Creates a Flask web application
   - Sets up logging
   - Defines a single route ("/") that returns a greeting message
   - Configures the application to run on host 0.0.0.0 and port 5000
   - Ensures debug mode is disabled in production

   b. Kubernetes Deployment (deployment.yaml, not shown in the main context but mentioned):
   - Likely defines how the application should be deployed on a Kubernetes cluster

   c. Kubernetes Service (service.yaml, not shown in the main context but mentioned):
   - Probably exposes the application to the network, making it accessible

   d. CI/CD Pipeline (pipeline.yml, not shown in the main context but mentioned):
   - Likely defines the steps for building, testing, and deploying the application

   e. Dependencies (requirements.txt):
   - Lists the Python packages required for the application, including Flask

The application is designed with security and production readiness in mind, as evidenced by the multiple comments ensuring that debug mode is disabled in production. It also uses environment variables for configuration, allowing for flexible deployment across different environments.

Reference: This summary is primarily based on the contents of the [FILE: app.py].

## Tech Stack
Based on the provided repository context, the main tech stack includes:

1. Python: The primary programming language used, as evident from the Flask application in app.py.

2. Flask: A Python web framework used for the backend application, specified in requirements.txt and used in app.py.

3. Docker: Used for containerization, as seen in the Docker-related steps in pipeline.yml.

4. Kubernetes: Used for orchestration and deployment, as shown in deployment.yaml and service.yaml files.

5. GitHub Actions: The CI/CD pipeline is implemented using GitHub Actions, as seen in pipeline.yml.

6. pytest: Used for running unit tests, as shown in the pipeline.yml file.

7. flake8: A linting tool used for code quality checks, also seen in pipeline.yml.

8. kubectl: The Kubernetes command-line tool, used in pipeline.yml for applying manifests and managing deployments.

These technologies form the core of the application's development, testing, containerization, and deployment processes.

## Workflow
Here's a detailed developer guide for this repository:

1. Project Overview:
This repository contains a Flask-based backend application deployed on Kubernetes. The main application is defined in `app.py`, with deployment configurations in `pipeline.yml` and `deployment.yaml`.

2. Application (app.py):
- The application is a simple Flask server that returns a "Hello" message.
- It uses logging to record when the home route is accessed.
- The server runs on host '0.0.0.0' and port 5000.
- Debug mode is disabled for production safety.

3. Dependencies (requirements.txt):
- The project uses Flask version 2.3.2.
- Ensure you install dependencies using: `pip install -r requirements.txt`

4. Docker Configuration (Dockerfile):
- Uses Python 3.9-slim as the base image.
- Copies requirements and installs dependencies.
- Exposes port 5000.
- Runs the application using `python -u app.py`.

5. Kubernetes Deployment (deployment.yaml):
- Deploys 2 replicas of the application.
- Sets resource limits and requests for CPU and memory.
- Includes readiness and liveness probes for health checking.
- Uses rolling update strategy for deployments.
- Sets environment variables for Flask and Python.

6. CI/CD Pipeline (pipeline.yml):
- Runs on self-hosted runners.
- Performs linting with flake8 and runs unit tests with pytest.
- Builds and pushes Docker image to Docker Hub.
- Applies Kubernetes manifests.
- Verifies deployment and tests the application.
- Uses GitHub Secrets for Docker Hub credentials.

7. Development Workflow:
a. Make changes to the application code in `app.py`.
b. Update `requirements.txt` if new dependencies are added.
c. Run linting and tests locally before committing.
d. Push changes to GitHub to trigger the CI/CD pipeline.
e. The pipeline will build, test, and deploy the application.

8. Deployment:
- The application is deployed to a Kubernetes cluster.
- The service is exposed via NodePort on port 30080.
- After deployment, the application URL will be printed in the pipeline output.

9. Monitoring and Debugging:
- Use `kubectl` commands to check pod status and logs.
- The application logs INFO level messages for monitoring.

10. Best Practices:
- Keep Flask debug mode disabled in production (as set in `app.py`).
- Use specific versions for dependencies (as done in `requirements.txt`).
- Utilize resource limits and requests in Kubernetes deployments (as set in `deployment.yaml`).
- Implement health checks using readiness and liveness probes (present in `deployment.yaml`).

11. Security:
- Sensitive information like Docker Hub credentials are stored as GitHub Secrets.
- The Docker image is versioned using Git SHA for better traceability.

This guide provides an overview of the project structure, deployment process, and best practices implemented in the repository. Developers should familiarize themselves with Flask, Docker, and Kubernetes concepts to effectively work with this project.
