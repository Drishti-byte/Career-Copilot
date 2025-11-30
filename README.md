# Career-Copilot
**Problem Statement**
Navigating a career in technology has become increasingly complex, especially for students, freshers, and early professionals who lack proper mentorship, structured guidance, and exposure to industry-ready skills. With thousands of emerging tech roles in the era of AI revolution, most learners found it difficult to understand which path fits their strengths and interests. Traditional career counseling is either generalised, outdated, or inaccessible leaving individuals to make major decisions with incomplete information. As a result, students often waste months learning irrelevant skills, taking random courses, or building projects that don't align with real job market needs. Career copilots solves this by offering a personalised AI agent that personalises career guidance, identifies skill gaps, curates learning resources and creates a step by step learning roadmap according to each individual's educational qualifications. 

**Solution Statement**
Single response chatbots fail to provide deep personalisation, long term reasoning and multi step planning. Career exploration is a sequential process which involves understanding the user, analysing skills, researching roles, planning a roadmap and finally generating daily guidance. This requires content retention, decision making, usage of tools and independent task execution capabilities that traditional models don't offer. AI Agents can operate as independent specialists - Profile Agent, Skills Gap Agent, Research Agent, Roadmap Agent, Companion Agent - each handling a specific part of career building pipeline. 

**Architecture**
Career Copilot consists of five agent autonomously coordinated system. 
1. **Profile Agent** - Collects user details such as skills, interests, availability, academic background and learning pace.
2. **Skills Gap Agent** - Analyses the user's profile and compares it with industry expectations across multiple tech roles. 
3. **Research Agent** - Evaluates job market trends and selects the best fit tech role for the user, along with essential study resources. 
4. **Roadmap Agent** - Converts long-term goals into a clear monthly plan balancing fundamentals, projects and porfolio building. 
5. **Companion Agent** - Generates a simple 7 day action plan to kickstart the user's journey immediately. 
A central controller flow sequentially passes state between these agents. Once the full pipeline completes, the system produces a unified dashboard displaying personalised career pathway. The UI is built using Streamlit, offering a clean, interactive experience. 

**Demo**
In the demo, the user begins by entering basic information : existing skills, areas of interest and available learning hours. 
Career Copilot then runs it autonomously:
- The **Profile Agent** condenses user input into a structured profile. 
- The **Skills Gap Agent** finds what skills they need to acquire and recommends potential roles. 
- The **Research Agent** picks the top role suited for the user and suggests curated learning resources. 
- The **Roadmap Agent** produces a 6 - month learning blueprint with monthly goals. 
- The **Companionn Agent** generates a motivational, actionable 7 - day kickoff plan. 
The final output is shown in the Streamlit interface as an organised, interactive career pathway - precise, personalised and ready to follow. 

**Tools, Technologies and Approach** 
Career Copilot was built using: 
- **Python 3.12**
- **OpenAI Agents API** for orchestrating autonomous agent behaviour 
- **Five specialised LLM Agents** for modular reasoning 
- **Streamlit** for building user friendly interface.
- **Asyncio** for coordinating agent execution 
- **Pandas** to handle table like structures, skill matrices and role comparisons 
- **Pydantic** for structured state manegement 
The project follows a clean, modular architecture. Each agent is defined with its own instructions, model configurations, and output schema. The final system is robust, adaptable and easy to extend - making it suitable for real - world student conseling and institutional use. 

**If I had more time, This is what I'd do**
If more time were available, several enhancements could significantly extend the impact of Career Copilot:
- Add a **real time job scraping** to connect users with live hiring oppurtunities. 
- Would concentrate on **non-tech roles** so students from all the domains have a clear path to their career. 
- Integrate a **resume analyser** to automatically evaluate and optimise the user's CV. 
- Introduce **mock interview agent** to stimulate technical and HR interviews. 
- Build a **progress tracker** where users log their their learning milestones. 
- Integrate with **Udemy, Coursera, Youtube API** to fetch structured learning paths automatically.
- Build a **mobile-friendly version** for wider reach. 
- Will focus on providing these facilities to **under developed areas and rural areas **where there is a lack of proper guidance. 
- Enabling **voice based interaction** with users for accessibility. 
With these additions, Career Copilot can evolve from a roadmap generator into a full-fledged AI career ecosystem.

**Conclusion**
Career Copilot successfully demonstrates how AI agents can transform the way learners navigate their career growth. By automating skill profiling, gap analysis, research, and personalized planning, the system delivers an end-to-end, actionable career pathway within seconds. The modular agent architecture ensures clarity, transparency, and extensibility—making it easy to add new data sources, roles, or learning resources in the future. This project shows that personalized career guidance, which traditionally requires expert time and effort, can now be made scalable, interactive, and accessible to anyone. Overall, Career Copilot proves that AI-driven career support can empower learners to make informed, confident decisions in their professional journey.

**Value Statement**
Career Copilot empowers students and early professionals with personalized, data-driven career guidance through a seamless multi-agent workflow. It transforms raw user inputs into actionable insights—clear skill gaps, relevant resources, a structured roadmap, and a motivational weekly companion. By combining intelligence, automation, and user-centric design, the system delivers clarity, confidence, and direction to individuals striving for impactful career growth.
