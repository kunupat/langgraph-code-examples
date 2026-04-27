---
name: mastering-langgraph
description: Build stateful AI agents and agentic workflows with LangGraph in Python using a methodological 5-step thinking process. Covers tool-using agents with LLM-tool loops, branching workflows, conversation memory, human-in-the-loop oversight, and production monitoring. Use when - (1) building agents that use tools and loop until task complete, (2) creating multi-step workflows with conditional branches, (3) adding persistence/memory across turns with checkpointers, (4) implementing human approval with interrupt(), (5) debugging via time-travel or LangSmith. This skill guides conversations through the proven methodology at https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph: map workflow steps, identify step types, design state, build nodes, and wire together. Covers StateGraph, nodes, edges, add_conditional_edges, MessagesState, thread_id, Command objects, and ToolMessage handling. Examples include chatbots, calculator agents, and structured workflows.
license: MIT
metadata:
  version: 1.0.0
  framework: LangGraph
  python: ">=3.9"
  methodology: 5-step-thinking-process
  reference_url: https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph
---

# LangGraph Development Guide

Build stateful AI agents and workflows by defining graphs of nodes (steps) connected by edges (transitions).

## Contents

- [Building a New Agent](#building-a-new-agent)
- [The 5-Step Thinking Process](#the-5-step-thinking-process)
- [How to Use This Skill](#how-to-use-this-skill)
- [Quick Start](#quick-start)
- [Common Build Scenarios](#common-build-scenarios)
- [Core Principles](#core-principles)
- [Development Workflow](#development-workflow)
- [Common Pitfalls](#common-pitfalls)
- [Environment Setup](#environment-setup)
- [Quick Verification](#quick-verification)
- [API Essentials](#api-essentials)
- [Next Steps](#next-steps)

## Building a New Agent

This codebase uses a standardized structure for creating new LangGraph agents. All agents are built in the `src/` folder with a consistent three-file architecture for maintainability and scalability.

### Project Structure

All agents must be created as folders inside the `src/` directory following this pattern:

```
src/
  your_agent_name/
    __init__.py
    graph.py          # Agent orchestration and graph construction
    tools.py          # Tool definitions and integrations
    prompts.py        # System prompts and instructions
```

### Getting Started

To create a new agent named `my_custom_agent`:

1. **Create the agent folder** in the `src/` directory:
   ```bash
   mkdir src/my_custom_agent
   touch src/my_custom_agent/__init__.py
   ```

2. **Create the three core files** (`graph.py`, `tools.py`, `prompts.py`) - see detailed instructions below.

3. **Add this import** to `src/my_custom_agent/__init__.py` to make the agent importable:
   ```python
   from my_custom_agent.graph import create_graph
   ```

### File Descriptions & Templates

#### 1. **prompts.py** — Agent Instructions and Behavior

This file contains all the textual instructions and prompts that define your agent's behavior and communication style. It serves as the "brain" of agent instructions.

**Responsibilities:**
- System instructions and agent personality/role definition
- Workflow instructions (step-by-step processes the agent follows)
- Tool descriptions and usage guidelines
- Constraints, safety guidelines, and operational rules
- Prompt templates for different agent modes or scenarios

**Use when:**
- You need to change agent behavior or communication style
- You want to add new instructions or workflows
- You need to describe tools to the agent
- You want to customize agent constraints

**Example structure:**
```python
"""Prompt templates and instructions for the my_custom_agent."""

SYSTEM_INSTRUCTIONS = """
You are a specialized agent designed for [YOUR_PURPOSE].

Your role is to:
- [Goal 1]
- [Goal 2]
- [Goal 3]
"""

WORKFLOW_INSTRUCTIONS = """
Follow this workflow:

1. **Step 1**: [Description and guidelines]
2. **Step 2**: [Description and guidelines]
3. **Step 3**: [Description and guidelines]
"""

TOOL_GUIDELINES = """
When using tools:
- [Tool constraint 1]
- [Tool constraint 2]
"""
```

#### 2. **tools.py** — Tool Definitions and Integrations

This file contains all the tools your agent can use. It's responsible for loading external tools (from MCP servers, APIs) and implementing custom tools.

**Responsibilities:**
- Load tools from MCP servers or external APIs
- Define custom tools specific to your agent's domain
- Tool implementations with proper function signatures using `@tool` decorator
- Tool parameter validation and error handling
- Tool helper functions for common operations

**Use when:**
- You need to add new capabilities to your agent
- You want to integrate with external APIs or services
- You need to define domain-specific tools
- You want to add web search, data retrieval, or computation capabilities

**Example structure:**
```python
"""Tools for the my_custom_agent."""

from langchain.tools import tool
import logging

logger = logging.getLogger(__name__)

async def get_mcp_tools():
    """Load tools from the MCP server."""
    # Example: Load tools from external FastMCP server
    # Return list of LangChain-compatible tools

@tool
def custom_tool_1(parameter: str) -> str:
    """
    Description of what this tool does.
    
    Args:
        parameter: Description of the parameter
        
    Returns:
        Description of the return value
    """
    # Implementation
    return result

@tool
def custom_tool_2(data: dict) -> dict:
    """Another custom tool with specific functionality."""
    # Implementation
    return result
```

#### 3. **graph.py** — Agent Orchestration and Graph Building

This is the main execution file that puts everything together. It orchestrates the LLM, loads tools and prompts, and builds the compiled agent graph.

**Responsibilities:**
- Load environment variables and initialize configuration
- Initialize the LLM (language model)
- Load tools from `tools.py` and integrate them
- Build system prompts using `prompts.py`
- Create and compile the LangGraph agent
- Set up logging and monitoring
- Provide the `create_graph()` function as the main entry point

**Use when:**
- You need to change the core agent logic or graph structure
- You want to add new nodes or edges to the workflow
- You need to modify LLM behavior or model selection
- You want to integrate with monitoring/tracing systems
- You need to adjust how tools are bound to the LLM

**Example structure:**
```python
"""LangGraph agent with tool integration."""

import logging
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

from my_custom_agent.prompts import (
    SYSTEM_INSTRUCTIONS,
    WORKFLOW_INSTRUCTIONS,
)
from my_custom_agent.tools import (
    get_mcp_tools,
    custom_tool_1,
    custom_tool_2,
)

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(env_path, override=True)

logger = logging.getLogger(__name__)

def create_graph():
    """Create and configure the agent graph.
    
    Returns:
        Compiled LangGraph agent.
    """
    logger.info("Initializing agent...")
    
    # Initialize LLM
    llm = ChatOllama(model="your-model-name")
    
    # Load tools
    tools = []
    tools.extend(asyncio.run(get_mcp_tools()))
    tools.append(custom_tool_1)
    tools.append(custom_tool_2)
    
    # Build system prompt
    system_prompt = f"{SYSTEM_INSTRUCTIONS}\n\n{WORKFLOW_INSTRUCTIONS}"
    
    # Create and compile agent
    agent = create_agent(llm, tools, system_prompt)
    
    logger.info(f"Agent created with {len(tools)} tools")
    return agent
```

### Best Practices for New Agents

1. **Modularity**: Keep prompts, tools, and graph logic separate:
   - Don't put tool definitions in `graph.py`
   - Don't put prompts in `tools.py`
   - Don't hardcode instructions in code

2. **Reusability**: Reference existing agents (`agent/`, `deep_agent/`, `deep_agent_with_skills/`) as templates:
   - `agent/` — Start here for simple ReAct agents
   - `deep_agent/` — For agents with complex workflows and sub-agents
   - `deep_agent_with_skills/` — For agents with specialized skill modules

3. **Documentation**: Every function should have a docstring explaining:
   - What it does
   - Input parameters and types
   - Return values and types
   - Any side effects or important behaviors

4. **Error Handling**: Add robust error handling in `graph.py`:
   - Handle missing environment variables
   - Manage API failures gracefully
   - Log important events and errors

5. **Environment Setup**: Create a `.env` file in the project root with required variables:
   ```bash
   # Example .env
   OLLAMA_MODEL=llama2
   MCP_SERVER_URL=http://localhost:8000/mcp
   API_KEY=your-api-key
   ```

### Running Your Agent

From the `agents/` directory:

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the agent in development mode
langgraph dev

# Or import and run directly
python -c "from my_custom_agent import create_graph; agent = create_graph(); print(agent.invoke({'input': 'your question'}))"
```

## The 5-Step Thinking Process

When helping users build LangGraph agents, **always fetch and reference** the official methodology guide at: https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph

This guide describes a proven 5-step approach that should structure all LangGraph agent development conversations:

### Step 1: Start with the Process You Want to Automate
**Your role:** Ask clarifying questions to understand the user's automation goals, requirements, and success criteria.
- What is the overall process or workflow they want to automate?
- What are the inputs and desired outputs?
- Who are the users and what problems does this solve?
- Are there existing manual processes to improve?

### Step 2: Map Out Workflow as Discrete Steps
**Your role:** Help the user decompose the process into distinct nodes (steps), each doing one thing well.
- Identify core operations (e.g., Read Email, Classify Intent, Search Docs, etc.)
- Sketch the workflow showing possible paths and decision points
- Clarify which nodes make routing decisions vs. proceed linearly
- Use a visual representation (text-based diagram or description)

### Step 3: Identify What Each Step Needs to Do
**Your role:** Categorize each node by type and ensure the user understands what work it performs.

Each step falls into one of four categories:
- **LLM steps**: Understand, analyze, generate text, or make reasoning decisions
- **Data steps**: Retrieve information from external sources
- **Action steps**: Perform external actions or systems calls
- **User input steps**: Require human intervention or approval

Ask: "For each node, what type is it, and what external resources does it need?"

### Step 4: Design Your State
**Your role:** Guide the user to define what data persists across the workflow.

Key principle: **Keep state raw, format prompts on-demand**
- Ask: "What data needs to persist between steps?"
- Ensure state contains facts, not formatted prompts
- Each node can format shared data as needed
- Use TypedDict to define the state schema clearly

### Step 5: Build Your Nodes and Wire Together
**Your role:** Help implement each node and connect them into a working graph.

- Each node is a Python function: `def node(state: State) -> dict`
- Implement error handling: retries for transient failures, loop-back for LLM-recoverable errors, interrupt() for user input
- Wire nodes with edges (connections)
- Compile the graph with a checkpointer for persistence and human-in-the-loop

## How to Use This Skill

**When a user asks to build a LangGraph agent:**

1. **Fetch the reference**: Retrieve the content from https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph to stay aligned with the official methodology.

2. **Guide through the 5 steps methodically**: Don't jump to code immediately. Walk the user through each step in order:
   - Clarify their use case (Step 1)
   - Help them map the workflow (Step 2)
   - Categorize node types (Step 3)
   - Design state together (Step 4)
   - Build and wire together (Step 5)

3. **Stir the conversation strategically**: Ask targeted questions to help the user discover insights:
   - "What are the discrete operations in this process?"
   - "Which steps involve LLM reasoning vs. data retrieval vs. external actions?"
   - "What information needs to persist across all steps?"
   - "Where might humans need to intervene?"
   - "How should errors in each step be handled?"

4. **Reference the methodology**: When explaining concepts, cite the 5-step process. Say things like:
   - "Following the methodology at [reference], let's first map out your workflow..."
   - "In Step 3 of the thinking process, we categorize each node..."
   - "This aligns with Step 4 of the official guide—designing your state..."

5. **Provide code incrementally**: Generate code only after clarifying Steps 1–4. Then implement Step 5 (nodes + graph wiring).

6. **Emphasize key principles from the reference**:
   - Break into discrete steps
   - State is shared memory (keep it raw)
   - Nodes are functions
   - Errors are part of the flow
   - Human input is first-class
   - Graph structure emerges naturally

## Quick Start

Minimal chatbot with memory:

```python
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AnyMessage
from typing_extensions import TypedDict, Annotated
import operator

# 1. Define state
class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]  # Append mode

# 2. Define node
llm = ChatOpenAI(model="gpt-4")

def chat(state: State) -> dict:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

# 3. Build graph
graph = StateGraph(State)
graph.add_node("chat", chat)
graph.add_edge(START, "chat")
graph.add_edge("chat", END)

# 4. Compile with memory
chain = graph.compile(checkpointer=InMemorySaver())

# 5. Invoke with thread_id for persistence
result = chain.invoke(
    {"messages": [HumanMessage(content="Hello!")]},
    config={"configurable": {"thread_id": "user-123"}}
)
print(result["messages"][-1].content)
```

Key patterns:
- `Annotated[list, operator.add]` — append to list instead of replace
- `InMemorySaver()` — enables memory across invocations
- `thread_id` — identifies conversation for persistence

## Common Build Scenarios

### Simple Chatbot / Q&A
The Quick Start above covers this. Add more nodes for preprocessing or postprocessing as needed.

### Tool-Using Agent
Agent that calls external tools (APIs, calculators, search) in a loop until task complete.
→ See [references/tool-agent-pattern.md](references/tool-agent-pattern.md)

### Structured Workflow
Multi-step pipeline with conditional branches, parallel execution, or prompt chaining.
→ See [references/workflow-patterns.md](references/workflow-patterns.md)

### Agent with Long-Term Memory
Persist conversation across sessions, enable time-travel debugging, survive crashes.
→ See [references/persistence-memory.md](references/persistence-memory.md)

### Human-in-the-Loop
Pause for human approval, correction, or additional input mid-workflow.
→ See [references/hitl-patterns.md](references/hitl-patterns.md)

### Debugging / Production Monitoring
Unit test nodes, visualize graphs, trace with LangSmith.
→ See [references/debugging-monitoring.md](references/debugging-monitoring.md)

### Multi-Agent Systems
Build supervisor or swarm-based multi-agent workflows with handoff tools.
→ See [references/multi-agent-patterns.md](references/multi-agent-patterns.md)

### Production Deployment
Deploy to LangGraph Platform (cloud/self-hosted) or custom infrastructure.
→ See [references/production-deployment.md](references/production-deployment.md)

### New to LangGraph?
Learn core concepts: State, Nodes, Edges, Graph APIs.
→ See [references/core-api.md](references/core-api.md)

## Core Principles

### 1. Keep State Raw
Store facts, not formatted prompts. Each node can format data as needed.

```python
# ✓ Good: raw data
class State(TypedDict):
    user_question: str
    retrieved_docs: list[str]
    intent: str

# ✗ Bad: pre-formatted
class State(TypedDict):
    full_prompt: str  # Mixes data with formatting
```

### 2. Single-Purpose Nodes
Each node does one thing. Name it descriptively.

```python
# ✓ Good: clear responsibilities
graph.add_node("classify_intent", classify_intent)
graph.add_node("search_knowledge", search_knowledge)
graph.add_node("generate_response", generate_response)
```

### 3. Explicit Routing
Use conditional edges for decisions. Don't hide routing logic inside nodes.

```python
def route_by_intent(state) -> str:
    if state["intent"] == "billing":
        return "billing_handler"
    return "general_handler"

graph.add_conditional_edges("classify", route_by_intent, 
    ["billing_handler", "general_handler"])
```

### 4. Use Aggregators for Lists
Any list field that accumulates values needs `operator.add`:

```python
class State(TypedDict):
    messages: Annotated[list, operator.add]      # ✓ Appends
    current_step: str                             # Replaces (no annotation)
```

### 5. Handle Errors Deliberately

| Error Type | Strategy |
|------------|----------|
| Transient (network) | Use `RetryPolicy` on node |
| LLM-recoverable (parse fail) | Feed error to LLM via state, loop back |
| User-fixable (missing info) | Use `interrupt()` to pause and ask |
| Unexpected (bugs) | Let bubble up for debugging |

## Development Workflow

1. **Define Steps** — Break task into discrete operations (each becomes a node)
2. **Categorize Steps** — LLM call? Data retrieval? Action? User input?
3. **Design State** — TypedDict with all needed fields; keep it raw
4. **Implement Nodes** — `def node(state) -> dict` for each step
5. **Connect Graph** — `add_node()`, `add_edge()`, `add_conditional_edges()`
6. **Compile & Test** — `graph.compile()`, test with sample inputs

## Common Pitfalls

### 1. Forgetting `operator.add` on Lists
**Symptom:** Messages disappear, only last message retained.
```python
# ✗ Wrong: messages: list[AnyMessage]
# ✓ Fix: messages: Annotated[list[AnyMessage], operator.add]
```

### 2. Missing `thread_id` for Memory
**Symptom:** Agent forgets previous turns.
```python
# ✓ Fix: Always pass config with thread_id
chain.invoke(input, config={"configurable": {"thread_id": "unique-id"}})
```

### 3. Not Compiling Before Invoke
**Symptom:** AttributeError on graph object.
```python
# ✗ Wrong: graph.invoke(input)
# ✓ Fix: chain = graph.compile(); chain.invoke(input)
```

### 4. Non-Deterministic Nodes Without @task
**Symptom:** Different results on resume from checkpoint.
```python
from langgraph.func import task

@task  # Wrap for durable execution
def fetch_data(state):
    return {"data": requests.get(url).json()}
```

### 5. Circular Imports with Type Hints
**Symptom:** ImportError when defining state classes.
```python
# ✓ Fix: Use string annotations
from __future__ import annotations
```

## Environment Setup

```bash
# Core
pip install -U langgraph

# LLM providers (pick one or more)
pip install langchain-openai
pip install langchain-anthropic

# Production persistence
pip install langgraph-checkpoint-postgres

# Observability
pip install langsmith
```

Environment variables:
```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export LANGSMITH_API_KEY="ls-..."
export LANGSMITH_TRACING=true
```

## Quick Verification

### Before Building
- [ ] `python -c "import langgraph; print(langgraph.__version__)"` works
- [ ] LLM API key set (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`)
- [ ] Optional: `LANGSMITH_API_KEY` for tracing

### After Building
- [ ] Graph compiles without error: `chain = graph.compile()`
- [ ] Visualization renders: `print(chain.get_graph().draw_mermaid())`
- [ ] Invoke succeeds with sample input: `chain.invoke({...})`
- [ ] Lists accumulate correctly (verify `operator.add` annotations)
- [ ] Memory persists across invocations (test same `thread_id` twice)
- [ ] Conditional routing works as expected (test each branch)

## API Essentials

```python
# Imports
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from typing_extensions import TypedDict, Annotated
import operator

# State with append-mode list
class State(TypedDict):
    messages: Annotated[list, operator.add]

# Node signature
def node(state: State) -> dict:
    return {"messages": [new_message]}

# Graph construction
graph = StateGraph(State)
graph.add_node("name", node_fn)
graph.add_edge(START, "name")
graph.add_edge("name", END)

# Conditional routing
graph.add_conditional_edges("from", router_fn, ["option1", "option2", END])

# Compile and run
chain = graph.compile(checkpointer=InMemorySaver())
result = chain.invoke(input, config={"configurable": {"thread_id": "id"}})

# Visualization
print(chain.get_graph().draw_mermaid())
```

For detailed API reference → See [references/core-api.md](references/core-api.md)

## Next Steps

- **Tool agents**: [references/tool-agent-pattern.md](references/tool-agent-pattern.md)
- **Workflows**: [references/workflow-patterns.md](references/workflow-patterns.md)
- **Persistence**: [references/persistence-memory.md](references/persistence-memory.md)
- **Human-in-the-loop**: [references/hitl-patterns.md](references/hitl-patterns.md)
- **Testing/Monitoring**: [references/debugging-monitoring.md](references/debugging-monitoring.md)
- **Multi-agent**: [references/multi-agent-patterns.md](references/multi-agent-patterns.md)
- **Production**: [references/production-deployment.md](references/production-deployment.md)
- **Core concepts**: [references/core-api.md](references/core-api.md)
- **Official docs**: [references/official-resources.md](references/official-resources.md)
