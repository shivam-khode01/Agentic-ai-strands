from strands import Agent
from strands.agent.conversation_manager import SlidingWindowConversationManager
from strands.models.ollama import OllamaModel

model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3"
)

conversation_manager = SlidingWindowConversationManager(
    window_size=20,  
    should_truncate_results=True
)


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

print(agent("My name is Shivam and I am an engineering student interested in compiler design and ML. What are some good career options?"))
print(agent("What are some relevant textbooks that align with my interests?"))
print(agent("What companies should I target for internships or research roles?"))
