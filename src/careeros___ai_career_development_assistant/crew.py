import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	FileReadTool,
	FirecrawlScrapeWebsiteTool
)





@CrewBase
class CareerosAiCareerDevelopmentAssistantCrew:
    """CareerosAiCareerDevelopmentAssistant crew"""

    
    @agent
    def senior_career_profiler(self) -> Agent:
        
        return Agent(
            config=self.agents_config["senior_career_profiler"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def tech_recruitment_researcher(self) -> Agent:
        
        return Agent(
            config=self.agents_config["tech_recruitment_researcher"],
            
            
            tools=[				FirecrawlScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def lead_career_architect(self) -> Agent:
        
        return Agent(
            config=self.agents_config["lead_career_architect"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def profile_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["profile_analysis_task"],
            markdown=False,
            
            
        )
    
    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"],
            markdown=False,
            
            
        )
    
    @task
    def strategy_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config["strategy_generation_task"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the CareerosAiCareerDevelopmentAssistant crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
