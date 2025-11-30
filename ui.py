import streamlit as st
import asyncio
from run import demo_flow
import pandas as pd
import time

st.set_page_config(page_title="Career Co-Pilot", layout="wide")
st.title("🎓 Career Co-Pilot")

st.markdown(
    """
    Enter your details below and click **Run Co-Pilot**.
    The pipeline will generate a personalized career roadmap and tasks.
    """
)

with st.form("profile_form"):
    name = st.text_input("Name", value="Student")
    skills = st.text_area("Skills (comma separated)", value="python, sql")
    hours_per_week = st.number_input("Hours per week", min_value=1, max_value=168, value=15)
    interest = st.selectbox("Interest", ["data", "web", "ml", "design"], index=0)
    submitted = st.form_submit_button("Run Co-Pilot")

if submitted:
    user_questionnaire = {
        "languages": [s.strip() for s in skills.split(",") if s.strip()],
        "hours_per_week": hours_per_week,
        "interest": interest
    }

    # Spinner + fake progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    async def run_pipeline():
        output = await demo_flow()
        return output

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    output = loop.run_until_complete(run_pipeline())

    # Simulate progress
    for i in range(101):
        time.sleep(0.01)
        progress_bar.progress(i)
        if i % 20 == 0:
            status_text.text(f"Processing... {i}%")
    status_text.text("Pipeline completed!")

    st.success("✅ Career Co-Pilot finished!")

    # Layout using tabs
    tabs = st.tabs(["Profile", "Skills Gap", "Research", "Roadmap", "Companion Tasks"])

    # Profile
    with tabs[0]:
        profile = output.get("profile", {})
        st.table(pd.DataFrame([profile]))

    # Skills Gap
    with tabs[1]:
        skills_gap = output.get("skills_gap", {})
        if "recommended_roles" in skills_gap:
            df_roles = pd.DataFrame(
                {"Recommended Roles": skills_gap["recommended_roles"][:],
                 "Missing Skills": [', '.join(skills_gap.get("missing_skills", []))]*len(skills_gap["recommended_roles"])}
            )
            st.table(df_roles)
        else:
            st.write(skills_gap)

    # Research
    with tabs[2]:
        research = output.get("research", {})
        if research:
            df_research = pd.DataFrame({"Top Role": [research.get("top_role", "")],
                                        "Resources": [', '.join(research.get("resources", []))]})
            st.table(df_research)
        else:
            st.write("No research data available.")

    # Roadmap
    with tabs[3]:
        roadmap = output.get("roadmap", {})
        if roadmap:
            df_roadmap = pd.DataFrame(list(roadmap.items()), columns=["Month", "Task"])
            st.table(df_roadmap)
        else:
            st.write("No roadmap available.")

    # Companion Tasks
    with tabs[4]:
        companion = output.get("companion", {})
        if companion:
            df_companion = pd.DataFrame(list(companion.items()), columns=["Day", "Task"])
            st.table(df_companion)
        else:
            st.write("No companion tasks available.")

    st.download_button(
        label="Download JSON",
        data=str(output),
        file_name="career_copilot_output.json",
        mime="application/json"
    )