from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

llm = Ollama(model="qwen2.5:7b", request_timeout=60.0)

messages = [
    ChatMessage(role="system", content="You are a helpful assistant."),
    ChatMessage(role="user", content="Use chinese to tell me a joke."),
]
chat_response = llm.chat(messages)
print(chat_response)  # 添加打印语句来查看响应