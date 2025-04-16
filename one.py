from openai import OpenAI
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='llama3'
)

response = client.chat.completions.create(
    messages=[
        {'role': 'user', 'content': "鲁迅和周树人是什么关系？"},
    ],
    model='mistral',
    stream=True
)
print("鲁迅和周树人是什么关系？")
for chunk in response:
    #打印更多信息
    print(chunk.choices[0].delta.content, end="", flush=True)
    