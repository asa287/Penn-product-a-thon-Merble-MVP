# Penn-product-a-thon-Merble MVP
This is a Minimum Viable Product for the startup partner Merble, developed for the Product-a-thon at the University of Pennsylvania (Spring '26).

1. Folder Structure

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