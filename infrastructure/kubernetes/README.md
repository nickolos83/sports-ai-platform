# Kubernetes Configuration

## Components
1. Agent Deployments
2. Message Queue (Kafka)
3. Databases (MongoDB, Redis)
4. Monitoring Stack

## Deployment
```bash
# Apply base configuration
kubectl apply -f base/

# Deploy agents
kubectl apply -f agents/

# Setup monitoring
kubectl apply -f monitoring/
```

## Scaling
- HorizontalPodAutoscaler for agents
- Resource limits and requests
- Node pool configurations