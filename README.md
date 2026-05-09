# Penn-product-a-thon-Merble MVP
This is a Minimum Viable Product for the startup partner Merble, developed for the Product-a-thon at the University of Pennsylvania (Spring '26).

The MVP is a data pipeline that processes member transaction data and generates a list of signals and scores that can be used to determine if a member is at risk of defaulting on a loan. The MVP also includes a lightweight agent that can be used to automatically export the data to Airtable. The main goal is to create an MVP for decision support for loan officers, rather than decision making, in consideration of explainability, accountability, and compliance.
本最小可行性产品（MVP）旨在构建一条处理成员交易数据的数据管线，并生成相关的特征信号与风险评分，以判定成员的贷款违约概率。此外，该MVP还包含一个轻量级代理工具，可将数据自动导出至 Airtable。基于对可解释性、归责性及合规性的综合考量，本方案的核心目标是为信贷审批员提供决策支持，而非直接取代人工进行决策制定。

1. Overview/Folder Structure

```
merble-project/
├── data/
│   ├── raw_members.csv           # 原始 synthetic 数据
│   └── processed_members.csv     # 处理后（含 signals/score）
├── src/
│   ├── main.py                   # 主入口（运行 pipeline）
│   ├── signals.py                # 信号识别逻辑
│   ├── scoring.py                # 评分算法逻辑
│   ├── classification.py         # 贷款分类逻辑
│   ├── llm.py                    # LLM 解释 & 文案生成
│   └── utils.py                  # 通用工具函数
├── tests/
│   └── test_scoring.py           # 测试脚本
├── notebooks/
│   └── exploration.ipynb         # 存放数据探索逻辑
├── .env                          # 存放私密 API Key (不进入 Git)
├── .gitignore                    # 告诉 Git 忽略哪些文件
├── output/
│   └── airtable_upload.csv       # 最终导入 Airtable 的文件
├── config.py                     # 参数配置（如阈值、API Key 等）
├── requirements.txt              # 环境依赖清单
└── README.md                     # 项目说明文档
```

2. Core System:

**member transaction data** → **signal detection** → **scoring/ranking** → **LLM summary & explanation** → **Airtable export**

3. Key Features:

| 模块     | 技术                |
| ------ | ----------------- |
| 核心决策   | rules/scoring     |
| 外部信息增强 | RAG               |
| 解释与话术  | LLM               |
| 工作流自动化 | lightweight agent |
