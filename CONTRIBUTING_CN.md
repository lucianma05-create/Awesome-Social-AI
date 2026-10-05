# 贡献指南（Awesome Social AI）

**[简体中文](CONTRIBUTING_CN.md)** | **[English](CONTRIBUTING.md)**

欢迎所有对社会智能对话智能体感兴趣的朋友为仓库做出贡献。你可以：

- 向目录（`metadata/papers.json`）添加新论文，并在 `paper/` 中撰写中文摘要
- 改进关键词、词表定义与流水线脚本
- 修正错别字、链接或元数据问题

整体上我们采用 "fork-and-pull" 的 Git 工作流：

1. Fork 本仓库到自己的 GitHub 账户
2. 克隆到本地并为改动创建分支
3. 完成修改并提交
4. 将分支推送到自己的 fork
5. 向本仓库 `main` 分支发起 Pull Request

## 命名规范

- `paper/` 下的文件名请严格按 `[方向]-[会议/期刊名]-[年份]-[论文完整名].md` 命名，例如 `Memory-NeurIPS-2023-Retrieval-Augmented-Generation.md`
- 文件名前缀是论文的**主入口**，从当前 11 个前缀中选择最接近的一项，它不替代关键词；确需新增前缀时请先在组内讨论。当前前缀：`PD`、`ED`、`Recommend`、`Coop`、`ToM`、`Emotion`、`Norms`、`Memory`、`RLHF`、`US`、`Data`
- `image/` 下的文件按 `[年]-[月]-[日]-[编号]-[姓名缩写].png` 命名，例如 `2024010101mmh.png`

## 添加论文

1. 参照 [Example.md](Example.md) 模板撰写中文摘要
2. 在 `metadata/papers.json` 中新增结构化记录：`type`、`goal`、`horizon` 单选；能力、情境、方法可多选。所有标签值须来自 [关键词词表](metadata/KEYWORDS.md)，并为每个多选标签填写论文依据
3. 提交前运行校验并重建目录：

```bash
python scripts/validate_metadata.py --paper-dir paper
python scripts/render_readme_catalog.py
```

也可使用 [Auto-Summary](https://github.com/lucianma05-create/Auto-Summary) 自动生成摘要初稿，再进行人工校对。
