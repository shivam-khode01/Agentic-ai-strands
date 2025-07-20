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

---

# level 2

Building upon Level 1, this enhanced version adds conversational memory capabilities to the AI agent, allowing it to maintain context across multiple interactions and provide more personalized responses.

## 🚀 Additional Features (Level 2)

- **Conversational Memory**: Agent remembers previous interactions within a conversation
- **Sliding Window Memory**: Maintains a configurable number of recent messages
- **System Prompts**: Customizable AI personality and behavior
- **Context Awareness**: Builds upon user information across multiple turns
- **Memory Management**: Optimized performance with truncation options

## 📁 Updated Project Structure

```
strands-agent/
├── agent.py              # Level 1: Basic agent implementation
├── conversational_agent.py  # Level 2: Agent with conversational memory
├── __init__.py           # Package initialization
├── setup_and_run.sh      # Automated setup and run script
├── README.md             # Project documentation
└── venv/                 # Virtual environment (created after setup)
```

## 💻 Usage (Level 2)

1. **Ensure Ollama is running**
   Make sure Ollama is running on `http://localhost:11434` with the Llama3 model available.

2. **Run the conversational agent**
   ```bash
   python conversational_agent.py
   ```

3. **Expected Conversational Flow**
   The agent will engage in a multi-turn conversation, demonstrating memory across interactions.

## 🔧 Configuration (Level 2)

The conversational agent includes additional configuration options:

- **Memory Window Size**: Number of messages to retain (default: 20)
- **Result Truncation**: Option to truncate responses for memory efficiency
- **System Prompt**: Defines the AI's role and behavior

To modify these settings, update the parameters in `conversational_agent.py`:

```python
conversation_manager = SlidingWindowConversationManager(
    window_size=20,  # Adjust memory size
    should_truncate_results=True  # Enable/disable truncation
)
```

## 📝 Code Overview (Level 2)

### conversational_agent.py
Enhanced implementation with conversational memory:

```python
from strands import Agent
from strands.agent.conversation_manager import SlidingWindowConversationManager
from strands.models.ollama import OllamaModel

# Load Ollama model (e.g., llama3)
model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3"
)

# Create conversation manager with sliding memory
conversation_manager = SlidingWindowConversationManager(
    window_size=20,  # Max messages to retain in memory
    should_truncate_results=True
)

# Create Agent with system prompt
agent = Agent(
    model=model,
    conversation_manager=conversation_manager,
    system_prompt=(
        "You are a helpful and friendly AI career advisor assisting engineering students. "
        "If the user shares their background, interests, or goals, remember and build upon it "
        "in follow-up answers. Give actionable and detailed advice, especially in machine learning "
        "and compiler design if those topics come up."
    )
)

# Simulate conversation
print(agent("My name is Shivam and I am an engineering student interested in compiler design and ML. What are some good career options?"))
print(agent("What are some relevant textbooks that align with my interests?"))
print(agent("What companies should I target for internships or research roles?"))
```

## 🎯 Sample Interactions (Level 2)

### Multi-Turn Conversation Example

**Turn 1**: 
- **User**: "My name is Shivam and I am an engineering student interested in compiler design and ML. What are some good career options?"
- **AI**: Provides personalized career advice based on the specific interests mentioned, remembering the name and interests.

**Turn 2**: 
- **User**: "What are some relevant textbooks that align with my interests?"
- **AI**: Recommends books specifically for compiler design and ML, referencing the interests shared in Turn 1.

**Turn 3**: 
- **User**: "What companies should I target for internships or research roles?"
- **AI**: Suggests companies that align with compiler design and ML, building upon the complete context from previous turns.

## 🔍 Key Components (Level 2)

### SlidingWindowConversationManager
- **Purpose**: Manages conversation history and memory
- **Window Size**: Controls how many recent messages to retain
- **Truncation**: Optionally shortens responses to save memory
- **Context Preservation**: Maintains relevant information across turns

### System Prompt Design
The system prompt defines the AI's behavior:
- **Role Definition**: "AI career advisor"
- **Target Audience**: "engineering students"
- **Memory Instructions**: "remember and build upon" user information
- **Specialization**: Focus on "machine learning and compiler design"

## 🔧 Memory Management

### Window Size Considerations
- **Small Window (5-10)**: Fast performance, limited context
- **Medium Window (15-25)**: Balanced performance and context
- **Large Window (30+)**: Rich context, potential performance impact

### Truncation Benefits
- Reduces memory usage
- Maintains conversation flow
- Prevents context overflow

## 🚀 Advanced Usage (Level 2)

### Customizing System Prompts
```python
custom_prompt = (
    "You are an expert Python tutor. Remember student questions and "
    "build upon previous explanations. Focus on practical examples."
)

agent = Agent(
    model=model,
    conversation_manager=conversation_manager,
    system_prompt=custom_prompt
)
```

### Adjusting Memory Settings
```python
# For longer conversations
conversation_manager = SlidingWindowConversationManager(
    window_size=50,
    should_truncate_results=False
)

# For resource-constrained environments
conversation_manager = SlidingWindowConversationManager(
    window_size=10,
    should_truncate_results=True
)
```

## 🔍 Troubleshooting (Level 2)

### Memory-Related Issues

1. **High Memory Usage**:
   - Reduce `window_size` parameter
   - Enable `should_truncate_results`
   - Monitor conversation length

2. **Context Loss**:
   - Increase `window_size`
   - Check if important information fits within window
   - Consider conversation structure

3. **Performance Issues**:
   - Balance window size with performance needs
   - Enable truncation for faster responses
   - Monitor system resources

### Common Level 2 Issues

1. **Import Errors**:
   ```bash
   pip install --upgrade strands
   ```

2. **Conversation Manager Not Found**:
   - Verify strands version compatibility
   - Check import statements

3. **System Prompt Not Working**:
   - Ensure proper string formatting
   - Verify agent initialization order
