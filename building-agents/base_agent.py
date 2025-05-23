from dotenv import load_dotenv
load_dotenv()

from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import AgentWorkflow

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b

def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

llm = Ollama(model="qwen2.5:7b", request_timeout=60.0)

workflow = AgentWorkflow.from_tools_or_functions(
    [multiply, add],
    llm=llm,
    system_prompt="You are an agent that can perform basic mathematical operations using tools."
)

async def main():
    response = await workflow.run(user_msg="What is 20+(2*4)+2 ?")
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())