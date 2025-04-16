import chainlit as cl

def on_chat_start():
    cl.Message("欢迎使用 Chainlit!")

def main():
    cl.title("Hello, Chainlit!")
    cl.button("Click Me")
    cl.on_chat_start(on_chat_start)  # 确保这里注册了回调

if __name__ == '__main__':
    main()