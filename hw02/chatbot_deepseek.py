import os
from openai import OpenAI

# 初始化 DeepSeek 客户端（OpenAI 兼容接口）
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 从环境变量读取 API Key
    base_url="https://api.deepseek.com/v1"  # DeepSeek 官方接口地址
)

def chat_with_deepseek(user_input: str) -> str:
    """
    调用 DeepSeek 模型获取回答
    :param user_input: 用户输入的问题文本
    :return: 模型返回的回答内容
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # 使用 DeepSeek 聊天模型
            messages=[
                {"role": "system", "content": "你是一个专业的AI助手，请清晰、准确地回答用户问题。"},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"调用失败：{str(e)}"

if __name__ == "__main__":
    print("✅ DeepSeek Chatbot 已启动，输入 'quit' 或 'exit' 退出")
    while True:
        user_input = input("\n🗣️ 你: ")
        if user_input.lower() in ["quit", "exit"]:
            print("👋 再见！")
            break
        reply = chat_with_deepseek(user_input)
        print(f"🤖 DeepSeek: {reply}")