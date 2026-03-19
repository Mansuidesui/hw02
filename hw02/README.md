# hw02 项目说明

## 任务一：论文导读
- **论文**：《Attention Is All You Need》, NeurIPS 2017
- **生成工具**：DeepSeek Chat 模型
- **配图方式**：手动从论文及公开资料获取模型架构图、实验结果图，插入到 Markdown 文档并添加图注

## 任务二：DeepSeek Chatbot
- **API 平台**：DeepSeek 官方 OpenAI 兼容接口
- **运行环境**：Python 3.8+
- **依赖安装**：`pip install -r requirements.txt`
- **配置**：设置环境变量 `DEEPSEEK_API_KEY` 为你的 DeepSeek API Key
- **运行命令**：`python chatbot_deepseek.py`
- **示例**：输入问题后，模型会返回对应的回答

## 项目结构
hw02/
├── chatbot_deepseek.py
├── requirements.txt
├── README.md
├── 导读_Attention_Is_All_You_Need.md
└── assets/
    ├── transformer_arch.png
    └── transformer_result.png