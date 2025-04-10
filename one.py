from openai import OpenAI
client = OpenAI(
    api_key = "sk-xxxxxx",
    base_url = "https://api.openai.com",
)

response = client.chat.completions.create(
    messages=[
        {'role': 'user', 'content': "鲁迅为什么打周树人？"},
    ],
    model='gpt-3.5-16K',
    stream=True
)

for chunk in response:
    #打印更多信息
    print(chunk.choices[0].delta.content, end="", flush=True)

llm = OpenAI("gpt-4o")