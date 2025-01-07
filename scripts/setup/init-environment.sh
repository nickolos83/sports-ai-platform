#!/bin/bash

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup infrastructure
kubectl apply -f k8s/dev/

# Initialize databases
helm install mongodb mongodb/mongodb
helm install redis redis/redis

# Setup monitoring
helm install prometheus prometheus-community/prometheus
helm install grafana grafana/grafana