import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    await cl.Message("欢迎使用 Chainlit!").send()

@cl.on_message
async def on_message(message: cl.Message):
    await cl.Message("收到消息: " + message.content).send()

if __name__ == '__main__':
    cl.run()