# Repository Summary

[Tech Stack](TECHSTACK.md) | [Workflow](WORKFLOW.md)

Based on the repository context provided, this appears to be a Kubernetes-deployed Flask application with CI/CD automation. The main components are:

1. Flask web application, likely defined in app.py [README.md]
2. Kubernetes deployment files (k8s/deployment.yaml and k8s/service.yaml) [README.md]
3. Docker containerization with a Dockerfile in the root directory [README.md]
4. CI/CD pipeline using GitHub Actions (.github/workflows/pipeline.yml) [README.md]
5. FAISS index files for similarity search or information retrieval (faiss_index/index.faiss and faiss_index/index.pkl) [README.md]
6. Documentation files including README.md, Design.md, SuggestedFix.md, and UML.md [README.md]

The overall purpose of this repository is to host a Flask-based web application, with a focus on automated deployment to Kubernetes and potentially incorporating FAISS for efficient similarity search capabilities.

## Tech Stack
Based on the repository context provided, the main tech stack includes:

1. Python: The main programming language used [TECHSTACK.md]
2. Flask: Python web framework for the backend application [TECHSTACK.md]
3. Docker: Used for containerizing the application [TECHSTACK.md]
4. Kubernetes: Used for orchestrating and deploying the application [TECHSTACK.md]
5. GitHub Actions: Used for CI/CD [TECHSTACK.md]
6. FAISS: Library for efficient similarity search [TECHSTACK.md]
7. pytest: Testing framework [TECHSTACK.md]
8. flake8: Used for linting Python code [TECHSTACK.md]

This tech stack represents a typical modern web application setup with containerization, orchestration, and CI/CD practices, as stated in the TECHSTACK.md file.

## Workflow
Here's a detailed developer guide for this repository based on the provided context:

1. Project Overview:
   This is a Flask-based web application deployed on Kubernetes with CI/CD automation via GitHub Actions. The application likely incorporates FAISS for vector search capabilities. [README.md]

2. Development Environment Setup:
   - Use Python 3.x (specific version not provided)
   - Install dependencies: `pip install -r requirements.txt`
   - Flask 2.3.2 is the main web framework [requirements.txt]

3. Project Structure:
   - Root directory: Contains main application files (app.py, Dockerfile, requirements.txt)
   - .github/workflows: CI/CD pipeline configuration (pipeline.yml)
   - k8s: Kubernetes manifests (deployment.yaml, service.yaml)
   - faiss_index: FAISS index files for vector search (index.faiss, index.pkl)
   [WORKFLOW.md]

4. Application Code:
   - Main application logic is in app.py
   - FAISS index is used for vector search (faiss_index directory)
   [WORKFLOW.md]

5. Testing:
   - Add a `tests/` directory with unit and integration tests
   - Run tests using pytest: `pytest`
   - Linting is done with flake8: `flake8 .`
   [SuggestedFix.md, pipeline.yml]

6. Docker:
   - Dockerfile is present in the root directory
   - Build image: `docker build -t ashwanth01/ashapp-backend:latest .`
   - Run container: `docker run -p 5000:5000 ashwanth01/ashapp-backend:latest`
   [WORKFLOW.md]

7. Kubernetes Deployment:
   - Kubernetes manifests are in the k8s directory
   - Deploy: 
     ```
     kubectl apply -f k8s/deployment.yaml
     kubectl apply -f k8s/service.yaml
     ```
   - The deployment uses a rolling update strategy and includes resource limits and health checks
   [WORKFLOW.md, SuggestedFix.md]

8. CI/CD:
   - GitHub Actions workflow is defined in .github/workflows/pipeline.yml
   - The pipeline includes steps for linting, testing, building Docker image, and deploying to Kubernetes
   - Docker Hub is used for image registry
   - Images are tagged with both 'latest' and the Git SHA
   [pipeline.yml, WORKFLOW.md]

9. Environment Variables:
   - Use environment variables for sensitive information
   - Add a `.env.example` file to show which variables are needed
   - FLASK_ENV and PYTHONUNBUFFERED are set in the Kubernetes deployment
   [SuggestedFix.md, WORKFLOW.md]

10. Logging:
    - Implement a logging configuration file for proper logging throughout the application
    [SuggestedFix.md]

11. Documentation:
    - Expand documentation by adding:
      - CONTRIBUTING.md for potential contributors
      - API.md or ENDPOINTS.md to document available endpoints
      - DEPLOYMENT.md with deployment instructions
    [SuggestedFix.md]

12. Dependency Management:
    - Consider using `Pipfile` and `Pipfile.lock` (for pipenv) or `poetry.lock` (for poetry) in addition to `requirements.txt`
    [SuggestedFix.md]

13. Security:
    - Use environment variables for sensitive information
    - Implement a .dockerignore file
    - Use GitHub Secrets for sensitive information in CI/CD
    [SuggestedFix.md, WORKFLOW.md]

14. FAISS Index Management:
    - Implement a process for updating and managing FAISS index files
    - Consider versioning these files if they change frequently
    [SuggestedFix.md]

15. Best Practices:
    - Follow Python style guidelines (implied by use of flake8 in pipeline)
    - Ensure all dependencies in requirements.txt are pinned to specific versions
    - Review Kubernetes manifests for best practices in resource limits, health checks, and security contexts
    [SuggestedFix.md, WORKFLOW.md]

This guide provides an overview based on the available context. Developers should refer to the specific files mentioned for more
