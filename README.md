# agent_007-chatbot
# 🤖 agent007 — General-Purpose AI Chatbot (LangGraph + Ollama)

`agent007` is a fast, local-first AI chatbot powered by [LangGraph](https://github.com/langchain-ai/langgraph) and [Ollama](https://ollama.com/). It uses state machine logic to structure interactions and can run entirely on your machine — no cloud dependencies.

---

## 🚀 Features

- 💬 General-purpose chatbot
- 🔄 Memory of past interactions (limited to reduce latency)
- ⚡️ Optimized for speed using lightweight local models
- 🧠 Built with LangGraph's stateful agent architecture
- 🛠 Easy to extend with tools or RAG (retrieval) later

---

## 📦 Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- A supported model (like `mistral`, `llama3`, or `phi3`) downloaded

---

## 📥 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/agent007.git
cd agent007
