import asyncio

# Simulated agents using mock logic
async def profile_agent(questionnaire):
    # Extract skills and interests
    return {
        "skills": questionnaire.get("languages", []),
        "interests": [questionnaire.get("interest", "data")],
        "hours_per_week": questionnaire.get("hours_per_week", 0)
    }

async def skills_agent(profile):
    # Mock role recommendations
    roles = {
        "data_scientist": {"title": "Data Scientist", "skills": ["python","statistics","ml"]},
        "ml_engineer": {"title": "ML Engineer", "skills": ["python","mlops","docker"]},
        "frontend_dev": {"title": "Frontend Developer", "skills": ["javascript","react","html"]},
    }
    return {
        "recommended_roles": list(roles.keys()),
        "missing_skills": ["ml", "docker"]  #mock example 
    }

async def research_agent(skills_gap):
    # Mock research summary
    return {
        "top_role": skills_gap["recommended_roles"][0],
        "resources": ["Build projects with pandas and scikit-learn", 
                      "Portfolio examples for recruiters"]
    }

async def roadmap_loop(skills_gap, research):
    # Mock 6-month roadmap
    return {
        "Month1": "Learn Python & SQL",
        "Month2": "Build Data Projects",
        "Month3": "Learn ML Basics",
        "Month4": "Learn MLOps",
        "Month5": "Deploy a Project",
        "Month6": "Portfolio + Apply Jobs"
    }

async def companion_agent(roadmap):
    # Mock 7-day companion tasks
    return {
        "Day1": "Complete Python tutorial",
        "Day2": "Do SQL exercises",
        "Day3": "Start project 1",
        "Day4": "Continue project 1",
        "Day5": "Learn ML basics",
        "Day6": "Work on ML project",
        "Day7": "Write portfolio README"
    }

async def demo_flow():
    # Initial questionnaire
    questionnaire = {
        "languages": ["python", "sql"],
        "hours_per_week": 15,
        "interest": "data"
    }

    state = {}
    state['profile'] = await profile_agent(questionnaire)
    state['skills_gap'] = await skills_agent(state['profile'])
    state['research'] = await research_agent(state['skills_gap'])
    state['roadmap'] = await roadmap_loop(state['skills_gap'], state['research'])
    state['companion'] = await companion_agent(state['roadmap'])

    return state

if __name__ == "__main__":
    output = asyncio.run(demo_flow())
    print("\nFinal Output:\n", output)