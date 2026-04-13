# AI Tutor Learning Project Backend 🤖📚

An intelligent **AI-powered learning backend system** built using **Python**, **FastAPI**, **Ollama**, and **MCP client integration**.

This project powers an **AI Learning / Tutor application** designed for **subject-wise and class-wise guided learning**. It helps students select a subject, choose their learning level or class, and receive **step-by-step concept explanations, topic progression, and future quiz support**.

The backend processes user queries, routes them through an agent pipeline, interacts with local LLM models, and returns **structured tutoring responses based on subject, class, topic, and learning goal**.

---

## 🚀 Features

* AI-powered subject-wise tutoring backend
* FastAPI REST API server
* local LLM inference using Ollama
* agent-based response orchestration
* MCP server tool integration
* prompt engineering for adaptive tutoring
* topic-wise learning flow
* next topic recommendation
* scalable modular backend design

---

## 🎯 Learning Flow

The application supports a guided learning experience:

* select **AI topic**
* choose **learning level**
* get detailed explanation
* move to **next recommended topic**
* future support for **quiz + short questions**

Example:

```text
Subject: Machine Learning
Class / Level: Beginner
Topic: Linear Regression
Goal: AI Deep Learning
```

---

## 🛠 Tech Stack

* **Python**
* **FastAPI**
* **Ollama**
* **MCP Client**
* **REST API**
* **Prompt Engineering**
* **Async / Await**
* **Uvicorn**
* **Qdrant (future integration)**

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
├── master_prompt.txt
├── tutor_model.py
├── requirement.txt
└── README.md
```

---

## 📁 File Description

### `main.py`

Main FastAPI server entry point.

Responsible for:

* creating tutoring API endpoints
* handling incoming student requests
* returning AI learning responses

---

### `agent.py`

Core AI agent logic.

Responsible for:

* processing student query
* managing tutoring prompt flow
* integrating MCP tools
* calling LLM layer
* handling next topic flow

---

### `llm_ollama.py`

Handles communication with **Ollama local LLM model**.

Responsible for:

* model invocation
* prompt execution
* response generation
* concept explanation

---

### `mc_client.py`

Responsible for MCP server communication.

Used for:

* listing tools
* calling external MCP tools

  SSE connection handling
* future RAG support

---

### `prompt.py`

Contains prompt templates and tutoring instructions.

Used for:

* Topic-wise responses
* level-based explanations
* prompt customization

---

## ⚙️ Architecture Flow

```text
Student Request
      ↓
FastAPI Endpoint
      ↓
Agent Layer
      ↓
Prompt Builder
      ↓
Ollama / MCP Tools
      ↓
Structured Learning Response
      ↓
Client Response
```

---

## 📡 API Endpoint

### Tutor Learning API

```http
POST /ask
```

### Request

```json
{
  "subject": "Machine Learning",
  "level": "Beginner",
  "goal": "AI Deep Learning",
  "topic": "Linear Regression",
  "user_query": "Teach me linear regression step by step"
}
```

### Response

```json
{
  "response": "1. Concept Explanation ... 2. Formula / Theory ..."
}
```

---

## ▶️ How to Run

### 1. Clone project

```[bash
https://github.com/sonimishraa/AI_Tutor_Client_Server.git
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

* Android AI learning app
* level tutor application
* subject-based education apps
* guided concept learning system
* AI topic progression system
* future quiz engine

---

## 🚀 Future Improvements

* quiz generation
* short-answer questions
* adaptive difficulty
* PDF question answering
* vector database integration
* chat memory history
* streaming responses
* voice tutoring support
* multilingual tutoring

---

## 👩‍💻 Developed By

**Mishra Soni**

AI / Android / Backend Developer
Kotlin | Python | FastAPI | LLM | Ollama | MCP
