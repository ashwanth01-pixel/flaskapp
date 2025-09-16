Here's a detailed developer guide for this repository:

1. Project Overview:
This repository contains a Flask-based backend application that is containerized and deployed to Kubernetes. The main application file is `app.py`, which serves a simple "Hello" message.

2. Development Environment Setup:
- Ensure Python 3.9 is installed on your system.
- Install the required dependencies by running `pip install -r requirements.txt`.
- The main dependency is Flask, pinned to version 2.3.2 (requirements.txt).

3. Application Structure:
- `app.py`: Contains the main Flask application code.
- `Dockerfile`: Used to build the Docker image for the application.
- `requirements.txt`: Lists the Python dependencies.
- `pipeline.yml`: GitHub Actions workflow for CI/CD.
- `deployment.yaml`: Kubernetes deployment configuration.

4. Local Development:
- Run the application locally using `python app.py`.
- The app will be accessible at `http://localhost:5000`.
- Note: Debug mode is disabled for security reasons (app.py).

5. Docker Build:
- Use the provided Dockerfile to build the image:
  `docker build -t ashwanth01/ashapp-backend:latest .`
- The Dockerfile uses a Python 3.9 slim base image and copies the application files into the container.

6. Continuous Integration/Continuous Deployment (CI/CD):
- The `pipeline.yml` file defines the GitHub Actions workflow.
- It includes steps for linting (flake8), running unit tests (pytest), building and pushing the Docker image, and deploying to Kubernetes.
- The workflow uses GitHub Secrets for sensitive information like Docker Hub credentials.

7. Kubernetes Deployment:
- The `deployment.yaml` file defines the Kubernetes deployment configuration.
- It specifies 2 replicas of the application.
- Resource limits and requests are set to ensure proper resource allocation.
- Readiness and liveness probes are configured for health checking.
- A rolling update strategy is implemented for smooth updates.

8. Best Practices and Notes:
- The Flask version is pinned to 2.3.2 for consistency (requirements.txt).
- Debug mode is disabled in production for security (app.py).
- Docker image tags use both 'latest' and the Git SHA for versioning (pipeline.yml).
- Sensitive information is stored in GitHub Secrets (pipeline.yml).
- The pipeline includes linting and unit testing before building and deploying (pipeline.yml).
- Kubernetes deployment includes resource limits, health checks, and a rolling update strategy (deployment.yaml).

9. Deployment and Testing:
- The CI/CD pipeline handles deployment to Kubernetes.
- After deployment, the application should be accessible via the NodePort service at `http://<NODE_IP>:30080`.
- The pipeline includes a step to verify the deployment and test the application.

10. Cleanup:
- In case of deployment failure, the pipeline includes a cleanup step to delete the Kubernetes deployment and service.

Remember to update the Docker Hub credentials and any other environment-specific configurations before deploying to your own environment.
