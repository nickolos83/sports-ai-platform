from fastapi import APIRouter, HTTPException
from typing import List
from models.agent import Agent, AgentTask

router = APIRouter()

@router.get('/agents', response_model=List[Agent])
async def get_agents():
    return await agent_service.get_all()

@router.post('/agents/{agent_id}/tasks')
async def create_task(agent_id: str, task: AgentTask):
    return await agent_service.assign_task(agent_id, task)