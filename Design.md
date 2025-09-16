Based on the provided repository context, I can generate a Mermaid diagram that illustrates the CI/CD pipeline and deployment process for the application. Here's a Mermaid diagram in markdown fenced code block format:

```mermaid
graph TD
    A[Developer Push] --> B[GitHub Actions]
    B --> C[Lint with flake8]
    C --> D[Run unit tests]
    D --> E[Build Docker Image]
    E --> F[Push to Docker Hub]
    F --> G[Apply Kubernetes Manifests]
    G --> H[Verify Deployment]
    H --> I[Test Application]
    I --> J[Cleanup on Failure]

    subgraph Kubernetes Cluster
    K[Deployment: ashapp-backend]
    L[Service: ashapp-backend]
    end

    G --> K
    G --> L
```

This diagram is based on the information from the `pipeline.yml` file, which outlines the CI/CD process, and the `deployment.yaml` file, which describes the Kubernetes deployment. The diagram shows the flow from a developer push to GitHub, through the various steps in the GitHub Actions workflow, and finally to the deployment and verification in the Kubernetes cluster.
