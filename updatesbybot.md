# Updates by Bot

### File: app.py
- Problem: Debug mode is explicitly set to False, which may hinder development
- Applied Fix: Use an environment variable to toggle debug mode: app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')

### File: Dockerfile
- Problem: No specific Python version pinned, which may lead to inconsistencies
- Applied Fix: Use a specific Python version, e.g., FROM python:3.9-slim

### File: requirements.txt
- Problem: Flask version is not pinned, which may cause compatibility issues
- Applied Fix: Pin the Flask version to a specific release, e.g., flask==2.3.2

### File: k8s/deployment.yaml
- Problem: No rolling update strategy defined, which may cause downtime during updates
- Applied Fix: Add a rolling update strategy to the deployment spec, e.g., strategy: {type: RollingUpdate, rollingUpdate: {maxSurge: 1, maxUnavailable: 0}}

### File: .github/workflows/pipeline.yml
- Problem: No version tagging for Docker images, which may make rollbacks difficult
- Applied Fix: Use Git SHA or another versioning scheme for Docker image tags, e.g., tags: ashwanth01/ashapp-backend:latest,ashwanth01/ashapp-backend:${{ github.sha }}

