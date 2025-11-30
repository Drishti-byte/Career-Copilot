import asyncio
from typing import Any, Dict

async def questionnaire_tool(session_id: str, session_service, **kwargs) -> Dict[str, Any]:
    await asyncio.sleep(0.05)
    return {
    "languages": ["python", "sql"],
    "hours_per_week": 15,
    "interest": "data",
    }

async def csv_analyzer_tool(name: str, query: str = None) -> Dict[str, Any]:
    await asyncio.sleep(0.05)
    roles = {
    "data_scientist": {"title": "Data Scientist", "skills": ["python","statistics","ml"]},
    "ml_engineer": {"title": "ML Engineer", "skills": ["python","mlops","docker"]},
    "frontend_dev": {"title": "Frontend Developer", "skills": ["javascript","react","html"]},
    }
    if name == "roles":
        return {"ok": True, "hits": roles}
    return {"ok": False, "error": "dataset not found"} 

async def local_search_tool(query: str) -> Dict[str, Any]:
    await asyncio.sleep(0.05)
    docs = {
    "data_projects": "Build projects with pandas and scikit-learn",
    "mlops_intro": "MLOps pipelines and deployment strategies",
    "portfolio": "README + deployed examples impress recruiters",
    }
    hits = [v for k,v in docs.items() if query.lower() in k or query.lower() in v.lower()]
    return {"ok": True, "hits": hits} 