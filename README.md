# 🎮 Tic Tac Toe – Flask App with CI/CD & Kubernetes

A simple **Tic Tac Toe web app built using Python Flask**, containerized with Docker, deployed on Kubernetes, and automated through a GitHub Actions CI/CD pipeline with ArgoCD.

## 🚀 Features
- Classic Tic Tac Toe game
- Flask-based web UI
- Dockerized app
- Kubernetes LoadBalancer deployment
- CI/CD with GitHub Actions
- Continuous Delivery via ArgoCD












                 ┌──────────────────────────┐
                 │      Developer Push      │
                 │   (Code → GitHub Main)   │
                 └────────────┬─────────────┘
                              │
                              ▼
           ┌────────────────────────────────────────┐
           │        GitHub Actions CI/CD Pipeline    │
           │------------------------------------------│
           │  ✅ Tests, Lint, SonarQube, Trivy        │
           │  ✅ Build & Push Image to ECR            │
           │  ✅ Update Kubernetes Deployment YAML     │
           └──────────────────┬───────────────────────┘
                              │
                              ▼
                    ┌────────────────┐
                    │     ArgoCD     │
                    │ (GitOps Engine)│
                    └───────┬────────┘
                            │
                            ▼
               ┌────────────────────────────┐
               │  Kubernetes Cluster (EKS)  │
               │----------------------------│
               │  🐳 Pods: TicTacToe App     │
               │  ☸️ Service: LoadBalancer   │
               │  🧠 Namespace: tictactoe    │
               └────────────┬───────────────┘
                            │
                            ▼
              🌐 AWS ELB → http://<elb-dns>:5050
