# [方向（例如记忆、说服等）]-[会议/期刊名]-[年份]-[论文名]

> 元数据是 README 关键词与交叉索引的唯一来源。请在 `metadata/papers.json` 中以稳定的小写论文 ID 为键，新增如下记录；`summary_path` 填当前文件的相对路径。所有标签值均须来自 [metadata/KEYWORDS.md](metadata/KEYWORDS.md) 的受控词表。`evidence` 必须给出每个多选标签的论文依据。提交前运行 `python scripts/validate_metadata.py --paper-dir paper`。

```json
"paper-short-name-year": {
  "title": "[论文完整标题]",
  "year": 2025,
  "venue": "ACL",
  "paper_url": "https://...",
  "code_url": "https://...",
  "summary_path": "paper/[当前文件名].md",
  "primary_section": "influence-negotiation",
  "type": "Method",
  "goal": "Influence",
  "capabilities": ["Mental-State Modeling"],
  "contexts": [],
  "approaches": ["RL"],
  "horizon": "Multi-turn",
  "field_evidence": [
    {"field": "primary_section", "rationale": "主要问题是说服对手。", "source": "摘要"},
    {"field": "type", "rationale": "主要贡献是提出训练方法。", "source": "§3"},
    {"field": "goal", "rationale": "系统优化说服效果。", "source": "摘要"},
    {"field": "horizon", "rationale": "实验和方法都以多轮对话为单位。", "source": "§4"}
  ],
  "evidence": [
    {
      "tag": "Mental-State Modeling",
      "rationale": "论文在问题定义或方法中显式建模对手的信念、意图或偏好。",
      "source": "§2"
    }
  ],
  "annotated_by": "your-github-id",
  "review_status": "draft"
}
```

*论文下载地址（可选）：[https://arxiv.org/](https://arxiv.org/)*

*代码是否开源：是/否 [https://github.com/](https://github.com/)*

*分享人：XXX*

## 一句话总结挑战
> 用一句话总结文章所解决的挑战

## 一句话总结创新贡献
> 用一句话总结文章为了解决挑战做出的贡献

## 举一个例子说明这篇文章的创新点
> 通俗易懂的一个例子简述和其它工作的区别和创新点

## 框架图
> 请在此处放置框架图（将图片文件放入 image/ 目录，然后在下方用相对路径引用，例如：`![framework](../image/xxx.png)`）

> **框架工作流描述**：请用文字简要描述整个框架的工作流程，例如各模块之间的数据流向、各组件的作用、关键处理步骤等。

## 本文挑战及已有工作不足
> 总结本文的挑战和现有工作不足

## 印象最深刻的点
> 简述印象最深刻的点

## 是否有开创性
> 是否开创性工作

## 其他需要补充的点（可选）
> 

## 与其他论文的关联（可选）
> 

## 未来工作
> 还有哪些不足的地方

example version: 0.1.0
