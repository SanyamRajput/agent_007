from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_community.chat_models import ChatOllama
from typing import TypedDict, Annotated, Sequence
from operator import add

class AgentState(TypedDict):
    messages: Annotated[Sequence[HumanMessage | AIMessage], add]

llm_model = ChatOllama(model="gemma:2b", temperature=0.7)
sys_prompt = SystemMessage(
    content="You are a helpful, general-purpose AI assistant. Answer clearly and politely."
)

def llm_node(state: AgentState) -> AgentState:
    messages = [sys_prompt] + list(state["messages"])
    response = llm_model.invoke(messages)
    return {"messages": [response]}

def create_agent():
    graph = StateGraph(AgentState)
    graph.add_node("llm_model", llm_node)
    graph.set_entry_point("llm_model")
    graph.add_edge("llm_model", END)
    return graph.compile()

bot = create_agent()

def run_bot():
    print("Agent007 Bot - Ready to assist!")
    print("Type 'exit' or 'bye' to quit the conversation.")
    print("-" * 50)
    
    history = []

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ["exit", "bye", "quit"]:
                print("\n007: Goodbye! Have a great day!")
                break
            
            if not user_input:
                print("Please enter a message or type 'exit' to quit.")
                continue

            user_msg = HumanMessage(content=user_input)
            history.append(user_msg)

            result = bot.invoke({"messages": history})
            ai_msg = result["messages"][-1]
            
            print(f"\n007: {ai_msg.content}")

            history.append(ai_msg)
            
        except KeyboardInterrupt:
            print("\n\n007: Conversation interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please try again or type 'exit' to quit.")

def ask_bot(question: str, conversation_history=None):
    if conversation_history is None:
        conversation_history = []
    
    user_msg = HumanMessage(content=question)
    messages = conversation_history + [user_msg]
    
    result = bot.invoke({"messages": messages})
    return result["messages"][-1].content


