from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    number1: int 
    operation: str
    number2: int
    finalNumber: int
    number3: int
    operation2: str
    number4: int
    finalNumber2: int




def adder(state:AgentState) -> AgentState:
    """This node adds the 2 numbers"""
    print("adder")
    state["finalNumber"] = state["number1"] + state["number2"]
    return state

def subtractor(state:AgentState) -> AgentState:
    """This node subtracts the 2 numbers"""
    print("subtractor")
    state["finalNumber"] = state["number1"] - state["number2"]
    return state

def decide_next_node(state:AgentState) -> AgentState:
    """This node will select the next phase"""
    if state["operation"] == "+":
        return "addition_operation"
    
    elif state["operation"] == "-":
        print("SUB 1")
        return "subtraction_operation"   


def adder2(state:AgentState) -> AgentState:
    """This node adds the 2 numbers"""
    print("adder1")
    state["finalNumber2"] = state["number3"] + state["number4"]
    print(state["finalNumber2"])

    return state

def subtractor2(state:AgentState) -> AgentState:
    """This node subtracts the 2 numbers"""
    print("subtractor1")
    state["finalNumber2"] = state["number3"] - state["number4"]
    print(state["finalNumber2"])
    return state

def decide_next_node1(state:AgentState) -> AgentState:
    """This node will select the next phase"""
    if state["operation2"] == "+":
        print("ADD1")
        return "addition_operation2"
    
    elif state["operation2"] == "-":
        return "subtraction_operation2"   




# Se crea el grafo con el esquema de estado de dos fases.
graph = StateGraph(AgentState)

# Nodos de Fase 1:
# - add_node: suma number1 + number2
# - subtract_node: resta number1 - number2
# - router: nodo de entrada que pasa el estado sin cambios
graph.add_node("add_node", adder)
graph.add_node("subtract_node", subtractor)
graph.add_node("router", lambda state:state)  # Nodo passthrough Fase 1.

# Nodos de Fase 2:
# - add_node2: suma number3 + number4
# - subtract_node2: resta number3 - number4
# - router2: nodo de paso a Fase 2 sin cambios
graph.add_node("add_node2", adder2)
graph.add_node("subtract_node2", subtractor2)
graph.add_node("router2", lambda state:state)  # Nodo passthrough Fase 2.

# El grafo comienza en router (inicio de Fase 1).
graph.add_edge(START, "router")

# Bordes condicionales Fase 1: router -> decide_next_node -> add_node o subtract_node
graph.add_conditional_edges(
    "router",  # Nodo de origen.
    decide_next_node,  # Función decisora (evalúa 'operation').
    {
        # Mapeo: valores retornados por decide_next_node -> nodos destino
        "addition_operation": "add_node",
        "subtraction_operation": "subtract_node"
    }
)

# Ambos nodos de Fase 1 llevan a router2 (inicio de Fase 2).
graph.add_edge("add_node", "router2")
graph.add_edge("subtract_node", "router2")

graph.add_conditional_edges(
    "router2", 
    decide_next_node1,
    {
        "addition_operation2": "add_node2",
        "subtraction_operation2": "subtract_node2"
    }
)

graph.add_edge("add_node2", END)
graph.add_edge("subtract_node2", END)

app = graph.compile()


initial_state = AgentState(number1 = 10, operation="-", number2 = 5, 
                        number3 = 7, number4=2, operation2="+", finalNumber= 0, finalNumber2 = 0)


print(app.invoke(initial_state))







