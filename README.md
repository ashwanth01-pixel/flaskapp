# Repository Summary

Based on the provided repository context, particularly the app.py file, this repository appears to be for a simple Flask-based backend application intended to run on Kubernetes. Here's a summary of the main components and purpose:

1. Purpose:
   The repository contains a basic Flask web application that serves as a backend service, likely part of a larger system or microservices architecture.

2. Main components:

   a. Flask Application (app.py):
      - Creates a Flask app with a single route ("/")
      - Implements basic logging
      - Ensures debug mode is disabled for production use
      - Runs the app on host 0.0.0.0 and port 5000

   b. Deployment Configuration (deployment.yaml, not shown in the main context):
      - Likely contains Kubernetes deployment specifications for the application

   c. Service Configuration (service.yaml, not shown in the main context):
      - Probably defines how the application is exposed within the Kubernetes cluster

   d. Dependencies (requirements.txt, not shown in the main context):
      - Lists the Python package dependencies, including Flask

   e. CI/CD Pipeline (pipeline.yml, not shown in the main context):
      - Likely contains the continuous integration and deployment configuration

The app.py file demonstrates a focus on security and production readiness, with multiple comments emphasizing the importance of disabling debug mode in production. The application is designed to run in a containerized environment, specifically on Kubernetes, as evidenced by the message returned by the home route: "Hello from Ashapp Backend running on Kubernetes!"

## Tech Stack
Based on the repository context provided, the main tech stack includes:

1. Python: The primary programming language used, as evidenced by the Flask application in app.py.

2. Flask: A Python web framework used for the backend application, specified in requirements.txt and used in app.py.

3. Docker: Used for containerization, as seen in the Docker image building and pushing steps in pipeline.yml.

4. Kubernetes: Used for orchestration and deployment, as shown in deployment.yaml and service.yaml files.

5. GitHub Actions: Implied by the presence of pipeline.yml, which defines a CI/CD workflow.

6. pytest: A testing framework for Python, used in the pipeline as seen in pipeline.yml.

7. flake8: A linting tool for Python, used in the pipeline as seen in pipeline.yml.

These technologies form the core of the application's development, testing, and deployment pipeline.

## Workflow
Here's a detailed developer guide for this repository:

1. Project Overview:
This repository contains a Flask-based backend application designed to run on Kubernetes. The main application is defined in `app.py`, with deployment configurations in `deployment.yaml` and `pipeline.yml`.

2. Application (app.py):
- The application is a simple Flask server that returns a "Hello" message.
- It uses logging to record when the home route is accessed.
- The app runs on host '0.0.0.0' and port 5000.
- Debug mode is disabled for production use (app.py).

3. Dependencies (requirements.txt):
- The project uses Flask version 2.3.2.
- Ensure you install dependencies using: `pip install -r requirements.txt`

4. Docker Configuration (Dockerfile):
- Uses Python 3.9 slim image as the base.
- Copies requirements and installs dependencies.
- Exposes port 5000.
- Runs the app using `python -u app.py`.

5. Kubernetes Deployment (deployment.yaml):
- Deploys 2 replicas of the application.
- Sets resource limits and requests for CPU and memory.
- Includes readiness and liveness probes for health checking.
- Uses a rolling update strategy for deployments.

6. CI/CD Pipeline (pipeline.yml):
- Runs on self-hosted runners.
- Performs linting with flake8 and runs unit tests with pytest.
- Builds and pushes a Docker image to Docker Hub.
- Applies Kubernetes manifests for deployment and service.
- Verifies deployment and tests the application.

7. Development Workflow:
a. Make changes to the application code in `app.py`.
b. Update `requirements.txt` if new dependencies are added.
c. Run linting and tests locally before committing.
d. Push changes to trigger the CI/CD pipeline.

8. Deployment:
- The pipeline automatically builds, tests, and deploys the application.
- It uses Git SHA for Docker image tagging for versioning.
- Kubernetes manifests are applied automatically.

9. Monitoring and Debugging:
- The application logs are configured for INFO level.
- Kubernetes probes are set up for monitoring application health.

10. Security Considerations:
- Docker Hub credentials are stored as GitHub Secrets.
- Debug mode is disabled in production.

11. Best Practices:
- Use specific versions for dependencies (as seen in requirements.txt).
- Implement proper resource management in Kubernetes (as seen in deployment.yaml).
- Utilize rolling updates for zero-downtime deployments.

This guide provides an overview of the repository structure and key components for developers working on this project.
