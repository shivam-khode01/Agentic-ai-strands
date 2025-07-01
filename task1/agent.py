from strands import Agent
from strands.models.ollama import OllamaModel
#creating instance for ollama
ollama_model = OllamaModel(
    host="http://localhost:11434",  
    model_id="llama3"               
)

# Create an agent using the Ollama model
agent = Agent(model=ollama_model)

# Use the agent
agent("say hello World") 