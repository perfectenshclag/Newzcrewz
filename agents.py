from crewai import Agent
import os
from dotenv import load_dotenv
from tools import tool

# Load environment variables
load_dotenv()

from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Streamlit app title

# Define Embedder Configuration
embedder = {
    "provider": "huggingface",
    "config": {
        "model": "all-MiniLM-L6-v2",
    }
}

# Define LLM
llm = ChatGroq(model="groq/llama3-8b-8192",verbose=True,temperature=0.5)


researcher=Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technoligies in {topic}",
    embedder=embedder,
    verbose=True,
    memoryview=True,
    backstory="A senior researcher that has years of experience and is driven by curiosity",
    tools=[tool],
    llm=llm,
    allow_delegation=True
)


news_writer=Agent(
       role="News writer",
    goal="Narrate compelling stories about {topic}",
    embedder=embedder,
    verbose=True,
    memoryview=True,
    backstory="A senior writer that has years of experience and is driven by curiosity",
    tools=[tool],
    llm=llm,
    allow_delegation=False 

)


