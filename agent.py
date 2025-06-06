from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.graphs.neo4j_graph import Neo4jGraph
import os
from dotenv import load_dotenv

load_dotenv()

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD")
)

llm = ChatOpenAI(
    openai_api_base=os.getenv("SAMBANOVA_API_URL", "http://localhost:11434"),
    openai_api_key=os.getenv("SAMBANOVA_API_KEY"),
    model="gemma-7b-it"
)

tools = [
    Tool(name="Graph Search", func=graph.query, description="Query Neo4j graph")
]

agent = initialize_agent(
    tools, llm, agent="chat-zero-shot-react-description", verbose=True
)

if __name__ == "__main__":
    print(agent.run("Summarize InfraFlow mesh status"))
