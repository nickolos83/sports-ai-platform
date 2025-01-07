# Environment Setup Guide

## Prerequisites
- Python 3.9+
- Node.js 16+
- Docker
- Kubernetes
- Access to required APIs

## API Keys Required
- Flashscore API
- SportScore API
- Football API
- OpenAI API (for GPT-4)
- Mistral AI API

## Development Environment
```bash
# Clone repository
git clone https://github.com/nickolos83/sports-ai-platform.git

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Infrastructure Setup
```bash
# Start Kubernetes cluster
kubectl apply -f k8s/dev/

# Setup monitoring
helm install prometheus prometheus-community/prometheus
helm install grafana grafana/grafana
```