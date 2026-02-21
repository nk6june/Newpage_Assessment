from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from src.components.llm import load_llm
from src.components.tools import create_retriever_tool


def create_agent(vector_store):

    llm = load_llm()
    retriever_tool = create_retriever_tool(vector_store)
    agent = create_react_agent(
        llm,
        tools=[retriever_tool],
        checkpointer=MemorySaver(),
    )


    return agent

