from llama_index.core.llms import ChatMessage, TextBlock, ImageBlock
from llama_index.llms.ollama import Ollama

llm = Ollama(model="qwen2.5:7b", request_timeout=60.0)

messages = [
    ChatMessage(
        role="user",
        blocks=[
            ImageBlock(path="./image.png"),
            TextBlock(text="Describe the image in a few sentences in Chinese."),
        ],
    )
]

resp = llm.chat(messages)
print(resp.message.content)