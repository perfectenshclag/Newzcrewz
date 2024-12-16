from crewai import Crew, Process
from agents import researcher,news_writer
from tasks import research_task,writing_task


crew=Crew(verbose=True,
          memory=True,
    agenst=[researcher,news_writer],
    tasks=[research_task,writing_task],
    process=Process.sequential
)


result=crew.kickoff(inputs={'topic':'Evolution of humans'})
print(result)
