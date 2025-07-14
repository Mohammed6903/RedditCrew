# Redditcrew: Multi-Agent Reddit User Persona Analysis

**Project Overview**  
Redditcrew is a sophisticated multi-agent AI system built using [crewAI](https://crewai.com), designed to scrape, analyze, and construct detailed user personas from Reddit profiles. This project showcases advanced AI agent orchestration, data scraping, and behavioral analysis, leveraging Python, crewAI, and custom tools to extract actionable insights from social media data. It demonstrates expertise in AI-driven automation, data analysis, and persona construction, with applications in social media research, user behavior analysis, and digital marketing.

## Key Features
- **Multi-Agent System**: Utilizes crewAI to orchestrate two specialized AI agents:
  - **Reddit User Data Researcher**: Scrapes and analyzes Reddit user data (posts, comments, subreddit activity) to identify behavioral patterns and interests.
  - **User Persona Construction Analyst**: Synthesizes scraped data into comprehensive, evidence-based user personas with detailed demographic, psychographic, and behavioral insights.
- **Custom Tooling**: Includes a custom `reddit_user_scraper_tool.py` for targeted Reddit data extraction.
- **Structured Output**: Generates detailed persona reports (e.g., `report.md`) with citations, confidence levels, and structured analysis for actionable insights.
- **Scalable Configuration**: Uses YAML-based configuration files (`agents.yaml`, `tasks.yaml`) for flexible agent and task customization.
- **Dependency Management**: Leverages [UV](https://docs.astral.sh/uv/) for efficient Python dependency management, ensuring reproducibility and scalability.

## Project Structure
```
redditcrew
├── README.md                          # Project documentation
├── output                             # Outputs storage (as text files)
├── knowledge
│   └── user_preference.txt            # User context (e.g., AI Engineer, Maharashtra, India)
├── pyproject.toml                     # Project configuration and dependencies
├── report.md                          # Generated persona report
├── src
│   └── redditcrew
│       ├── __init__.py               # Package initialization
│       ├── config
│       │   ├── agents.yaml           # Agent definitions
│       │   └── tasks.yaml            # Task configurations
│       ├── crew.py                   # CrewAI logic for agent orchestration
│       ├── main.py                   # Entry point for running the crew
│       └── tools
│           ├── __init__.py           # Tools package initialization
│           └── reddit_user_scraper_tool.py  # Custom Reddit scraping tool
├── tests                              # Unit tests (to be implemented)
└── uv.lock                           # Dependency lock file
```

## Technical Highlights
- **AI Agent Orchestration**: Implements a collaborative multi-agent system using crewAI, showcasing proficiency in designing and managing AI workflows.
- **Data Scraping & Analysis**: Employs a custom Reddit scraper to extract posts, comments, and metadata, with analysis of posting frequency, sentiment, and thematic patterns.
- **Persona Construction**: Transforms raw data into structured personas, including demographics (e.g., location, age), psychographics (e.g., interests, values), and behavioral patterns, with evidence-based citations.
- **Python Ecosystem**: Built with Python 3.10–3.13, using `crewai[tools]>=0.141.0` and UV for dependency management, ensuring a modern, robust development environment.
- **Extensibility**: Modular design allows easy addition of new agents, tasks, or tools, making the system adaptable for broader social media analysis use cases.

## Installation
Ensure Python 3.10–3.13 is installed. The project uses UV for dependency management.

1. **Install UV**:
   ```bash
   pip install uv
   ```

2. **Install Dependencies**:
   Navigate to the project root and run:
   ```bash
   uv sync
   ```

3. **Set Environment Variables**:
   Create a `.env` file in the project root and add these variables. Make sure to create a Reddit app to obtain the necessary Client ID and Client Secret and sign up for gemini api from google ai studio to get gemini api key:
   ```
    MODEL=gemini/gemini-2.5-flash-preview-04-17
    GEMINI_API_KEY=
    REDDIT_USER_AGENT="python:my_crewai_app:v1.0 by /u/userid"
    REDDIT_CLIENT_ID=
    REDDIT_CLIENT_SECRET=
   ```

## Running the Project
To execute the Redditcrew system and generate a user persona report:
```bash
crewai run
```
This command initializes the AI agents, scrapes Reddit data for the specified user profile, and generates a detailed persona report (e.g., `report.md`) in the project root.

## Customization
- **Agents**: Modify `src/redditcrew/config/agents.yaml` to define new agent roles, goals, or backstories.
- **Tasks**: Update `src/redditcrew/config/tasks.yaml` to customize data extraction and analysis tasks.
- **Logic**: Edit `src/redditcrew/crew.py` to adjust agent orchestration or integrate additional tools.
- **Inputs**: Modify `src/redditcrew/main.py` to specify custom Reddit user profiles or analysis parameters.

## Example Output
The system generates detailed persona reports, such as for user `Hungry-Move-6603`:
- **Demographics**: Adult, recently moved to Lucknow from Delhi for business purposes.
- **Interests**: Local culture, social issues (e.g., corruption, safety), food quality.
- **Behavioral Patterns**: Low activity, concentrated in July 2025, engaging in Indian subreddits like r/lucknow.
- **Communication Style**: Direct, observational, occasionally informal with emojis.

See `report.md` and `Hungry-Move-6603_UserPersona.txt` for full details.

## Skills Demonstrated
This project highlights the following skills relevant to AI engineering and data analysis:
- **AI Agent Development**: Designing and orchestrating multi-agent systems using crewAI.
- **Data Scraping**: Building custom tools for social media data extraction.
- **Behavioral Analysis**: Synthesizing complex datasets into actionable insights.
- **Python Programming**: Proficient use of Python, YAML, and modern dependency management tools.
- **Documentation**: Creating clear, professional documentation for technical and non-technical audiences.

## Future Enhancements
- Add unit tests in the `tests` directory for robust validation.
- Expand scraping capabilities to other platforms (e.g., X, Twitter).
- Integrate advanced NLP for deeper sentiment and thematic analysis.
- Enhance persona reports with visualizations (e.g., engagement timelines).

## Support
For questions or feedback:
- Visit the [crewAI documentation](https://docs.crewai.com)
- Check the [crewAI GitHub repository](https://github.com/joaomdmoura/crewai)
- Join the [crewAI Discord](https://discord.com/invite/X4JWnZnxPb)

---

**About the Developer**  
Developed by Mohammed Usmani, an AI Engineer based in Maharashtra, India, with a passion for building AI-driven solutions for social media analysis and user behavior modeling. This project reflects my expertise in AI agent systems, data scraping, and persona construction, tailored to real-world applications in digital analytics.
