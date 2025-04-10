from ollama import Client

def test_ollama_connection():
    client = Client()
    try:
        # 尝试获取服务器信息
        response = client.list()
        models = response.models  # 假设 response.models 是一个包含 Model 对象的列表

        print("成功连接到Ollama服务器")
        print(f"可用模型：{[model.model for model in models]}")
        
        # 获取用户输入的模型名称
        model_name = input("请输入要使用的模型名称: ")
        
        # 检查输入的模型名称是否在可用模型列表中
        if model_name not in [model.model for model in models]:
            print(f"模型 '{model_name}' 未找到，请重新输入")
            return
        
        # 简单的测试请求
        while True:
            user_input = input("你: ")
            response = client.chat(model=model_name, messages=[
                {
                    'role': 'user',
                    'content': user_input
                }
            ])
            print(f"助手: {response['message']['content']}")
        
    except Exception as e:
        print(f"连接测试失败：{str(e)}")

test_ollama_connection()
