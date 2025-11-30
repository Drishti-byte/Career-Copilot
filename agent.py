from typing import Dict 
from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent
from google.adk.runners import Runner
from tools import questionnaire_tool, csv_analyzer_tool, local_search_tool 

LLM_MODEL = "mock-local"

profile_agent = LlmAgent(
name = "profile_builder",
model = LLM_MODEL,
instruction = """
Extract a compact skills list and interests from the questionnaire results available in the session state.
Output JSON with keys: skills (list), interests (list), hours_per_week (int).
""",
output_key="profile",
)

skills_agent = LlmAgent(
name="skills_gap_analyzer",
model = LLM_MODEL,
instruction="""
Given state['profile'], call the csv_analyzer tool to fetch roles and skills, compute missing skills, and produce a sorted list of role recommendations. Save the result as 'skills_gap'.
""",
output_key="skills_gap",
)

research_agent = LlmAgent(
name="research_agent",
model=LLM_MODEL,
instruction="""
Using state['skills_gap'], identify the top role and summarize useful learning resources from the local_search tool. Save a short summary into 'research'.
""",
output_key="research",
)

roadmap_llm = LlmAgent(
name = "roadmap_llm",
model = LLM_MODEL,
instruction = """
Generate a 6-month roadmap using state['skills_gap'] and state['research']. Use Month1..Month6 format.
""",
output_key = "roadmap",
)

# Loop agent that may call roadmap_llm multiple times to refine the plan
roadmap_loop = LoopAgent(
name = "roadmap_loop",
sub_agents = [roadmap_llm],
max_iterations = 3,
)

companion_agent = LlmAgent(
name = "companion_agent",
model = LLM_MODEL,
instruction = """
Create a 7-day companion task list derived from state['roadmap'] for motivation and progress tracking. Save under 'companion'.
""",
output_key="companion",
)

pipeline = SequentialAgent(
name = "career_co_pilot_pipeline",
sub_agents=[profile_agent, skills_agent, research_agent, roadmap_loop, companion_agent],
)

root_agent = pipeline
# Tools registry for the Runner
TOOLS = {
"questionnaire": questionnaire_tool,
"csv_analyzer": csv_analyzer_tool,
"local_search": local_search_tool,
}

def create_runner() -> Runner:
    runner = Runner(
        app_name="career_copilot_app",
        agent=root_agent,
        session_service=None 
    )
    return runner