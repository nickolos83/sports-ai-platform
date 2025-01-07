import pytest
from agents.analytics import AnalyticsAgent

@pytest.mark.asyncio
async def test_analytics_agent():
    agent = AnalyticsAgent()
    data = {
        'match_data': {...},
        'team_stats': {...}
    }
    
    result = await agent.analyze(data)
    
    assert result.quality_score > 0.8
    assert 'insights' in result
    assert 'recommendations' in result