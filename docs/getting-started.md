# Getting Started

## Prerequisites
1. Python 3.9+
2. Node.js 16+
3. Docker
4. Kubernetes
5. Cursor IDE

## Initial Setup
```bash
# Clone repository
git clone https://github.com/nickolos83/sports-ai-platform.git
cd sports-ai-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt
cd dashboard && npm install

# Setup development environment
kubectl apply -f k8s/dev/
```

## First Steps in Cursor
1. Open project in Cursor IDE
2. Navigate to `src/agents/analytics/base.py`
3. Start with basic agent implementation