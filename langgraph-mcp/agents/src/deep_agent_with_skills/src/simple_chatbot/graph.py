"""LangGraph agent with tool integration for simple chatbot."""

import logging
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import AnyMessage, HumanMessage
from typing_extensions import TypedDict, Annotated
import operator

from simple_chatbot.prompts import (
    SYSTEM_INSTRUCTIONS,
    WORKFLOW_INSTRUCTIONS,
)
from simple_chatbot.tools import (
    get_mcp_tools,
)

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_path, override=True)

logger = logging.getLogger(__name__)

# Define the state for our chatbot
class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

def create_graph():
    """Create and configure the agent graph.
    
    Returns:
        Compiled LangGraph agent.
    """
    logger.info("Initializing simple chatbot agent...")
    
    # Initialize LLM - using Ollama with a default model, can be configured via env
    model_name = os.getenv("OLLAMA_MODEL", "llama2")
    llm = ChatOllama(model=model_name)
    
    # Build system prompt
    system_prompt = f"{SYSTEM_INSTRUCTIONS}\n\n{WORKFLOW_INSTRUCTIONS}"
    
    # Define the chat node function
    def chat_node(state: State) -> dict:
        """Process user messages and generate responses.
        
        Args:
            state: Current conversation state containing messages
            
        Returns:
            Updated state with the LLM's response
        """
        logger.info("Processing chat node")
        
        # Prepare messages for the LLM
        messages_for_llm = [
            {"role": "system", "content": system_prompt}
        ] + state["messages"]
        
        # Generate response from LLM
        response = llm.invoke(messages_for_llm)
        
        # Return the response to be added to messages
        return {"messages": [response]}
    
    # Create the graph
    workflow = StateGraph(State)
    
    # Add nodes
    workflow.add_node("chat", chat_node)
    
    # Add edges
    workflow.add_edge(START, "chat")
    workflow.add_edge("chat", END)
    
    # Add memory for conversation persistence
    memory = MemorySaver()
    
    # Compile the graph
    app = workflow.compile(checkpointer=memory)
    
    logger.info(f"Simple chatbot agent created with model: {model_name}")
    return app

# Create the graph instance for easy importing
graph = create_graph()