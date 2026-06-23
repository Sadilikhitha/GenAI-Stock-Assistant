# GenAI Stock Assistant

## Overview

GenAI Stock Assistant is an LLM-powered web application that provides real-time stock news and market insights through a conversational interface. The application uses Google's Gemini API along with a tool-calling architecture to understand user queries, retrieve relevant stock news, and generate intelligent responses.

The system follows a Plan → Action → Observe → Output workflow, enabling the AI assistant to reason about user requests and fetch accurate financial information using external APIs.

---

## Features

* Real-time stock news retrieval
* Conversational AI interface
* LLM-powered query understanding
* Tool-calling architecture
* Company-specific news search
* Interactive web application
* Intelligent response generation

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI Model

* Google Gemini API (LLM)

### APIs

* NewsAPI

### Libraries

* Requests
* Python-dotenv

---

## Project Architecture

```text
User
 │
 ▼
Web Interface (HTML/CSS/JS)
 │
 ▼
Flask Backend
 │
 ▼
Gemini LLM
 │
 ▼
Tool Selection
 │
 ▼
NewsAPI
 │
 ▼
Stock News Results
 │
 ▼
AI Generated Response
```

---

## Workflow

### Step 1

User enters a query.

Example:

```text
Latest news about Tesla
```

### Step 2

Gemini analyzes the query.

### Step 3

The AI selects the appropriate tool.

```text
get_stock_news()
```

### Step 4

NewsAPI fetches the latest company news.

### Step 5

The news data is returned to Gemini.

### Step 6

Gemini generates a user-friendly response.

---

## Example Queries

* Latest news about Tesla
* Show recent Apple news
* Give me news about Microsoft
* What are the latest updates on NVIDIA?
* Recent stock news about Amazon

---

## Project Structure

```text
GENAI_STOCK/
│
├── AI_agent/
│   ├── agent.py
│   └── tools.py
│
├── templates/
│   └── index.html
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
STOCK_API_KEY=your_newsapi_key
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd GENAI_STOCK
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Key Highlights

* Built using Google's Gemini Large Language Model (LLM)
* Implemented custom tool-calling architecture
* Integrated real-time stock news retrieval
* Developed an interactive Flask web application
* Designed a Plan → Action → Observe → Output agent workflow

---

## Future Enhancements

* Real-time stock price tracking
* Stock market charts and visualizations
* Portfolio management
* News sentiment analysis
* Multi-company comparison
* Financial report summarization
* User authentication and chat history

---

## Author

Sadi Likhitha 

B.Tech Information Technology
