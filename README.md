# 🎯 Guiden - AI Career Development Assistant

> **⚠️ Project Status**: This is an active prototype. Currently **40% complete** with core multi-agent system implemented. Frontend UI, LiveKit voice interviews, and mem0 memory integration are in development.

**Guiden** is an intelligent career development platform powered by **CrewAI** that helps job seekers bridge the gap between their current skills and their dream roles. Using a multi-agent AI system, Guiden provides personalized career guidance, skill gap analysis, learning roadmaps, and interview preparation strategies.

## �️ System Architecture

![Guiden System Architecture](docs/architecture-diagram.png)

Guiden combines **CrewAI multi-agents**, **mem0 long-term memory**, **Firecrawl real-time web intelligence**, and **LiveKit voice interviews** to deliver adaptive, self-improving career mentorship.

### Architecture Layers

**Layer 1 — User Interaction**

- Target users: Students, Job-Seekers, and Early-Career Professionals

**Layer 2 — Frontend Experience (UI Layer)**

- Dashboard for overview and insights
- Profile & Resume Upload interface
- Job Match View for comparing opportunities
- Roadmap View for learning paths
- Voice Interview Interface powered by LiveKit

**Layer 3 — API Gateway Layer**

- FastAPI backend routes requests between UI, agents, memory, and tools

**Layer 4 — Multi-Agent Intelligence Layer (CrewAI)**

- **Career Profile Agent**: Parses resume & profile
- **Job-Fit & Skill-Gap Agent**: Calculates fit & missing skills
- **Learning Roadmap Agent**: Builds adaptive roadmap
- **Web & Market Intelligence Agent (Firecrawl)**: Fetches jobs, company data, skill trends
- **Job Matching Agent**: Recommends high-fit roles
- **Resume Tailoring Agent**: Creates role-specific resumes
- **Voice Interview Agent (LiveKit)**: Conducts HR & technical mock interviews
- **Feedback & Reflection Agent**: Analyzes performance

**Layer 5 — Intelligence & Data Services**

- **mem0 Long-Term Memory Service**: Stores user history, interviews, progress & feedback
- **Firecrawl API**: Extracts real-time job descriptions, company data, skill needs & learning resources

**Layer 6 — Backend Storage & Identity**

- Firebase Authentication for user identity & secure login
- Database & Vector Store for user profiles, embeddings, and metadata

**Layer 7 — Continuous Improvement Loop**

- User actions & interviews feed back into the system
- Agent reasoning and memory storage (mem0) continuously improve recommendations
- Updated roadmap & coaching based on performance and feedback

## �🌟 Overview

Guiden leverages three specialized AI agents working collaboratively to:

- 📄 **Analyze your resume** or profile to understand your current skills and experience
- 🔍 **Research target job postings** and company culture
- 🗺️ **Generate personalized roadmaps** with actionable steps to bridge skill gaps
- 🎤 **Prepare you for interviews** with role-specific questions and behavioral scenarios

The system addresses the "Cold Start" problem by accepting either a structured resume (PDF) or user responses to screening questions, making it accessible to everyone from early-career professionals to experienced candidates.

## 🤖 AI Agents Architecture

### 1. Senior Career Profiler

**Role**: Comprehensive Resume and Profile Analysis  
**Capabilities**:

- Extracts technical and soft skills from resumes or user input
- Identifies experience levels and career trajectory
- Highlights achievements and notable projects
- Pinpoints strengths and growth areas

**Tools**:

- `FileReadTool()` - For reading and analyzing resume documents

**Model**: GPT-4o-mini (Temperature: 0.7)

### 2. Tech Recruitment Researcher

**Role**: Job Market and Company Culture Analysis  
**Capabilities**:

- Scrapes and analyzes job postings from provided URLs
- Decodes explicit and implicit job requirements
- Researches company culture, values, and work environment
- Identifies cultural fit indicators and hidden requirements

**Tools**:

- `FirecrawlScrapeWebsiteTool()` - For web scraping job postings and company information

**Model**: GPT-4o-mini (Temperature: 0.7)

### 3. Lead Career Architect

**Role**: Strategic Career Planning and Roadmap Generation  
**Capabilities**:

- Synthesizes profile analysis and market research
- Calculates match scores (0-100)
- Generates detailed skill gap analysis
- Creates actionable learning roadmaps with timelines
- Develops interview preparation materials

**Model**: GPT-4o-mini (Temperature: 0.7)

## 📋 Tasks Workflow

The system operates through a **sequential process** with three main tasks:

### Task 1: Profile Analysis

- **Agent**: Senior Career Profiler
- **Input**: Resume or user responses (`resume_or_text`)
- **Output**: Structured professional profile with skill inventory, achievements, and growth areas

### Task 2: Market Research

- **Agent**: Tech Recruitment Researcher
- **Input**: Job URL (`job_url`)
- **Output**: Comprehensive job requirements breakdown and company culture assessment

### Task 3: Strategy Generation

- **Agent**: Lead Career Architect
- **Input**: Results from Tasks 1 & 2
- **Output**: JSON-formatted career strategy including:
  - Match score (0-100)
  - Missing skills list
  - Learning roadmap with resources and timelines
  - Interview preparation context (technical questions, behavioral scenarios, key talking points)

## 🚀 Getting Started

### Prerequisites

- **Python**: 3.10 to 3.13
- **UV Package Manager**: For dependency management

### Installation

1. **Install UV** (if not already installed):

