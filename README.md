# 🎮 Tic Tac Toe – Flask App with CI/CD & Kubernetes

A simple **Tic Tac Toe web app built using Python Flask**, containerized with Docker, deployed on Kubernetes, and automated through a GitHub Actions CI/CD pipeline with ArgoCD.

## 🚀 Features
- Classic Tic Tac Toe game
- Flask-based web UI
- Dockerized app
- Kubernetes LoadBalancer deployment
- CI/CD with GitHub Actions
- Continuous Delivery via ArgoCD





Developer Commit (GitHub)
        │
        ▼
GitHub Actions (CI/CD Pipeline)
  ├── Run Tests & Lint
  ├── Code Quality Scan (SonarQube)
  ├── Build & Push Docker Image to ECR
  ├── Security Scan (Trivy)
  └── Update Deployment YAML
        │
        ▼
ArgoCD (GitOps)
        │
        ▼
Kubernetes Cluster (EKS)
  ├── Pods (TicTacToe App)
  ├── Service (LoadBalancer)
  └── Namespace (tictactoe)
