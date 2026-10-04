# Keywords for Awesome Social AI

本文档是本仓库的受控关键词词表。关键词采用**分面（facet）**而非单一分类：不同分面可以组合，同一分面内的单选字段必须唯一。不要以自由同义词替代既有术语。

## Required fields

`papers.json` 的键是稳定、小写的论文 ID（例如 `tomap-2025`），而不是摘要文件名。这样即使论文尚未有中文摘要，也能进入完整目录。每条记录必须包含 `title`、`year`、`venue`、`paper_url`、`code_url` 和可为 `null` 的 `summary_path`，再标注以下分类字段：

| Field | Cardinality | Values | Rule |
| --- | --- | --- | --- |
| `type` | exactly one | `System`, `Method`, `Dataset`, `Benchmark`, `Evaluation`, `Survey` | 按论文的主要贡献，而非所有组成部分。 |
| `goal` | exactly one | `Influence`, `Support`, `Recommendation`, `Coordination`, `General Interaction` | 选择主要社会交互目标。 |
| `horizon` | exactly one | `Single-turn`, `Multi-turn`, `Longitudinal`, `Unspecified` | `Longitudinal` 指跨会话或长期状态演化；不能仅因多轮而使用。标题回退而没有交互尺度证据时使用 `Unspecified`，不臆测为单轮。 |

`primary_section` 也是必填单选字段，用于 README 的主入口。可选值为：`influence-negotiation`、`support-care`、`conversational-recommendation`、`cooperation-coordination`、`mental-state-modeling`、`affect-social-perception`、`social-context-norms-morality`、`social-memory-adaptation`、`learning-planning-alignment`、`user-simulation-environments`、`datasets-benchmarks-evaluation`。它只表达最适合浏览的入口，不替代下列交叉标签。

## Optional multi-label fields

### `capabilities`

| Tag | Include when the paper centrally studies… | Exclude when… |
| --- | --- | --- |
| `Social Perception` | 从语言、语音、视觉或多模态线索识别社会信号 | 仅生成带情绪语气的文本而不推断线索。 |
| `Affect` | 情绪、共情、情感状态的理解、表达或调节 | “支持”只是应用场景但没有情感建模。 |
| `Mental-State Modeling` | 信念、意图、目标、偏好或高阶心理状态的建模与推断 | 仅进行一般文本分类或策略搜索。 |
| `Social Context` | 模型**显式表示、推断或利用**角色、关系、群体结构、共同基础、文化或规范等社会情境，并据此改变推理或决策 | 社会情境仅是研究背景、数据集设计或应用条件（如基准中的角色设定、在特定文化中收集的语料），模型未对社会情境本身建模或推理；此类情形只标入 `contexts`，不标 `Social Context`。 |
| `Interaction Management` | 轮次管理、共识、关系维护、协调、融洽度或对话行为选择 | 仅完成单次问答。 |
| `Social Memory & Adaptation` | 利用跨互动的社会历史、偏好或反馈进行持续个性化/适应 | 通用上下文压缩或与社会互动无关的 RAG。 |

`Social Context` 与 `contexts` 分面的区别：前者描述模型**建模或推理社会情境的能力**，后者描述研究问题**所处的社会情境**。同一篇论文可以只有 `contexts`（例如在特定文化中收集语料但未建模文化对推理的影响）而没有 `Social Context`；两者同时出现也是合法的。

### `contexts`

`Personalization`, `Relationship & Role`, `Norms & Morality`, `Culture`, `Multi-party`, `Embodied`。

这些标签描述研究问题所在的社会情境，而非模型能力或技术实现。`Embodied` 仅用于身体、空间行动或非语言交互是核心研究变量的工作。`Relationship & Role`、`Norms & Morality`、`Culture` 不要求模型对相应情境建模；仅当论文明确建模了情境如何改变推理/决策时，才同时标 `Social Context`。

### `approaches`

`Supervised Learning`, `Retrieval`, `Planning`, `RL`, `Preference Optimization`, `Reward Modeling`, `Self-play`, `User Simulation`。

仅标注论文的关键方法。`Alignment` 是研究目标而非方法；应使用其具体实现（例如 `Preference Optimization` 或 `Reward Modeling`）。`User Simulation` 仅在模拟用户参与训练、规划或评测闭环时使用。

## Evidence and review policy

1. 标签判断以论文的摘要、问题定义、方法和实验为依据，**不以标题关键词自动决定**。
2. 为每一个 `capabilities`、`contexts`、`approaches` 标签在 `evidence` 中记录一条简短理由和论文页码/章节；没有证据不得标注。
3. 在 `field_evidence` 中记录 `primary_section`、`type`、`goal`、`horizon` 的判断依据；这避免仅从题目猜测论文的主要贡献或交互尺度。
4. 首次标注者完成后，由另一位维护者复核高风险或边界标签：`Influence`、`Support`、`Mental-State Modeling`、`Norms & Morality`、`Longitudinal`、`Social Context`（缩窄定义下仍易与 `contexts` 混淆，需人工确认证据确实支持“模型对社会情境建模并据此改变推理/决策”）。
5. `auto_extracted` 记录可进入 README，但会标注为“自动摘要提取”；`reviewed` 表示人工复核完成。`draft` 与 `needs_review` 不发布。两人不一致时记录为 `needs_review`，由负责维护者裁决并留下修订记录。
6. 每季度抽样复审，并在新增术语前先修改本词表、说明与生成脚本。

迁移期间，只有书目信息而尚未逐篇判断的记录使用 `unclassified`；它们不含经过审核的分类字段、不出现在关键词索引。为保持旧 README 的浏览位置，这类记录可暂存从旧表导入的 `primary_section`，但该值不是已审核标签。自动抓取原文摘要并由规则抽取的记录使用 `auto_extracted`，其每个标签均保留触发的摘要片段和抓取来源。每条已标注记录必须填写 `annotated_by`。若状态为 `reviewed`，还必须填写与标注者不同的 `reviewed_by`；校验器会拒绝缺失这些审计字段的正式记录。

## Display format

README 中以紧凑标签形式呈现，例如：

```text
`Method` · `Influence` · `Mental-State Modeling` · `RL` · `Multi-turn`
```

标签所属分面由本词表的映射统一定义；论文列表不重复显示分面前缀，以保持条目简洁。
