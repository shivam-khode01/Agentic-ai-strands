# Agentic ai-strands
# level 1

A basic AI agent implementation using the Strands framework with Ollama integration. This project demonstrates how to create a simple AI agent powered by a local LLM (Large Language Model) that can respond to user queries.

## 🚀 Features

- **Simple AI Agent**: Basic agent implementation without tools
- **Local LLM Integration**: Uses Ollama for local model hosting
- **Strands Framework**: Built with the Strands AI framework
- **Easy Setup**: Minimal configuration required

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- Ollama installed and running locally
- The `strands` Python package
- Llama3 model downloaded in Ollama

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shivam-khode01/strandsAgents-persistent.git
   cd strands-agent
   ```

2. **Install required packages**
   ```bash
   pip install strands
   ```

3. **Install and setup Ollama**
   - Download Ollama from [https://ollama.ai](https://ollama.ai)
   - Install Ollama on your system
   - Pull the Llama3 model:
     ```bash
     ollama pull llama3
     ```
   - Start Ollama service:
     ```bash
     ollama serve
     ```

## 📁 Project Structure

```
strands-agent/
├── agent.py              # Main agent implementation
├── __init__.py           # Package initialization
├── setup_and_run.sh      # Automated setup and run script
├── README.md             # Project documentation
└── venv/                 # Virtual environment (created after setup)
```

## 💻 Usage

1. **Ensure Ollama is running**
   Make sure Ollama is running on `http://localhost:11434` with the Llama3 model available.

2. **Run the agent**
   ```bash
   python agent.py
   ```

3. **Expected Output**
   ```
   Hello, World!
   ```

## 🔧 Configuration

The agent is configured with the following settings:

- **Host**: `http://localhost:11434` (default Ollama endpoint)
- **Model**: `llama3` (you can change this to any model you have installed)

To use a different model, modify the `model_id` parameter in `agent.py`:

```python
ollama_model = OllamaModel(
    host="http://localhost:11434",  
    model_id="your-preferred-model"  # Change this
)
```

## 📝 Code Overview

### agent.py
The main file contains:
- Ollama model initialization
- Agent creation using the Strands framework
- A simple "Hello World" interaction

```python
from strands import Agent
from strands.models.ollama import OllamaModel

# Create Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  
    model_id="llama3"               
)

# Create an agent using the Ollama model
agent = Agent(model=ollama_model)

# Use the agent
agent("say hello World")
```

## 🎯 Sample Interactions

Here are some example interactions you can try:

**User Input**: "What are the principles of OOPS?"
**AI Response**: The agent will provide an explanation of Object-Oriented Programming principles using the underlying LLM's knowledge.

**User Input**: "Explain Python basics"
**AI Response**: The agent will explain Python programming fundamentals.

## 🔍 Troubleshooting

### Common Issues

1. **Connection Error**: 
   - Ensure Ollama is running: `ollama serve`
   - Check if the service is accessible at `http://localhost:11434`

2. **Model Not Found**:
   - Pull the required model: `ollama pull llama3`
   - Verify available models: `ollama list`

3. **Import Errors**:
   - Install strands: `pip install strands`
   - Check Python version compatibility

