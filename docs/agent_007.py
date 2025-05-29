from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_community.chat_models import ChatOllama
from typing import TypedDict, Annotated, Sequence
from operator import add as add_messages


class AgentState(TypedDict):
    messages: Annotated[Sequence[HumanMessage | AIMessage], add_messages]

llm_model = ChatOllama(model="gemma:2b", temperature=0.7)

system_prompt = SystemMessage(
    content="You are a helpful, general-purpose AI assistant. Answer clearly and politely."
)

def llm_node(state: AgentState) -> AgentState:
    messages = [system_prompt] + list(state["messages"])
    response = llm_model.invoke(messages)
    return {"messages": [response]}

# === Graph Setup ===
graph = StateGraph(AgentState)
graph.add_node("llm_model", llm_node)
graph.set_entry_point("llm_model")
graph.set_finish_point("llm_model")

bot = graph.compile()

def run_bot():
    print("agent007  \n exit or bye to close")
    history = []

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "bye"]:
            break

        user_msg = HumanMessage(content=user_input)
        history.append(user_msg)

        result = bot.invoke({"messages": history})
        ai_msg = result["messages"][-1]
        print(f"\nAI: {ai_msg.content}")

        history.append(ai_msg)

run_bot()
