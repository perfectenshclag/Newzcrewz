from crewai import Task
from agents import researcher,news_writer
from tools import tool

research_task=Task(
    description="Identify the current news related to {topic}.Focus on identifying pros and cons",
    expected_output="A summary report on the {topic}",
    tools=[tool],
    agent=researcher
)

writing_task=Task(
    description="Identify the current news related to {topic}.Focus on identifying pros and cons",
    expected_output="A 4 para article on the {topic}",
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file="news.md"
)