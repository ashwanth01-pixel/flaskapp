Based on the repository context provided, the main tech stack includes:

1. Python: The main programming language used, as evidenced by the app.py file and the presence of requirements.txt [app.py, requirements.txt]

2. Flask: A Python web framework used for the backend application [app.py]

3. Docker: Used for containerizing the application, as indicated by the presence of a Dockerfile [SuggestedFix.md, pipeline.yml]

4. Kubernetes: Used for orchestrating and deploying the application, as shown by the k8s directory containing deployment.yaml and service.yaml files [SuggestedFix.md, deployment.yaml]

5. GitHub Actions: Used for CI/CD, as evidenced by the pipeline.yml file in the .github/workflows directory [pipeline.yml]

6. FAISS: A library for efficient similarity search, indicated by the presence of FAISS index files [SuggestedFix.md]

7. pytest: Mentioned as a testing framework in the CI/CD pipeline [pipeline.yml]

8. flake8: Used for linting Python code, as seen in the CI/CD pipeline [pipeline.yml]

This tech stack represents a typical modern web application setup with containerization, orchestration, and CI/CD practices.
