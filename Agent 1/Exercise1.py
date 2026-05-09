from typing import Dict, TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str

def greeting_node(state: AgentState) -> AgentState:
    """A simple node that respond to bob's message."""

    state['name'] = state['name']+ ", You are doing an amazing job learning Lang Graph"
    return state

graph = StateGraph(AgentState)

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result = app.invoke({"name": "bob"})

print(result["name"])


