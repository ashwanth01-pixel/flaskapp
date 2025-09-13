

## Automated Fixes Applied
- Updated `Dockerfile`
- Updated `k8s/deployment.yaml`
- Updated `app.py`
- Updated `.gitignore`

---
### Fixes Applied (2025-09-13T04:15:15.405043 UTC)
- No major changes, formatting only.


---
### Fixes Applied (2025-09-13T04:17:44.830566 UTC)
- No major changes, formatting only.


---
### Fixes Applied (2025-09-13T04:21:53.048292 UTC)
- **example_file.py**
    No textual changes detected (file created or binary)



---
### Fixes Applied (2025-09-13T04:28:36.898007 UTC)
- **example_file.py**
    No textual changes detected (file created or binary)



---
### Fixes Applied (2025-09-13T04:30:21.319545 UTC)

- **app.py**
    --- a/app.py
    +++ b/app.py
    @@ -1,4 +1,4 @@
    -
    +from flask import Flask
     import logging
     
     app = Flask(__name__)

- **Dockerfile**
    --- a/Dockerfile
    +++ b/Dockerfile
    @@ -5,3 +5,6 @@
     COPY requirements.txt .
     RUN pip install --no-cache-dir -r requirements.txt
     
    +COPY . .
    +
    +CMD ["python", "app.py"]

- **k8s/deployment.yaml**
    --- a/k8s/deployment.yaml
    +++ b/k8s/deployment.yaml
    @@ -17,3 +17,22 @@
             image: ashwanth01/ashapp-backend:latest
             ports:
             - containerPort: 5000
    +        resources:
    +          limits:
    +            cpu: "500m"
    +            memory: "256Mi"
    +          requests:
    +            cpu: "250m"
    +            memory: "128Mi"
    +        readinessProbe:
    +          httpGet:
    +            path: /
    +            port: 5000
    +          initialDelaySeconds: 10
    +          periodSeconds: 5
    +        livenessProbe:
    +          httpGet:
    +            path: /
    +            port: 5000
    +          initialDelaySeconds: 15
    +          periodSeconds: 10

- **.github/workflows/pipeline.yml**
    --- a/.github/workflows/pipeline.yml
    +++ b/.github/workflows/pipeline.yml
    @@ -1,6 +1,10 @@
     name: CI/CD Pipeline
     
     on:
    +  push:
    +    branches: [main]
    +  pull_request:
    +    branches: [main]
       workflow_dispatch:
     
     jobs:
    @@ -12,13 +16,17 @@
           uses: actions/checkout@v3
     
         - name: Log in to Docker Hub
    -      run: echo "${{ secrets.DOCKERHUB_TOKEN }}" | docker login -u "ashwanth01" --password-stdin
    +      uses: docker/login-action@v2
    +      with:
    +        username: ashwanth01
    +        password: ${{ secrets.DOCKERHUB_TOKEN }}
     
    -    - name: Build Docker image
    -      run: docker build -t ashwanth01/ashapp-backend:latest .
    -
    -    - name: Push Docker image
    -      run: docker push ashwanth01/ashapp-backend:latest
    +    - name: Build and push Docker image
    +      uses: docker/build-push-action@v4
    +      with:
    +        context: .
    +        push: true
    +        tags: ashwanth01/ashapp-backend:latest
     
         - name: Apply Kubernetes manifests
           run: |
    @@ -30,3 +38,7 @@
             NODE_IP=$(hostname -I | awk '{print $1}')
             echo "App running at: http://$NODE_IP:30080"
     
    +    - name: Verify deployment
    +      run: |
    +        kubectl rollout status deployment/ashapp-backend
    +        kubectl get pods -l app=ashapp-backend