```bash
pip install uv
```

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd Guiden
```

1. **Install dependencies**:

```bash
crewai install
```

1. **Set up environment variables**:
Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Configuration

The project uses YAML configuration files for agents and tasks:

- **Agents**: [src/careeros___ai_career_development_assistant/config/agents.yaml](src/careeros___ai_career_development_assistant/config/agents.yaml)
- **Tasks**: [src/careeros___ai_career_development_assistant/config/tasks.yaml](src/careeros___ai_career_development_assistant/config/tasks.yaml)

## 💻 Usage

### Running the Crew

Execute the crew from the project root:

```bash
crewai run
```

### Command Line Options

The project provides several CLI commands:

#### 1. Run (Execute the crew)

```bash
python -m careeros___ai_career_development_assistant.main run
```

#### 2. Train (Train the crew with iterations)

```bash
python -m careeros___ai_career_development_assistant.main train <n_iterations> <filename>
```

#### 3. Replay (Replay from a specific task)

```bash
python -m careeros___ai_career_development_assistant.main replay <task_id>
```

#### 4. Test (Test the crew)

```bash
python -m careeros___ai_career_development_assistant.main test <n_iterations> <openai_model_name>
```

### Input Parameters

The system expects four main inputs:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `resume_or_text` | Resume content or user responses | PDF path or text responses |
| `job_url` | Target job posting URL | "<https://company.com/careers/job-id>" |
| `candidate_profile` | Additional candidate context | "AI Engineer with 5 years experience" |
| `target_role` | Desired position | "Senior ML Engineer" |

### Customizing Inputs

Edit [src/careeros___ai_career_development_assistant/main.py](src/careeros___ai_career_development_assistant/main.py) to customize inputs:

```python
inputs = {
    'resume_or_text': 'path/to/your/resume.pdf',
    'job_url': 'https://company.com/job-posting',
    'candidate_profile': 'Your professional summary',
    'target_role': 'Your target role'
}
```

## 📁 Project Structure

```
Guiden/
├── pyproject.toml                 # Project dependencies and metadata
├── README.md                       # This file
├── knowledge/                      # Knowledge base
│   └── user_preference.txt        # User preferences and context
├── src/
│   └── careeros___ai_career_development_assistant/
│       ├── __init__.py
│       ├── main.py                # Entry point with CLI commands
│       ├── crew.py                # Crew configuration and agent/task definitions
│       ├── config/
│       │   ├── agents.yaml        # Agent configurations
│       │   └── tasks.yaml         # Task configurations
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py     # Custom tool templates
```

## 🔧 Dependencies

Key dependencies (defined in [pyproject.toml](pyproject.toml)):

- **CrewAI**: 1.4.1 (with LiteLLM and tools extensions)
- **Firecrawl-py**: Web scraping for job postings
- **Python**: >=3.10, <3.14

## 🛠️ Extending the Project

### Adding Custom Tools

1. Define your tool in [src/careeros___ai_career_development_assistant/tools/custom_tool.py](src/careeros___ai_career_development_assistant/tools/custom_tool.py)
2. Import and add to the relevant agent in [crew.py](src/careeros___ai_career_development_assistant/crew.py)

Example:

```python
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class MyCustomToolInput(BaseModel):
    argument: str = Field(..., description="Argument description")

class MyCustomTool(BaseTool):
    name: str = "Tool Name"
    description: str = "Tool description"
    args_schema: Type[BaseModel] = MyCustomToolInput
    
    def _run(self, argument: str) -> str:
        # Your implementation
        return result
```

### Modifying Agent Behavior

Edit [src/careeros___ai_career_development_assistant/config/agents.yaml](src/careeros___ai_career_development_assistant/config/agents.yaml) to adjust:

- Agent roles and goals
- Backstories and expertise
- Behavioral parameters

### Customizing Tasks

Modify [src/careeros___ai_career_development_assistant/config/tasks.yaml](src/careeros___ai_career_development_assistant/config/tasks.yaml) to:

- Change task descriptions and outputs
- Adjust task sequencing
- Add new tasks or context dependencies

## 🎓 Knowledge Base

The `knowledge/` directory contains user preferences and context:

- **user_preference.txt**: Stores user information for personalized recommendations

Current user context:

- Name: John Doe
- Role: AI Engineer
- Interests: AI Agents
- Location: San Francisco, California

## 🔒 Environment Variables

Required environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key for LLM access

## 📊 Output Format

The final output is a **structured JSON** containing:

```json
{
  "match_score": 85,
  "missing_skills": [
    "Kubernetes",
    "GraphQL",
    "System Design at scale"
  ],
  "roadmap_steps": [
    {
      "skill": "Kubernetes",
      "resources": ["Course links", "Documentation"],
      "timeline": "2 weeks",
      "priority": "High"
    }
  ],
  "interview_prep_context": {
    "technical_questions": [...],
    "behavioral_scenarios": [...],
    "key_talking_points": [...]
  }
}
```

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📚 Resources

- **CrewAI Documentation**: [https://docs.crewai.com](https://docs.crewai.com)
- **CrewAI GitHub**: [https://github.com/joaomdmoura/crewai](https://github.com/joaomdmoura/crewai)
- **CrewAI Discord**: [https://discord.com/invite/X4JWnZnxPb](https://discord.com/invite/X4JWnZnxPb)
- **UV Documentation**: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

## 📝 License

This project is built using CrewAI framework. Please refer to CrewAI's licensing terms.

## 🙏 Acknowledgments

Built with ❤️ using:

- [CrewAI](https://crewai.com) - Multi-agent orchestration framework
- [OpenAI GPT-4o-mini](https://openai.com) - Language models
- [Firecrawl](https://firecrawl.dev) - Web scraping capabilities

---

**Guiden** - Empowering careers through intelligent guidance. 🚀
