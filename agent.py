from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2.5:3b")

class AgentState(TypedDict):
    task: str
    result: str

def assistant(state):

    task = state["task"]

    prompt = f"""
    Ты AI-помощник преподавателя НВТП.

    Помогай:
    - создавать тесты
    - генерировать планы уроков
    - объяснять темы
    - создавать тактические задания
    - делать вопросы для курсантов

    Запрос:
    {task}
    """

    response = llm.invoke(prompt)

    return {
        "result": response
    }

graph = StateGraph(AgentState)

graph.add_node("assistant", assistant)

graph.set_entry_point("assistant")

graph.add_edge("assistant", END)

app = graph.compile()