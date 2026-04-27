"""Tools for the simple_chatbot."""

from langchain.tools import tool
import logging

logger = logging.getLogger(__name__)

# For a simple chatbot, we don't need external tools
# The agent will rely primarily on the LLM for conversation
# This file is present for consistency with the agent structure

async def get_mcp_tools():
    """Load tools from the MCP server.
    
    Returns:
        Empty list as we don't use external tools for this simple chatbot
    """
    logger.info("Loading MCP tools (none for simple chatbot)")
    return []

# Placeholder for potential future tools
# @tool
# def example_tool(parameter: str) -> str:
#     """
#     Example tool that could be added later.
#     
#     Args:
#         parameter: Description of the parameter
#         
#     Returns:
#         Description of the return value
#     """
#     # Implementation would go here
#     return f"Processed: {parameter}"