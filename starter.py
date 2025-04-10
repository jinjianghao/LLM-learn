import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama


# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b


# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    llm=Ollama(model="gemma3:1b", request_timeout=360.0),
    system_prompt="You are a helpful assistant that can multiply two numbers.",
    name="CalculatorAgent",
    description="This agent can multiply two numbers."
)


async def main():
    try:
        print("Starting agent...")
        response = await agent.run("What is 1234 * 4567?")
        print(str(response))
        print("Agent finished.")
    except Exception as e:
        print(f"Error occurred: {e}")




# Run the agent
if __name__ == "__main__":
    asyncio.run(main())