# LLM_Paper_Assistant
### 在大语言模型的研究过程中，阅读并分析英文论文是不可或缺的任务。为了提高研究效率，本项目旨在开发一个论文阅读与总结助手，帮助研究员快速获取论文核心内容，生成摘要，并辅助复现相关代码。
### 项目框架：
### │── backend/                     # 后端服务
### │   │── main.py                   # FastAPI 入口文件
### │   │── models.py                 # 数据模型
### │   │── services/
### │   │   │── paper_parser.py        # 论文解析模块
### │   │   │── summarizer.py          # 论文摘要生成模块
### │   │   │── qa_system.py           # 交互式问答模块
### │   │   │── code_extractor.py      # 代码提取模块
### │   │── routers/
### │   │   │── paper.py               # 论文相关 API
### │   │   │── summary.py             # 摘要生成 API
### │   │   │── qa.py                  # 问答 API
### │   │── config.py                  # 配置文件
### │── README.md                     # 说明文档
