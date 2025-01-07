# Sports AI Platform - Project Structure

## Directory Structure
```
sports-ai/
├── docs/                # Documentation
│   ├── getting-started.md
│   ├── architecture.md
│   ├── development.md
│   └── roadmap.md
├── src/                # Source code
│   ├── agents/         # AI Agents
│   │   ├── analytics/
│   │   ├── content/
│   │   ├── qa/
│   │   └── editor/
│   ├── api/           # Backend API
│   │   ├── routes/
│   │   └── services/
│   ├── dashboard/    # Frontend
│   │   ├── components/
│   │   └── pages/
│   └── core/        # Core functionality
├── tests/          # Tests
├── k8s/           # Kubernetes configs
└── tools/        # Development tools
```

## Tech Stack
- Backend: FastAPI, CrewAI, LangChain
- Frontend: React, TailwindCSS
- Database: MongoDB, Redis
- Infrastructure: Kubernetes, Istio
- Monitoring: Prometheus, Grafana