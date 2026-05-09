from typing import List, TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    skills: List[str]
    name: str
    age: str
    final : str


def first_node(state: AgentState) -> AgentState:
    """ this is the first node of our sequence"""

    state['final'] = f"{state ["name"]}, welcome to the system! "
    return state

def second_node(state: AgentState) -> AgentState:
    """ this is the second node of our sequence"""

    state['final'] = state['final'] +  f"You are {state ['age']} years old! "
    return state

def third_node(state: AgentState) -> AgentState:
    """ this is the third node of our sequence"""

    state['final'] = state['final'] + f"Your skills are: {', '.join(state ['skills'])}! "
    return state



graph =  StateGraph(AgentState)

# Se registran los tres nodos que se ejecutarán en secuencia.
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.add_node("third_node", third_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.add_edge("second_node", "third_node")
graph.set_finish_point("third_node")

app = graph.compile()




result = app.invoke({"name": "charlie", "age": "20", "skills": ["Python", "JavaScript"]})
print (result)


