# LangChain Learning Repository

![LangChain Academy](<https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/66e9eba1020525eea7873f96_LCA-big-green%20(2).svg>)

A comprehensive collection of projects, tutorials, and examples for learning LangChain, LangGraph, and related technologies for building powerful AI applications.

## Overview

This repository contains multiple projects and modules designed to help you learn LangChain ecosystem technologies, including:

-   **LangChain**: Framework for developing applications with language models
-   **LangGraph**: Tools for building agent and multi-agent applications
-   **RAG (Retrieval Augmented Generation)**: Techniques for enhancing LLM outputs with relevant context
-   **Multi-agent Systems**: Collaborative agent architectures for complex tasks

Perfect for beginners and experienced developers looking to master modern AI application development.

## Learning Modules

-   **LangGraph Modules**: Progressive introduction to building agent workflows
-   **RAG Implementation**: Learn to build retrieval-augmented generation systems
-   **Multi-agent Patterns**: Study and implement various agent collaboration techniques
-   **Practical Examples**: Real-world use cases like research assistants and map-reduce operations

## Prerequisites

-   Python 3.11 or later
-   OpenAI API key (for most examples)
-   Basic understanding of Python and machine learning concepts

## Installation

1. Clone the repository:

```bash
git clone https://github.com/langchain-ai/langchain-academy.git
cd langchain-academy
```

2. Create and activate a virtual environment:

For Mac/Linux/WSL:

```bash
python3 -m venv lc-academy-env
source lc-academy-env/bin/activate
```

For Windows PowerShell:

```powershell
python3 -m venv lc-academy-env
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
lc-academy-env\scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Set up the required API keys:

For Mac/Linux/WSL:

```bash
export OPENAI_API_KEY="your-api-key-here"
export LANGCHAIN_API_KEY="your-api-key-here"
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_PROJECT="langchain-academy"
export TAVILY_API_KEY="your-api-key-here"
```

For Windows PowerShell:

```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
$env:LANGCHAIN_API_KEY = "your-api-key-here"
$env:LANGCHAIN_TRACING_V2 = "true"
$env:LANGCHAIN_PROJECT = "langchain-academy"
$env:TAVILY_API_KEY = "your-api-key-here"
```

Alternatively, create a `.env` file and use the `python-dotenv` library.

## Project Structure

-   `langGraph/`: Modules focused on LangGraph concepts and applications
    -   `module-0/`: Basic setup and introduction
    -   `module-1/` to `module-4/`: Progressive LangGraph concepts
    -   `module-*/studio/`: LangGraph Studio compatible graphs
-   `langchain-course/`: Additional course materials and LangChain examples
    -   `4_RAGs/`: Retrieval Augmented Generation implementations
-   `Play_Ground/`: Experimental area for testing concepts

## Running the Learning Materials

Most learning materials are in Jupyter notebooks. If you don't have Jupyter installed:

```bash
pip install jupyter
jupyter notebook
```

## Advanced Tools (Optional)

### LangGraph Studio Setup (macOS only)

For visual development of agent graphs:

1. Download the latest `.dmg` file from [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio)
2. Install Docker Desktop for Mac
3. Create necessary `.env` files in the module directories

### LangSmith Integration

For tracing, monitoring, and debugging:

-   Sign up at [LangSmith](https://smith.langchain.com/)
-   Set environment variables as shown above

## Learning Path Recommendation

1. Start with basic LangChain concepts in `langchain-course/`
2. Progress to RAG implementations
3. Move to LangGraph modules in order (0→4)
4. Experiment with your own projects in the playground

## Resources

-   [LangChain Documentation](https://python.langchain.com/)
-   [LangSmith Documentation](https://docs.smith.langchain.com/)
-   [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
-   [Tavily API Documentation](https://tavily.com/)
