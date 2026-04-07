# AI Tutor Backend Server 🤖📚

An intelligent **AI-powered tutoring backend system** built using **Python**, **FastAPI**, **Ollama**, and **MCP client integration**.

This project processes user queries, routes them through an agent pipeline, interacts with local LLM models, and returns subject-wise tutoring responses.

---

## 🚀 Features

- AI-powered tutoring backend
- FastAPI REST API server
- Local LLM inference using Ollama
- Agent-based response orchestration
- MCP server tool integration
- Prompt engineering for subject-wise tutoring
- Clean modular Python architecture
- Scalable backend design

---

## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **Ollama**
- **MCP Client**
- **REST API**
- **Prompt Engineering**
- **Async / Await**
- **Uvicorn**

---

## 📂 Project Structure

```bash
AI_Tutor_Backend/
│
├── agent.py
├── llm_ollama.py
├── main.py
├── mcp_client.py
├── prompt.py
├── requirement.txt
└── README.md
```

---

## 📁 File Description

### `main.py`
Main FastAPI server entry point.

Responsible for:
- creating API endpoints
- handling incoming chat requests
- returning AI responses

---

### `agent.py`
Core AI agent logic.

Responsible for:
- processing user query
- managing prompt flow
- integrating tools / MCP
- calling LLM layer

---

### `llm_ollama.py`
Handles communication with **Ollama local LLM model**.

Responsible for:
- model invocation
- prompt execution
- response generation

---

### `mcp_client.py`
Responsible for MCP server communication.

Used for:
- listing tools
- calling external MCP tools
- SSE connection handling

---

### `prompt.py`
Contains prompt templates and tutoring instructions.

Used for:
- subject-based responses
- class-wise tutoring logic
- prompt customization

---

## ⚙️ Architecture Flow

```text
Client Request
      ↓
FastAPI Endpoint
      ↓
Agent Layer
      ↓
Prompt Builder
      ↓
Ollama / MCP Tools
      ↓
AI Response
      ↓
Client Response
```

---

## 📡 API Endpoint

### Chat API

```http
POST /chat
```

### Request

```json
{
  "query": "Explain Newton's second law"
}
```

### Response

```json
{
  "answer": "Newton's second law states that force equals mass multiplied by acceleration..."
}
```

---

## ▶️ How to Run

### 1. Clone project

```bash
git clone https://github.com/yourusername/ai-tutor-backend.git
cd ai-tutor-backend
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

---

### 4. Start Ollama

```bash
ollama serve
```

Make sure model is available:

```bash
ollama pull qwen2.5:3b
```

---

### 5. Run server

```bash
uvicorn main:app --reload
```

Server runs on:

```text
http://127.0.0.1:8000
```

---

## 🔥 Use Cases

This backend can be used for:

- Android AI Tutor app
- Web tutoring application
- Chat-based education apps
- Subject-wise learning assistant
- Homework help system

---

## 🚀 Future Improvements

- PDF question answering
- vector database integration
- memory chat history
- streaming responses
- voice tutoring support
- multilingual tutoring
- quiz generation

---

## 👩‍💻 Developed By

**Mishra Soni**

AI / Android / Backend Developer  
Kotlin | Python | FastAPI | LLM | Ollama | MCP
