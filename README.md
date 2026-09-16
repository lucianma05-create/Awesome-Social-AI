<div align="center">

# 🌐 Awesome Social AI

[![Awesome](https://img.shields.io/badge/Awesome-0066CC?style=for-the-badge&logo=awesome-lists&logoColor=white)](https://github.com/sindresorhus/awesome)
[![License](https://img.shields.io/badge/License-Apache%202.0-red?style=for-the-badge&logo=apache&logoColor=white)](http://www.apache.org/licenses/LICENSE-2.0)
[![Papers](https://img.shields.io/github/directory-file-count/lucianma05-create/Awesome-Social-AI/paper?type=file&extension=md&label=Papers&color=2ea44f&style=for-the-badge)](paper)
[![Summaries](https://img.shields.io/badge/Summaries-121-007ec6?style=for-the-badge)](README.md)
[![Views](https://komarev.com/ghpvc/?username=lucianma05-create&repo=Awesome-Social-AI&label=Views&color=orange&style=for-the-badge)](https://github.com/lucianma05-create/Awesome-Social-AI)
</div>

**我们精心收集整理社交人工智能(Social AI)领域的研究论文,并持续更新论文的中文摘要,从而支持快速了解该领域的代表性工作。仓库将不断更新,追踪社交 AI 前沿。欢迎 Follow 和 Star!⭐**

<a id="social-ai"></a>
## 🎯 范畴与结构

**Social AI** 是研究与构建具备社会智能的 AI 系统的领域。社会智能指智能体在社交情境中的三组能力:社交理解(感知情绪、意图、信念、关系、规范与多方动态)、社交推理(心智建模、归因与策略规划)、社交行动(说服、谈判、共情支持、建立信任)。

本仓库按四层结构组织:

- **任务层 · 社交任务**
  - [Persuasion & Negotiation](#pd) — 说服、谈判等策略性对话的研究、方法与评测
  - [Empathy & Emotional Support](#ed) — 共情对话、情感支持与心理辅导
  - [Conversational Recommendation](#recommend) — 对话式推荐系统
  - [Cooperation & Collaboration](#coop) — 合作、协作与多方共识构建
- **能力层 · 社交认知**
  - [Theory of Mind](#tom) — 心智建模、意图与信念推理
  - [Emotion Understanding](#emotion) — 情绪识别、归因与情绪推理
  - [Social Norms & Morality](#norms) — 社会规范、道德判断与价值对齐
  - [Agent Memory](#memory) — 智能体长期记忆与经验演化
- **方法层 · 支撑技术**
  - [Reinforcement Learning & Alignment](#rlhf) — 强化学习训练与对齐方法
- **资源层 · 研究基础设施**
  - [User Simulation & Interactive Environments](#us) — 用户模拟、交互环境与仿真
  - [Benchmark & Evaluation](#data) — 基准测试、数据集与评测

不收录:计算社会科学 / "AI for social science" 类工作。方法层的通用强化学习与对齐技术,以"支撑社交智能体的基础方法"身份收录;与社交无关、亦不服务于社交智能体的技术不收录。

**参考论文:**
> 1. [Towards Social AI: A Survey on Understanding Social Interactions](https://arxiv.org/abs/2409.15316)
> 2. [Advancing Social Intelligence in AI Agents: Technical Challenges and Open Questions](https://aclanthology.org/2024.emnlp-main.1143/)

<a id="toc"></a>
## 📑 目录

- [🌐 Awesome Social AI](https://github.com/lucianma05-create/Awesome-Social-AI)
  - [🎯 范畴与结构](#social-ai)
  - [📑 目录](#toc)
  - [📚 论文列表](#papers)
    - [Persuasion & Negotiation](#pd)
    - [Empathy & Emotional Support](#ed)
    - [Conversational Recommendation](#recommend)
    - [Cooperation & Collaboration](#coop)
    - [Theory of Mind](#tom)
    - [Emotion Understanding](#emotion)
    - [Social Norms & Morality](#norms)
    - [Agent Memory](#memory)
    - [Reinforcement Learning & Alignment](#rlhf)
    - [User Simulation & Interactive Environments](#us)
    - [Benchmark & Evaluation](#data)
  - [📁 仓库结构](#repo-structure)
  - [✍️ 如何贡献](#contributing)
  - [🧠 关于我们](#about)

<a id="papers"></a>
## 📚 论文列表

<a id="pd"></a>
<details>
<summary>🗣️ <b>Persuasion & Negotiation</b> · 35 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2008 | PERSUASIVE | A Systematic Framework for Designing and Evaluating Persuasive Systems | [查看](https://doi.org/10.1007/978-3-540-68504-3_15) | [摘要](paper/PD-PERSUASIVE-2008-A%20Systematic%20Framework%20for%20Designing%20and%20Evaluating%20Persuasive%20Systems.md) | - |
| 2008 | - | Measure Of Belief Change as an Evaluation of Persuasion | [查看](https://www.researchgate.net/publication/228964262_Measure_Of_Belief_Change_as_an_Evaluation_of_Persuasion) | [摘要](paper/PD-%E6%9C%AA%E6%8F%90%E5%8F%8A-2008-Measure%20Of%20Belief%20Change%20as%20an%20Evaluation%20of%20Persuasion.md) | - |
| 2014 | COLING | Reinforcement Learning of Cooperative Persuasive Dialogue Policies using Framing | [查看](https://aclanthology.org/C14-1161/) | [摘要](paper/PD-COLING-2014-Reinforcement-Learning-of-Cooperative-Persuasive-Dialogue-Policies-using-Framing.md) | - |
| 2017 | HCI | Persuasive Argumentation and Emotions- An Empirical Evaluation with Users | [查看](https://doi.org/10.1007/978-3-319-58071-5_50) | [摘要](paper/PD-HCI-2017-Persuasive%20Argumentation%20and%20Emotions-%20An%20Empirical%20Evaluation%20with%20Users.md) | - |
| 2023 | ArgComp | Strategic argumentation dialogues for persuasion- Framework and experiments based on modelling the beliefs and concerns of the persuadee | [查看](https://doi.org/10.3233/AAC-210005) | [摘要](paper/PD-ArgComp-2023-Strategic%20argumentation%20dialogues%20for%20persuasion-%20Framework%20and%20experiments%20based%20on%20modelling%20the%20beliefs%20and%20concerns%20of%20the%20persuadee.md) | - |
| 2023 | arXiv | Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback | [查看](https://arxiv.org/abs/2305.10142) | [摘要](paper/PD-arXiv-2023-Improving-Language-Model-Negotiation-with-Self-Play-and-In-Context-Learning-from-AI-Feedback.md) | - |
| 2024 | ICLR | Plug-and-Play Policy Planner for LLM-Powered Dialogue Agents | [查看](https://arxiv.org/pdf/2311.00262.pdf) | [摘要](paper/PD-ICLR-2024-Plug-and-Play%20Policy%20Planner%20for%20LLM-Powered%20Dialogue%20Agents.md) | [代码](https://github.com/dengyang17/PPDPP) |
| 2025 | Science | Durably reducing conspiracy beliefs through dialogues with AI | [查看](https://www.science.org/doi/10.1126/science.adq1814) | [摘要](paper/PD-Science-2025-Durably%20reducing%20conspiracy%20beliefs%20through%20dialogues%20with%20AI.md) | - |
| 2025 | Science | The Levers of Political Persuasion | [查看](https://www.science.org/doi/10.1126/science.aea3884) | [摘要](paper/PD-Science-2025-The%20Levers%20of%20Political%20Persuasion.md) | [代码](https://github.com/kobihackenburg/scaling-conversational-AI) |
| 2025 | ACL | Battling against Tough Resister- Strategy Planning with Adversarial Game for Non-collaborative Dialogues | [查看](https://aclanthology.org/2025.acl-long.184/) | [摘要](paper/PD-ACL-2025-Battling%20against%20Tough%20Resister-%20Strategy%20Planning%20with%20Adversarial%20Game%20for%20Non-collaborative%20Dialogues.md) | - |
| 2025 | TACL | Human Choice Prediction in Language-based Persuasion Games- Simulation-based Off-Policy Evaluation | [查看](https://doi.org/10.1162/TACL.a.16) | [摘要](paper/PD-TACL-2025-Human%20Choice%20Prediction%20in%20Language-based%20Persuasion%20Games-%20Simulation-based%20Off-Policy%20Evaluation.md) | [代码](https://github.com/eilamshapira/HumanChoicePrediction) |
| 2025 | EMNLP | Enhancing LLM-Based Persuasion Simulations with Cultural and Speaker-Specific Information | [查看](https://aclanthology.org/2025.findings-emnlp.808) | [摘要](paper/PD-EMNLP-2025-Enhancing%20LLM-Based%20Persuasion%20Simulations%20with%20Cultural%20and%20Speaker-Specific%20Information.md) | [代码](https://github.com/HF-heaven/Cross-Cultural-Persuasion-Simulations) |
| 2025 | EMNLP | Enhancing Persuasive Dialogue Agents by Synthesizing Cross-Disciplinary Communication Strategies | [查看](https://aclanthology.org/2025.emnlp-industry.158/) | [摘要](paper/PD-EMNLP-2025-Enhancing%20Persuasive%20Dialogue%20Agents%20by%20Synthesizing%20Cross-Disciplinary%20Communication%20Strategies.md) | - |
| 2025 | NAACL | Teaching models to balance resisting and accepting persuasion | [查看](https://aclanthology.org/2025.naacl-long.412/) | [摘要](paper/PD-NAACL-2025-Teaching%20models%20to%20balance%20resisting%20and%20accepting%20persuasion.md) | [代码](https://github.com/esteng/persuasion_balanced_training) |
| 2025 | arXiv | LLM Can be a Dangerous Persuader- Empirical Study of Persuasion Safety in Large Language Models | [查看](https://arxiv.org/abs/2504.10430) | [摘要](paper/PD-arXiv-2025-LLM%20Can%20be%20a%20Dangerous%20Persuader-%20Empirical%20Study%20of%20Persuasion%20Safety%20in%20Large%20Language%20Models.md) | [代码](https://github.com/PLUM-Lab/PersuSafety) |
| 2025 | EMNLP | PRINCIPLES- Synthetic Strategy Memory for Proactive Dialogue Agents | [查看](https://arxiv.org/abs/2509.17459) | [摘要](paper/PD-EMNLP-2025-PRINCIPLES-%20Synthetic%20Strategy%20Memory%20for%20Proactive%20Dialogue%20Agents.md) | [代码](https://huggingface.co/spaces/kimnamssya/Principles) |
| 2025 | NeurIPS | Persuade Me if You Can- A Framework for Evaluating Persuasion Effectiveness and Susceptibility Among Large Language Models | [查看](https://arxiv.org/abs/2503.01829) | [摘要](paper/PD-NeurIPS-2025-Persuade%20Me%20if%20You%20Can-%20A%20Framework%20for%20Evaluating%20Persuasion%20Effectiveness%20and%20Susceptibility%20Among%20Large%20Language%20Models.md) | [代码](https://beyzabozdag.github.io/PMIYC/) |
| 2025 | AAAI | Simulation-free hierarchical latent policy planning for proactive dialogues | [查看](https://arxiv.org/abs/2412.14584) | [摘要](paper/PD-AAAI-2025-Simulation-free%20hierarchical%20latent%20policy%20planning%20for%20proactive%20dialogues.md) | - |
| 2025 | arXiv | ToMAP: Training Opponent-Aware LLM Persuaders with Theory of Mind | [查看](https://arxiv.org/abs/2505.22961) | [摘要](paper/PD-arXiv-2025-ToMAP%3A%20Training%20Opponent-Aware%20LLM%20Persuaders%20with%20Theory%20of%20Mind.md) | [代码](https://github.com/ulab-uiuc/ToMAP) |
| 2025 | ACL | EPO: Explicit Policy Optimization for Strategic Reasoning in LLMs via RL | [查看](https://aclanthology.org/2025.acl-long.747/) | [摘要](paper/PD-ACL-2025-EPO-Explicit-Policy-Optimization-for-Strategic-Reasoning-in-LLMs-via-RL.md) | - |
| 2025 | arXiv | Disagreements in Reasoning: How a Model's Thinking Process Dictates Persuasion in Multi-Agent Systems | [查看](https://arxiv.org/abs/2503.09999) | [摘要](paper/PD-arXiv-2025-Disagreements-in-Reasoning-How-a-Model%E2%80%99s-Thinking-Process-Dictates-Persuasion-in-Multi-Agent-Systems.md) | - |
| 2025 | arXiv | EvoEmo: Evolved Emotional Policies for Adversarial LLM Agents in Multi-Turn Price Negotiation | [查看](https://arxiv.org/abs/2502.07483) | [摘要](paper/PD-arXiv-2025-EvoEmo-Evolved-Emotional-Policies-for-Adversarial-LLM-Agents-in-Multi-Turn-Price-Negotiation.md) | - |
| 2025 | arXiv | From Simulation to Strategy: Automating Personalized Interaction Planning for Conversational Agents | [查看](https://arxiv.org/abs/2502.13289) | [摘要](paper/PD-arXiv-2025-From-Simulation-to-Strategy-Automating-Personalized-Interaction-Planning-for-Conversational-Agents.md) | - |
| 2025 | arXiv | Persuasion Should be Double-Blind: A Multi-Domain Dialogue Dataset With Faithfulness Based on Causal Theory of Mind | [查看](https://arxiv.org/abs/2501.10832) | [摘要](paper/PD-arXiv-2025-Persuasion-Should-be-Double-Blind-A-Multi-Domain-Dialogue-Dataset-With-Faithfulness-Based-on-Causal-Theory-of-Mind.md) | - |
| 2025 | arXiv | Verbalized Bayesian Persuasion | [查看](https://arxiv.org/abs/2503.15477) | [摘要](paper/PD-arXiv-2025-Verbalized-Bayesian-Persuasion.md) | - |
| 2025 | EMNLP | Persuasion-Dynamics in LLMs: Investigating Robustness and Adaptability in Knowledge and Safety with DuET-PD | [查看](https://aclanthology.org/2025.emnlp-main.81/) | [摘要](paper/PD-EMNLP-2025-Persuasion-Dynamics-in-LLMs-Investigating-Robustness-and-Adaptability-in-Knowledge-and-Safety-with-DuET-PD.md) | - |
| 2025 | EMNLP | Profiling LLM Copyright Infringement Risks under Adversarial Persuasive Prompting | [查看](https://aclanthology.org/2025.findings-emnlp.855/) | [摘要](paper/PD-EMNLP-2025-Profiling-LLM-Copyright-Infringement-Risks-under-Adversarial-Persuasive-Prompting.md) | [代码](https://github.com/Rongite/Persuasion) |
| 2025 | CSUR | Persuasive Conversational Agents for Environmental Sustainability: A Survey | [查看](https://doi.org/10.1145/3774751) | [摘要](paper/PD-CSUR-2025-Persuasive-Conversational-Agents-for-Environmental-Sustainability-A-Survey.md) | - |
| 2025 | ACL | ASTRO: Automatic Strategy Optimization For Non-Cooperative Dialogues | [查看](https://aclanthology.org/2025.findings-acl.22.pdf) | [摘要](paper/PD-ACL-2025-ASTRO:%20Automatic%20Strategy%20Optimization%20For%20Non-Cooperative%20Dialogues.md) | [代码](https://github.com/SCUNLP/ASTRO) |
| 2026 | arXiv | One Model, All Roles- Multi-Turn, Multi-Agent Self-Play Reinforcement Learning for Conversational Social Intelligence | [查看](https://arxiv.org/abs/2602.03109) | [摘要](paper/PD-arXiv-2026-One%20Model%2C%20All%20Roles-%20Multi-Turn%2C%20Multi-Agent%20Self-Play%20Reinforcement%20Learning%20for%20Conversational%20Social%20Intelligence.md) | - |
| 2026 | arXiv | Personality-Aware Reinforcement Learning for Persuasive Dialogue with LLM-Driven Simulation | [查看](https://arxiv.org/abs/2601.06877) | [摘要](paper/PD-arXiv-2026-Personality-Aware-Reinforcement-Learning-for-Persuasive-Dialogue-with-LLM-Driven-Simulation.md) | - |
| 2026 | CSUR | A Comprehensive Survey of Computational Persuasion | [查看](https://dl.acm.org/doi/10.1145/3800687) | [摘要](paper/PD-CSUR-2026-A%20Comprehensive%20Survey%20of%20Computational%20Persuasion.md) | [代码](https://github.com/beyzabozdag/PersuasionSurvey) |
| 2026 | ICLR | RebuttalAgent: Strategic Persuasion in Academic Rebuttal via Theory of Mind | [查看](https://arxiv.org/abs/2601.15715) | [摘要](paper/PD-ICLR-2026-RebuttalAgent%3A%20Strategic%20Persuasion%20in%20Academic%20Rebuttal%20via%20Theory%20of%20Mind.md) | [代码](https://github.com/Zhitao-He/RebuttalAgent) |
| 2026 | ICLR | Towards Strategic Persuasion with Language Models | [查看](https://arxiv.org/abs/2509.22989v2) | [摘要](paper/PD-ICLR-2026-Towards%20Strategic%20Persuasion%20with%20Language%20Models.md) | - |
| 2026 | arXiv | METRO: Towards Strategy Induction from Expert Dialogue Transcripts for Non-collaborative Dialogues | [查看](https://arxiv.org/pdf/2604.11427v3.pdf) | [摘要](paper/PD-arXiv-2026-METRO:%20Towards%20Strategy%20Induction%20from%20Expert%20Dialogue%20Transcripts%20for%20Non-collaborative%20Dialogues.md) | [代码](https://github.com/Humphrey-0125/METRO) |

</details>

<a id="ed"></a>
<details>
<summary>❤️‍🩹 <b>Empathy & Emotional Support</b> · 13 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2023 | arXiv | CharacterChat- Learning towards Conversational AI with Personalized Social Support | [查看](https://arxiv.org/abs/2308.10278) | [摘要](paper/ED-arXiv-2023-CharacterChat-%20Learning%20towards%20Conversational%20AI%20with%20Personalized%20Social%20Support.md) | [代码](https://github.com/morecry/CharacterChat) |
| 2023 | EMNLP | SoulChat- Improving LLMs’ Empathy, Listening, and Comfort Abilities through Fine-tuning with Multi-turn Empathy Conversations | [查看](https://aclanthology.org/2023.findings-emnlp.83.pdf) | [摘要](paper/ED-EMNLP-2023-SoulChat-%20Improving%20LLMs%E2%80%99%20Empathy%2C%20Listening%2C%20and%20Comfort%20Abilities%20through%20Fine-tuning%20with%20Multi-turn%20Empathy%20Conversations.md) | [代码](https://github.com/scutcyr/SoulChat) |
| 2024 | ACL | EmoBench- Evaluating the Emotional Intelligence of Large Language Models | [查看](https://github.com/Sahandfer/EmoBench) | [摘要](paper/ED-ACL-2024-EmoBench-%20Evaluating%20the%20Emotional%20Intelligence%20of%20Large%20Language%20Models.md) | [代码](https://github.com/Sahandfer/EmoBench) |
| 2025 | arXiv | Echo-N1- Affective RL Frontier | [查看](https://arxiv.org/abs/2512.00344v1) | [摘要](paper/ED-arXiv-2025-Echo-N1-%20Affective%20RL%20Frontier.md) | - |
| 2025 | ACL | PsyDT- Using LLMs to Construct the Digital Twin of Psychological Counselor with Personalized Counseling Style for Psychological Counseling | [查看](https://arxiv.org/pdf/2412.13660) | [摘要](paper/ED-ACL-2025-PsyDT-%20Using%20LLMs%20to%20Construct%20the%20Digital%20Twin%20of%20Psychological%20Counselor%20with%20Personalized%20Counseling%20Style%20for%20Psychological%20Counseling.md) | [代码](https://github.com/scutcyr/SoulChat2.0) |
| 2025 | ACL | PsyDial- A Large-scale Long-term Conversational Dataset for Mental Health Support | [查看](https://aclanthology.org/2025.acl-long.1049/) | [摘要](paper/ED-ACL-2025-PsyDial:%20A%20Large-scale%20Long-term%20Conversational%20Dataset%20for%20Mental%20Health%20Support.md) | [代码](https://github.com/qiuhuachuan/PsyDial) |
| 2025 | arXiv | Reinforcement Learning with Verifiable Emotion Rewards for Empathetic Agents | [查看](https://arxiv.org/abs/2507.03112v1) | [摘要](paper/ED-arXiv-2025-Reinforcement%20Learning%20with%20Verifiable%20Emotion%20Rewards%20for%20Empathetic%20Agents.md) | [代码](https://github.com/Tencent/DigitalHuman/tree/main/RLVER) |
| 2025 | arXiv | SAGE- Steering and Refining Dialog Generation with State-Action Augmentation | [查看](https://arxiv.org/abs/2503.03040) | [摘要](paper/ED-arXiv-2025-SAGE-%20Steering%20and%20Refining%20Dialog%20Generation%20with%20State-Action%20Augmentation.md) | [代码](https://github.com/apple/ml-sage-dialog-gen) |
| 2025 | ACL | Beyond Verbal Cues: Emotional Contagion Graph Network for Causal Emotion Entailment | [查看](https://aclanthology.org/2025.findings-acl.88/) | [摘要](paper/ED-ACL-2025-Beyond%20Verbal%20Cues%3A%20Emotional%20Contagion%20Graph%20Network%20for%20Causal%20Emotion%20Entailment.md) | [代码](https://github.com/Yu-Fangxu/ECGN) |
| 2025 | EMNLP | Chain of Strategy Optimization Makes Large Language Models Better Emotional Supporter | [查看](https://arxiv.org/abs/2503.05362) | [摘要](paper/ED-EMNLP-2025-Chain%20of%20Strategy%20Optimization%20Makes%20Large%20Language%20Models%20Better%20Emotional%20Supporter.md) | [代码](https://github.com/XingYuSSS/CSO) |
| 2026 | arXiv | Affective Flow Language Model for Emotional Support Conversation | [查看](https://arxiv.org/abs/2602.08826v1) | [摘要](paper/ED-arXiv-2026-Affective%20Flow%20Language%20Model%20for%20Emotional%20Support%20Conversation.md) | [代码](https://github.com/chzou25-lgtm/AffectiveFlow) |
| 2026 | arXiv | EMPA: Evaluating Persona-Aligned Empathy as a Process | [查看](https://arxiv.org/abs/2603.00552) | [摘要](paper/ED-arXiv-2026-EMPA:%20Evaluating%20Persona-Aligned%20Empathy%20as%20a%20Process.md) | [代码](https://github.com/KAYA-HAI/EMPA-Benchmark-EPMSandbox) |
| 2026 | ACL | You Never Know a Person, You Only Know Their Defenses- Detecting Levels of Psychological Defense Mechanisms in Supportive Conversations | [查看](https://aclanthology.org/2026.findings-acl.708/) | [摘要](paper/ED-ACL-2026-You%20Never%20Know%20a%20Person%2C%20You%20Only%20Know%20Their%20Defenses-%20Detecting%20Levels%20of%20Psychological%20Defense%20Mechanisms%20in%20Supportive%20Conversations.md) | - |

</details>

<a id="recommend"></a>
<details>
<summary>🛍️ <b>Conversational Recommendation</b> · 18 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2020 | ACL | Towards Conversational Recommendation over Multi-Type Dialogs | [查看](https://github.com/PaddlePaddle/models/tree/develop/PaddleNLP/Research/ACL2020-DuRecDial) | [摘要](paper/Recommend-ACL-2020-Towards%20Conversational%20Recommendation%20over%20Multi-Type%20Dialogs.md) | [代码](https://github.com/PaddlePaddle/models/tree/develop/PaddleNLP/Research/ACL2020-DuRecDial) |
| 2021 | ACL | RevCore- Review-augmented Conversational Recommendation | [查看](https://aclanthology.org/2021.findings-acl.104/) | [摘要](paper/Recommend-ACL-2021-RevCore-%20Review-augmented%20Conversational%20Recommendation.md) | [代码](https://github.com/JD-AI-Research-NLP/RevCore) |
| 2023 | KDD | Improving conversational recommendation systems via counterfactual data simulation | [查看](https://dl.acm.org/doi/10.1145/3580305.3599387) | [摘要](paper/Recommend-KDD-2023-Improving%20conversational%20recommendation%20systems%20via%20counterfactual%20data%20simulation.md) | [代码](https://github.com/RUCAIBox/CFCRS) |
| 2023 | EMNLP | Rethinking the Evaluation for Conversational Recommendation in the Era of Large Language Models | [查看](https://aclanthology.org/2023.emnlp-main.621/) | [摘要](paper/Recommend-EMNLP-2023-Rethinking%20the%20Evaluation%20for%20Conversational%20Recommendation%20in%20the%20Era%20of%20Large%20Language%20Models.md) | [代码](https://github.com/RUCAIBox/iEvaLM-CRS) |
| 2024 | EMNLP | Beyond Persuasion: Towards Conversational Recommender System with Credible Explanations | [查看](https://aclanthology.org/2024.findings-emnlp.247) | [摘要](paper/Recommend-EMNLP-2024-Beyond%20Persuasion%3A%20Towards%20Conversational%20Recommender%20System%20with%20Credible%20Explanations.md) | [代码](https://github.com/mumen798/PC-CRS) |
| 2024 | WWW | How Reliable is Your Simulator- Analysis on the Limitations of Current LLM-based User Simulators for Conversational Recommendation | [查看](https://doi.org/10.1145/3589335.3651955) | [摘要](paper/Recommend-WWW-2024-How%20Reliable%20is%20Your%20Simulator-%20Analysis%20on%20the%20Limitations%20of%20Current%20LLM-based%20User%20Simulators%20for%20Conversational%20Recommendation.md) | [代码](https://github.com/RUCAIBox/iEvaLM-CRS/) |
| 2024 | ACL | LLM-REDIAL: A Large-Scale Dataset for Conversational Recommender Systems Created from User Behaviors with LLMs | [查看](https://aclanthology.org/2024.findings-acl.529/) | [摘要](paper/Recommend-ACL-2024-LLM-REDIAL%3A%20A%20Large-Scale%20Dataset%20for%20Conversational%20Recommender%20Systems%20Created%20from%20User%20Behaviors%20with%20LLMs.md) | [代码](https://github.com/LitGreenhand/LLM-Redial) |
| 2024 | arXiv | Reindex-Then-Adapt- Improving Large Language Models for Conversational Recommendation | [查看](https://arxiv.org/abs/2405.12119) | [摘要](paper/Recommend-arXiv-2024-Reindex-Then-Adapt-%20Improving%20Large%20Language%20Models%20for%20Conversational%20Recommendation.md) | - |
| 2025 | TKDE | A Causal-Based Attribute Selection Strategy for Conversational Recommender Systems | [查看](https://ieeexplore.ieee.org/abstract/document/10891447) | [摘要](paper/Recommend-TKDE-2025-A%20Causal-Based%20Attribute%20Selection%20Strategy%20for%20Conversational%20Recommender%20Systems.md) | - |
| 2025 | WWW | Bridging Conversational and Collaborative Signals for Conversational Recommendation | [查看](https://doi.org/10.1145/3701716.3715486) | [摘要](paper/Recommend-WWW-2025-Bridging%20Conversational%20and%20Collaborative%20Signals%20for%20Conversational%20Recommendation.md) | - |
| 2025 | WWW | Collaborative Retrieval for Large Language Model-based Conversational Recommender Systems | [查看](https://dl.acm.org/doi/10.1145/3589334.3645347) | [摘要](paper/Recommend-WWW-2025-Collaborative%20Retrieval%20for%20Large%20Language%20Model-based%20Conversational%20Recommender%20Systems.md) | [代码](https://github.com/yaochenzhu/CRAG) |
| 2025 | WWW | Towards Efficient Conversational Recommendations- Expected Value of Information Meets Bandit Learning | [查看](https://doi.org/10.1145/3696410.3714773) | [摘要](paper/Recommend-WWW-2025-Towards%20Efficient%20Conversational%20Recommendations-%20Expected%20Value%20of%20Information%20Meets%20Bandit%20Learning.md) | - |
| 2025 | arXiv | A Framework for Generating Conversational Recommendation Datasets from Behavioral Interactions | [查看](https://arxiv.org/abs/2506.17285) | [摘要](paper/Recommend-arXiv-2025-A%20Framework%20for%20Generating%20Conversational%20Recommendation%20Datasets%20from%20Behavioral%20Interactions.md) | - |
| 2025 | EMNLP | LLM-based Conversational Recommendation Agents with Collaborative Verbalized Experience | [查看](https://aclanthology.org/2025.findings-emnlp.119/) | [摘要](paper/Recommend-EMNLP-2025-LLM-based%20Conversational%20Recommendation%20Agents%20with%20Collaborative%20Verbalized%20Experience.md) | [代码](https://github.com/yaochenzhu/CRAVE) |
| 2025 | EMNLP | Towards Personalized Conversational Sales Agents | [查看](https://arxiv.org/abs/2504.08754) | [摘要](paper/Recommend-EMNLP-2025-Towards%20Personalized%20Conversational%20Sales%20Agents.md) | - |
| 2026 | WWW | Not All Information Brings Benefits- Personalization-Driven Agent Debate for Conversational Recommendation | [查看](https://doi.org/10.1145/3774904.3792152) | [摘要](paper/Recommend-WWW-2026-Not%20All%20Information%20Brings%20Benefits-%20Personalization-Driven%20Agent%20Debate%20for%20Conversational%20Recommendation.md) | - |
| 2026 | WWW | Optimizing Multi-Turn Interactive Recommendation Agents via Generative Intrinsic Motivation | [查看](https://doi.org/10.1145/3774904.3792209) | [摘要](paper/Recommend-WWW-2026-Optimizing%20Multi-Turn%20Interactive%20Recommendation%20Agents%20via%20Generative%20Intrinsic%20Motivation.md) | [代码](https://github.com/XueyangFeng/GIMO) |
| 2026 | arXiv | User Simulator-Guided Multi-Turn Preference Optimization for Reasoning LLM-based Conversational Recommendation | [查看](https://arxiv.org/abs/2604.03671) | [摘要](paper/Recommend-arXiv-2026-User%20Simulator-Guided%20Multi-Turn%20Preference%20Optimization%20for%20Reasoning%20LLM-based%20Conversational%20Recommendation.md) | - |

</details>

<a id="coop"></a>
<details>
<summary>🤝 <b>Cooperation & Collaboration</b> · 5 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2022 | Science | Human-level play in the game of Diplomacy by combining language models with strategic reasoning | [查看](https://doi.org/10.1126/science.ade9097) | [摘要](paper/Coop-Science-2022-Human-level%20play%20in%20the%20game%20of%20Diplomacy%20by%20combining%20language%20models%20with%20strategic%20reasoning.md) | - |
| 2024 | ICLR | Building Cooperative Embodied Agents Modularly with Large Language Models | [查看](https://mlanthology.org/iclr/2024/zhang2024iclr-building/) | [摘要](paper/Coop-ICLR-2024-Building%20Cooperative%20Embodied%20Agents%20Modularly%20with%20Large%20Language%20Models.md) | - |
| 2024 | TACL | Decision-Oriented Dialogue for Human-AI Collaboration | [查看](https://aclanthology.org/2024.tacl-1.50/) | [摘要](paper/Coop-TACL-2024-Decision-Oriented%20Dialogue%20for%20Human-AI%20Collaboration.md) | - |
| 2024 | ICML | Should we be going MAD- A Look at Multi-Agent Debate Strategies for LLMs | [查看](https://arxiv.org/abs/2311.17371) | [摘要](paper/Coop-ICML-2024-Should%20we%20be%20going%20MAD-%20A%20Look%20at%20Multi-Agent%20Debate%20Strategies%20for%20LLMs.md) | [代码](https://github.com/instadeepai/DebateLLM) |
| 2024 | ACL | Your Co-Workers Matter- Evaluating Collaborative Capabilities of Language Models in Blocks World | [查看](https://aclanthology.org/2024.findings-acl.294/) | [摘要](paper/Coop-ACL-2024-Your%20Co-Workers%20Matter-%20Evaluating%20Collaborative%20Capabilities%20of%20Language%20Models%20in%20Blocks%20World.md) | - |

</details>

<a id="tom"></a>
<details>
<summary>💭 <b>Theory of Mind</b> · 18 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2011 | CogSci | Bayesian Theory of Mind- Modeling Joint Belief-Desire Attribution | [查看](https://www.semanticscholar.org/paper/Explore-Theory-of-Mind%3A-Program-guided-adversarial-Sclar-Yu/3c52a1e1c3dc0ef5e1e638e11bbc3a2f09900dc6) | [摘要](paper/ToM-CogSci-2011-Bayesian%20Theory%20of%20Mind-%20Modeling%20Joint%20Belief-Desire%20Attribution.md) | - |
| 2019 | COBS | Theory of Mind as Inverse Reinforcement Learning | [查看](https://doi.org/10.1016/j.cobeha.2019.04.010) | [摘要](paper/ToM-COBS-2019-Theory-of-Mind-as-Inverse-Reinforcement-Learning.md) | - |
| 2025 | ACL | Machine Theory of Mind Needs Machine Validation | [查看](https://aclanthology.org/2025.findings-acl.951.pdf) | [摘要](paper/ToM-ACL-2025-Machine%20Theory%20of%20Mind%20Needs%20Machine%20Validation.md) | - |
| 2025 | ACL | Theory of Mind in Large Language Models- Assessment and Enhancement | [查看](https://aclanthology.org/2025.acl-long.1522.pdf) | [摘要](paper/ToM-ACL-2025-Theory%20of%20Mind%20in%20Large%20Language%20Models-%20Assessment%20and%20Enhancement.md) | - |
| 2025 | arXiv | MINDGAMES: Do Large Language Models Have a Planning Theory of Mind? | [查看](https://arxiv.org/pdf/2507.16196v1.pdf) | [摘要](paper/ToM-arXiv-2025-MINDGAMES:%20Do%20Large%20Language%20Models%20Have%20a%20Planning%20Theory%20of%20Mind.md) | [代码](https://github.com/jlcmoore/mindgames) |
| 2025 | arXiv | Modeling the Mental World for Embodied AI- A Comprehensive Review | [查看](https://arxiv.org/pdf/2601.02378) | [摘要](paper/ToM-arXiv-2025-Modeling%20the%20Mental%20World%20for%20Embodied%20AI-%20A%20Comprehensive%20Review.md) | - |
| 2025 | arXiv | ToM-agent: Large Language Models as Theory of Mind Aware Generative Agents with Counterfactual Reflection | [查看](https://arxiv.org/abs/2501.15355) | [摘要](paper/ToM-arXiv-2025-ToM-agent-%20Large%20Language%20Models%20as%20Theory%20of%20Mind%20Aware%20Generative%20Agents%20with%20Counterfactual%20Reflection.md) | - |
| 2025 | arXiv | ToM-RL: Reinforcement Learning Unlocks Theory of Mind in Small LLMs | [查看](https://arxiv.org/abs/2504.01698) | [摘要](paper/ToM-arXiv-2025-ToM-RL-Reinforcement-Learning-Unlocks-Theory-of-Mind-in-Small-LLMs.md) | [代码](https://github.com/bigai-ai/ToM-R) |
| 2025 | ICML | Overcoming Multi-step Complexity in Multimodal Theory-of-Mind Reasoning- A Scalable Bayesian Planner | [查看](https://arxiv.org/abs/2506.01301) | [摘要](paper/ToM-ICML-2025-Overcoming%20Multi-step%20Complexity%20in%20Multimodal%20Theory-of-Mind%20Reasoning-%20A%20Scalable%20Bayesian%20Planner.md) | - |
| 2025 | NeurIPS | AutoToM- Scaling Model-based Mental Inference via Automated Agent Modeling | [查看](https://arxiv.org/abs/2502.15676) | [摘要](paper/ToM-NeurIPS-2025-AutoToM-%20Scaling%20Model-based%20Mental%20Inference%20via%20Automated%20Agent%20Modeling.md) | - |
| 2025 | NeurIPS | MetaMind- Modeling Human Social Thoughts with Metacognitive Multi-Agent Systems | [查看](https://arxiv.org/abs/2505.18943) | [摘要](paper/ToM-NeurIPS-2025-MetaMind-%20Modeling%20Human%20Social%20Thoughts%20with%20Metacognitive%20Multi-Agent%20Systems.md) | [代码](https://github.com/XMZhangAI/MetaMind) |
| 2026 | AAAI | Reality vs Counterfactual- Multi-World Contrastive Reinforcement Learning for Enhancing MLLM’s Theory of Mind in Egocentric Videos | [查看](https://ojs.aaai.org/index.php/AAAI/article/view/37162) | [摘要](paper/ToM-AAAI-2026-Reality%20vs%20Counterfactual-%20Multi-World%20Contrastive%20Reinforcement%20Learning%20for%20Enhancing%20MLLM%E2%80%99s%20Theory%20of%20Mind%20in%20Egocentric%20Videos.md) | - |
| 2026 | arXiv | Infusing Theory of Mind into Socially Intelligent LLM Agents | [查看](https://arxiv.org/abs/2509.22887) | [摘要](paper/ToM-arXiv-2026-Infusing%20Theory%20of%20Mind%20into%20Socially%20Intelligent%20LLM%20Agents.md) | [代码](https://github.com/eujhwang/toma) |
| 2026 | arXiv | MetaMind- General and Cognitive World Models in Multi-Agent Systems by Meta-Theory of Mind | [查看](https://arxiv.org/abs/2603.00808) | [摘要](paper/ToM-arXiv-2026-MetaMind-%20General%20and%20Cognitive%20World%20Models%20in%20Multi-Agent%20Systems%20by%20Meta-Theory%20of%20Mind.md) | - |
| 2026 | arXiv | MindClaw- Closed-Loop Embodied Mental-State Reasoning for Precision Intervention | [查看](https://arxiv.org/abs/2606.01063) | [摘要](paper/ToM-arXiv-2026-MindClaw-%20Closed-Loop%20Embodied%20Mental-State%20Reasoning%20for%20Precision%20Intervention.md) | - |
| 2026 | arXiv | UserHarness- Harnessing User Minds for Stronger Agent Theory-of-Mind | [查看](https://arxiv.org/abs/2605.27721) | [摘要](paper/ToM-arXiv-2026-UserHarness-%20Harnessing%20User%20Minds%20for%20Stronger%20Agent%20Theory-of-Mind.md) | - |
| 2026 | CVPR | Video-Only ToM- Enhancing Theory of Mind in Multimodal Large Language Models | [查看](https://arxiv.org/abs/2603.24484) | [摘要](paper/ToM-CVPR-2026-Video-Only%20ToM-%20Enhancing%20Theory%20of%20Mind%20in%20Multimodal%20Large%20Language%20Models.md) | [代码](https://founce.github.io/VisionToM/) |
| 2026 | EACL | Let's Put Ourselves in Sally's Shoes: Shoes of Others Prefilling Improves Theory of Mind in LLMs | [查看](https://aclanthology.org/2026.findings-eacl.6/) | [摘要](paper/ToM-EACL-2026-Lets-Put-Ourselves-in-Sallys-Shoes-Shoes-of-Others-Prefilling-Improves-Theory-of-Mind-in-LLMs.md) | - |

</details>

<a id="emotion"></a>
<details>
<summary>🎭 <b>Emotion Understanding</b> · 5 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2019 | AAAI | DialogueRNN- An Attentive RNN for Emotion Detection in Conversations | [查看](https://ojs.aaai.org/index.php/AAAI/article/view/4657) | [摘要](paper/Emotion-AAAI-2019-DialogueRNN-%20An%20Attentive%20RNN%20for%20Emotion%20Detection%20in%20Conversations.md) | - |
| 2019 | ACL | MELD- A Multimodal Multi-Party Dataset for Emotion Recognition in Conversations | [查看](https://aclanthology.org/P19-1050/) | [摘要](paper/Emotion-ACL-2019-MELD-%20A%20Multimodal%20Multi-Party%20Dataset%20for%20Emotion%20Recognition%20in%20Conversations.md) | - |
| 2021 | AAAI | COSMIC- COmmonSense knowledge for eMotion Identification in Conversations | [查看](https://arxiv.org/abs/2010.02795) | [摘要](paper/Emotion-AAAI-2021-COSMIC-%20COmmonSense%20knowledge%20for%20eMotion%20Identification%20in%20Conversations.md) | - |
| 2023 | arXiv | InstructERC- Reforming Emotion Recognition in Conversation with Multi-task Retrieval-Augmented Large Language Models | [查看](https://arxiv.org/abs/2309.11911) | [摘要](paper/Emotion-arXiv-2023-InstructERC-%20Reforming%20Emotion%20Recognition%20in%20Conversation%20with%20Multi-task%20Retrieval-Augmented%20Large%20Language%20Models.md) | - |
| 2025 | arXiv | Do LLMs Feel- Teaching Emotion Recognition with Prompts, Retrieval, and Curriculum Learning | [查看](https://arxiv.org/abs/2511.07061) | [摘要](paper/Emotion-arXiv-2025-Do%20LLMs%20Feel-%20Teaching%20Emotion%20Recognition%20with%20Prompts,%20Retrieval,%20and%20Curriculum%20Learning.md) | - |

</details>

<a id="norms"></a>
<details>
<summary>⚖️ <b>Social Norms & Morality</b> · 6 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2020 | EMNLP | Social Chemistry 101- Learning to Reason about Social and Moral Norms | [查看](https://aclanthology.org/2020.emnlp-main.48/) | [摘要](paper/Norms-EMNLP-2020-Social%20Chemistry%20101-%20Learning%20to%20Reason%20about%20Social%20and%20Moral%20Norms.md) | - |
| 2021 | arXiv | Delphi- Towards Machine Ethics and Norms | [查看](https://arxiv.org/abs/2110.07574) | [摘要](paper/Norms-arXiv-2021-Delphi-%20Towards%20Machine%20Ethics%20and%20Norms.md) | - |
| 2022 | ACL | The Moral Integrity Corpus- A Benchmark for Ethical Dialogue Systems | [查看](https://arxiv.org/abs/2204.03021) | [摘要](paper/Norms-ACL-2022-The%20Moral%20Integrity%20Corpus-%20A%20Benchmark%20for%20Ethical%20Dialogue%20Systems.md) | [代码](https://github.com/SALT-NLP/mic) |
| 2023 | ICML | Do the Rewards Justify the Means- Measuring Trade-Offs Between Rewards and Ethical Behavior in the MACHIAVELLI Benchmark | [查看](https://arxiv.org/abs/2304.03279) | [摘要](paper/Norms-ICML-2023-Do%20the%20Rewards%20Justify%20the%20Means-%20Measuring%20Trade-Offs%20Between%20Rewards%20and%20Ethical%20Behavior%20in%20the%20MACHIAVELLI%20Benchmark.md) | - |
| 2023 | ACL | NormBank- A Knowledge Bank of Situational Social Norms | [查看](https://arxiv.org/abs/2305.17008) | [摘要](paper/Norms-ACL-2023-NormBank-%20A%20Knowledge%20Bank%20of%20Situational%20Social%20Norms.md) | [代码](https://github.com/SALT-NLP/normbank) |
| 2024 | arXiv | CultureBank- An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies | [查看](https://arxiv.org/abs/2404.15238) | [摘要](paper/Norms-arXiv-2024-CultureBank-%20An%20Online%20Community-Driven%20Knowledge%20Base%20Towards%20Culturally%20Aware%20Language%20Technologies.md) | [代码](https://github.com/SALT-NLP/CultureBank) |

</details>

<a id="memory"></a>
<details>
<summary>💾 <b>Agent Memory</b> · 7 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2023 | UIST | Generative Agents- Interactive Simulacra of Human Behavior | [查看](https://doi.org/10.1145/3586183.3606763) | [摘要](paper/Memory-UIST-2023-Generative%20Agents-%20Interactive%20Simulacra%20of%20Human%20Behavior.md) | [代码](https://github.com/joonspk-research/generative_agents) |
| 2025 | arXiv | A-Mem: Agentic Memory for LLM Agents | [查看](https://arxiv.org/abs/2502.12110) | [摘要](https://github.com/lucianma05-create/Awesome-Social-AI/blob/main/paper/Memory-arXiv-2025-A-Mem%3A%20Agentic%20Memory%20for%20LLM%20Agents.md) | [代码](https://github.com/WujiangXu/AgenticMemory) |
| 2025 | arXiv | Evo-Memory- Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory | [查看](https://arxiv.org/abs/2511.20857) | [摘要](paper/Memory-arXiv-2025-Evo-Memory-%20Benchmarking%20LLM%20Agent%20Test-time%20Learning%20with%20Self-Evolving%20Memory.md) | [代码](https://github.com/WujiangXu/AgenticMemory) |
| 2025 | arXiv | Remember Me, Refine Me- A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution | [查看](https://arxiv.org/abs/2512.10696) | [摘要](https://github.com/lucianma05-create/Awesome-Social-AI/blob/main/paper/Memory-arXiv-2025-Remember%20Me%2C%20Refine%20Me-%20A%20Dynamic%20Procedural%20Memory%20Framework%20for%20Experience-Driven%20Agent%20Evolution.md) | [代码](https://github.com/agentscope-ai/ReMe) |
| 2026 | ICLR | MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | [查看](https://arxiv.org/abs/2507.02259) | [摘要](paper/Memory-ICLR-2026-MemAgent%3A%20Reshaping%20Long-Context%20LLM%20with%20Multi-Conv%20RL-based%20Memory%20Agent.md) | - |
| 2026 | ICLR | ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | [查看](https://proceedings.iclr.cc/paper_files/paper/2026/hash/980ea04d23d1f6908964eba2a74afe45-Abstract-Conference.html) | [摘要](paper/Memory-ICLR-2026-ReasoningBank%3A%20Scaling%20Agent%20Self-Evolving%20with%20Reasoning%20Memory.md) | [代码](https://github.com/google-research/reasoning-bank) |
| 2023 | arXiv | MemoryBank- Enhancing Large Language Models with Long-Term Memory | [查看](https://arxiv.org/abs/2305.10250) | [摘要](paper/Memory-arXiv-2023-MemoryBank-%20Enhancing%20Large%20Language%20Models%20with%20Long-Term%20Memory.md) | [代码](https://github.com/zhongwanjun/memorybank-siliconfriend) |

</details>

<a id="rlhf"></a>
<details>
<summary>🤖 <b>Reinforcement Learning & Alignment</b> · 12 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2023 | NeurIPS | Direct Preference Optimization- Your Language Model is Secretly a Reward Model | [查看](https://arxiv.org/abs/2305.18290) | [摘要](paper/RLHF-NeurIPS-2023-Direct%20Preference%20Optimization-%20Your%20Language%20Model%20is%20Secretly%20a%20Reward%20Model.md) | - |
| 2024 | ICML | RLAIF vs. RLHF- Scaling Reinforcement Learning from Human Feedback with AI Feed | [查看](https://arxiv.org/abs/2309.00267v3) | [摘要](paper/RLHF-ICML-2024-RLAIF%20vs.%20RLHF-%20Scaling%20Reinforcement%20Learning%20from%20Human%20Feedback%20with%20AI%20Feed.md) | - |
| 2025 | arXiv | DCPO- Dynamic Clipping Policy Optimization | [查看](https://arxiv.org/abs/2509.02333v2) | [摘要](paper/RLHF-arXiv-2025-DCPO-%20Dynamic%20Clipping%20Policy%20Optimization.md) | [代码](https://github.com/lime-RL/DCPO) |
| 2025 | arXiv | Group Sequence Policy Optimization | [查看](https://arxiv.org/abs/2507.18071v2) | [摘要](paper/RLHF-arXiv-2025-Group%20Sequence%20Policy%20Optimization.md) | - |
| 2025 | COLING | MCA-Model-Based Causal RL for Efficient Dialogue Policy | [查看](https://aclanthology.org/2025.coling-main.490/) | [摘要](paper/RLHF-COLING-2025-MCA-Model-Based-Causal-RL-for-Efficient-Dialogue-Policy.md) | - |
| 2025 | NeurIPS | World Models Should Prioritize the Unification of Physical and Social Dynamics | [查看](https://arxiv.org/pdf/2510.21219/) | [摘要](paper/RLHF-NeurIPS-2025-World-Models-Should-Prioritize-the-Unification-of-Physical-and-Social-Dynamics.md) | - |
| 2025 | EMNLP | Dream to Chat: Model-based Reinforcement Learning on Dialogues with User Belief Modeling | [查看](https://arxiv.org/abs/2508.16876) | [摘要](paper/RLHF-EMNLP-2025-Dream%20to%20Chat%3A%20Model-based%20Reinforcement%20Learning%20on%20Dialogues%20with%20User%20Belief%20Modeling.md) | - |
| 2025 | arXiv | Enhancing User Engagement in Socially-Driven Dialogue through Interactive LLM Alignments | [查看](https://arxiv.org/abs/2506.21497v1) | [摘要](paper/RLHF-arXiv-2025-Enhancing-User-Engagement-in-Socially-Driven-Dialogue-through-Interactive-LLM-Alignments.md) | - |
| 2025 | arXiv | MAPO: Mixed Advantage Policy Optimization for Long-Horizon Multi-Turn Dialogue | [查看](https://arxiv.org/pdf/2603.06194) | [摘要](paper/RLHF-arXiv-2025-MAPO:%20Mixed%20Advantage%20Policy%20Optimization%20for%20Long-Horizon%20Multi-Turn%20Dialogue.md) | - |
| 2026 | ICLR | Toward Evaluative Thinking: Meta-Policy Optimization with Evolving Reward Models | [查看](https://arxiv.org/pdf/2504.20157) | [摘要](paper/RLHF-ICLR-2026-Toward-Evaluative-Thinking-Meta-Policy-Optimization-with-Evolving-Reward-Models.md) | - |
| 2026 | arXiv | Better LLM Reasoning via Dual-Play | [查看](https://arxiv.org/abs/2511.11881v3) | [摘要](paper/RLHF-arXiv-2026-Better%20LLM%20Reasoning%20via%20Dual-Play.md) | [代码](https://hcy123902.github.io/PasoDoble/) |
| 2026 | ICLR | TreeSearch for LLM Agent Reinforcement Learning | [查看](https://arxiv.org/abs/2509.21240) | [摘要](paper/RLHF-ICLR-2026-TreeSearch%20for%20LLM%20Agent%20Reinforcement%20Learning.md) | [代码](https://github.com/AMAP-ML/Tree-GRPO) |

</details>

<a id="us"></a>
<details>
<summary>🕹️ <b>User Simulation & Interactive Environments</b> · 11 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2006 | KER | A Survey of Statistical User Simulation Techniques for RL Dialogue Management | [查看](https://doi.org/10.1017/S0269888906000944) | [摘要](paper/US-KER-2006-A-Survey-of-Statistical-User-Simulation-Techniques-for-RL-Dialogue-Management.md) | - |
| 2023 | TOIS | Metaphorical User Simulators for Evaluating Task-oriented Dialogue Systems | [查看](https://doi.org/10.1145/3596510) | [摘要](paper/US-TOIS-2023-Metaphorical%20User%20Simulators%20for%20Evaluating%20Task-oriented%20Dialogue%20Systems.md) | [代码](http://github.com/sunnweiwei/MetaSim); [代码](https://github.com/Superbooming/simtester) |
| 2024 | ICLR | SOTOPIA- Interactive Evaluation for Social Intelligence in Language Agents | [查看](https://arxiv.org/abs/2310.11667) | [摘要](paper/US-ICLR-2024-SOTOPIA-%20Interactive%20Evaluation%20for%20Social%20Intelligence%20in%20Language%20Agents.md) | - |
| 2024 | WWW | An In-depth Investigation of User Response Simulation for Conversational Search | [查看](https://dl.acm.org/doi/10.1145/3589334.3645447) | [摘要](paper/US-WWW-2024-An%20In-depth%20Investigation%20of%20User%20Response%20Simulation%20for%20Conversational%20Search.md) | [代码](https://anonymous.4open.science/r/UserSimulation-7091) |
| 2024 | AAAI | Adversarial Socialbots Modeling Based on Structural Information Principles | [查看](https://ojs.aaai.org/index.php/AAAI/article/view/27793) | [摘要](paper/US-AAAI-2024-Adversarial%20Socialbots%20Modeling%20Based%20on%20Structural%20Information%20Principles.md) | [代码](https://github.com/SELGroup/SIASM) |
| 2024 | arXiv | Strength Lies in Differences! Improving Strategy Planning for Non-collaborative Dialogues via Diversified User Simulation | [查看](https://arxiv.org/pdf/2403.06769v3.pdf) | [摘要](paper/US-arXiv-2024-Strength%20Lies%20in%20Differences!%20Improving%20Strategy%20Planning%20for%20Non-collaborative%20Dialogues%20via%20Diversified%20User%20Simulation.md) | - |
| 2025 | SIGDIAL | Generating Diverse Personas for User Simulators to Test Interview Dialogue Systems | [查看](https://aclanthology.org/2025.sigdial-1.54/) | [摘要](paper/US-SIGDIAL-2025-Generating%20Diverse%20Personas%20for%20User%20Simulators%20to%20Test%20Interview%20Dialogue%20Systems.md) | - |
| 2025 | SIGIR | Simulating Before Planning- Constructing Intrinsic User World Model for User-Tailored Dialogue Policy Planning | [查看](https://doi.org/10.1145/3726302.3730084) | [摘要](paper/US-SIGIR-2025-Simulating%20Before%20Planning-%20Constructing%20Intrinsic%20User%20World%20Model%20for%20User-Tailored%20Dialogue%20Policy%20Planning.md) | - |
| 2025 | SIGIR | Theory and Toolkits for User Simulation in the Era of Generative AI- User Modeling, Synthetic Data Generation, and System Evaluation | [查看](https://doi.org/10.1145/3726302.3731697) | [摘要](paper/US-SIGIR-2025-Theory%20and%20Toolkits%20for%20User%20Simulation%20in%20the%20Era%20of%20Generative%20AI-%20User%20Modeling%2C%20Synthetic%20Data%20Generation%2C%20and%20System%20Evaluation.md) | - |
| 2025 | WWW | A LLM-based Controllable, Scalable, Human-Involved User Simulator Framework for Conversational Recommender Systems | [查看](https://doi.org/10.1145/3696410.3714858) | [摘要](paper/US-WWW-2025-A%20LLM-based%20Controllable%2C%20Scalable%2C%20Human-Involved%20User%20Simulator%20Framework%20for%20Conversational%20Recommender%20Systems.md) | [代码](https://github.com/zlxxlz1026/CSHI) |
| 2025 | NeurIPS | Goal Alignment in LLM-Based User Simulators for Conversational AI | [查看](https://arxiv.org/abs/2507.20152) | [摘要](paper/US-NeurIPS-2025-Goal%20Alignment%20in%20LLM-Based%20User%20Simulators%20for%20Conversational%20AI.md) | [代码](https://github.com/Shuhaibm/user_simulator_goal_alignment) |

</details>

<a id="data"></a>
<details>
<summary>📊 <b>Benchmark & Evaluation</b> · 20 篇</summary>

| 年份 | 会议/期刊 | 论文 | 链接 | 摘要 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 2024 | ACL | Evaluating Intention Detection Capability of Large Language Models in Persuasive Dialogues | [查看](https://aclanthology.org/2024.acl-long.90.pdf) | [摘要](paper/Data-ACL-2024-Evaluating%20Intention%20Detection%20Capability%20of%20Large%20Language%20Models%20in%20Persuasive%20Dialogues.md) | [代码](https://github.com/Syuko4omi/LLM_intention_detection_public) |
| 2024 | ICML | Agent-as-a-Judge- Evaluate Agents with Agents | [查看](https://arxiv.org/abs/2410.10934) | [摘要](paper/Data-ICML-2024-Agent-as-a-Judge-%20Evaluate%20Agents%20with%20Agents.md) | [代码](https://github.com/metauto-ai/agent-as-a-judge) |
| 2025 | AAAI | MuMA-ToM- Multi-modal Multi-Agent Theory of Mind | [查看](https://arxiv.org/abs/2408.12574) | [摘要](paper/Data-AAAI-2025-MuMA-ToM-%20Multi-modal%20Multi-Agent%20Theory%20of%20Mind.md) | [代码](https://scai.cs.jhu.edu/projects/MuMA-ToM/) |
| 2025 | AAAI | ToMATO: Verbalizing the Mental States of Role-Playing LLMs for Benchmarking Theory of Mind | [查看](https://arxiv.org/abs/2501.08838) | [摘要](paper/Data-AAAI-2025-ToMATO-%20Verbalizing%20the%20Mental%20States%20of%20Role-Playing%20LLMs%20for%20Benchmarking%20Theory%20of%20Mind.md) | [代码](https://github.com/nttmdlab-nlp/ToMATO) |
| 2025 | ACL | Towards Dynamic Theory of Mind- Evaluating LLM Adaptation to Temporal Evolution of Human States | [查看](https://arxiv.org/abs/2505.17663) | [摘要](paper/Data-ACL-2025-Towards%20Dynamic%20Theory%20of%20Mind-%20Evaluating%20LLM%20Adaptation%20to%20Temporal%20Evolution%20of%20Human%20States.md) | [代码](https://github.com/GAIR-NLP/DynToM) |
| 2025 | EMNLP | MOMENT S- A Comprehensive Multimodal Benchmark for Theory of Mind | [查看](https://aclanthology.org/2025.findings-emnlp.1230.pdf) | [摘要](paper/Data-EMNLP-2025-MOMENT%20S-%20A%20Comprehensive%20Multimodal%20Benchmark%20for%20Theory%20of%20Mind.md) | [代码](https://github.com/villacu/MoMentS) |
| 2025 | ICLR | Explore theory of mind: program-guided adversarial data generation for theory of mind reasoning | [查看](https://arxiv.org/abs/2412.12175) | [摘要](paper/Data-ICLR-2025-Explore%20Theory%20of%20Mind-%20PROGRAM-GUIDED%20ADVERSARIAL%20DATA%20GENERATION%20FOR%20THEORY%20OF%20MIND%20REASONING.md) | [代码](https://github.com/facebookresearch/exploretom) |
| 2025 | NAACL | Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLM Communication | [查看](https://aclanthology.org/2025.naacl-main.287/) | [摘要](paper/Data-NAACL-2025-Communication%20Makes%20Perfect%3A%20Persuasion%20Dataset%20Construction%20via%20Multi-LLM%20Communication.md) | [代码](https://github.com/HF-heaven/LLM-based_persuasion_simulator) |
| 2026 | AAAI | RecToM: A Benchmark for Evaluating Machine Theory of Mind in LLM-based Conversational Recommender Systems | [查看](https://arxiv.org/abs/2511.22275) | [摘要](paper/Data-AAAI-2026-RecToM-%20A%20Benchmark%20for%20Evaluating%20Machine%20Theory%20of%20Mind%20in%20LLM-based%20Conversational%20Recommender%20Systems.md) | [代码](https://github.com/CGCL-codes/RecToM) |
| 2026 | arXiv | EnactToM- An Evolving Benchmark for Functional Theory of Mind in Embodied Agents | [查看](https://arxiv.org/abs/2605.09826) | [摘要](paper/Data-arXiv-2026-EnactToM-%20An%20Evolving%20Benchmark%20for%20Functional%20Theory%20of%20Mind%20in%20Embodied%20Agents.md) | [代码](https://enact-tom.github.io/) |
| 2026 | arXiv | Large language model psychometrics- A systematic review of evaluation, validation, and enhancement | [查看](https://arxiv.org/abs/2505.08245) | [摘要](paper/Data-arXiv-2026-Large%20language%20model%20psychometrics-%20A%20systematic%20review%20of%20evaluation%2C%20validation%2C%20and%20enhancement.md) | [代码](https://github.com/valuebyte-ai/Awesome-LLM-Psychometrics) |
| 2026 | WWW | ES-MemEval- Benchmarking Conversational Agents on Personalized Long-Term Emotional Support | [查看](https://doi.org/10.1145/3774904.3792143) | [摘要](paper/Data-WWW-2026-ES-MemEval-%20Benchmarking%20Conversational%20Agents%20on%20Personalized%20Long-Term%20Emotional%20Support.md) | [代码](https://github.com/slptongji/ES-MemEval) |
| 2019 | CVPR | Social-IQ- A Question Answering Benchmark for Artificial Social Intelligence | [查看](https://openaccess.thecvf.com/content_CVPR_2019/html/Zadeh_Social-IQ_A_Question_Answering_Benchmark_for_Artificial_Social_Intelligence_CVPR_2019_paper.html) | [摘要](paper/Data-CVPR-2019-Social-IQ-%20A%20Question%20Answering%20Benchmark%20for%20Artificial%20Social%20Intelligence.md) | - |
| 2023 | ICCV | Social-IQ 2.0 Challenge- Benchmarking Multimodal Social Understanding | [查看](https://cmu-multicomp-lab.github.io/social-iq-2.0/) | [摘要](paper/Data-ICCV-2023-Social-IQ%202.0%20Challenge-%20Benchmarking%20Multimodal%20Social%20Understanding.md) | [代码](https://github.com/abwilf/Social-IQ-2.0-Challenge) |
| 2025 | ACL | DICE-BENCH- Evaluating the Tool-Use Capabilities of Large Language Models in Multi-Round, Multi-Party Dialogues | [查看](-) | [摘要](paper/Data-ACL-2025-DICE-BENCH-%20Evaluating%20the%20Tool-Use%20Capabilities%20of%20Large%20Language%20Models%20in%20Multi-Round,%20Multi-Party%20Dialogues.md) | [代码](https://github.com/snuhcc/DICE-Bench) |
| 2025 | ACL | In Search of the Lost Arch in Dialogue- A Dependency Dialogue Acts Corpus for Multi-Party Dialogues | [查看](https://aclanthology.org/2025.findings-acl.1032/) | [摘要](paper/Data-ACL-2025-In%20Search%20of%20the%20Lost%20Arch%20in%20Dialogue-%20A%20Dependency%20Dialogue%20Acts%20Corpus%20for%20Multi-Party%20Dialogues.md) | - |
| 2025 | NAACL | WHoW- A Cross-domain Approach for Analysing Conversation Moderation | [查看](https://aclanthology.org/2025.naacl-long.105/) | [摘要](paper/Data-NAACL-2025-WHoW-%20A%20Cross-domain%20Approach%20for%20Analysing%20Conversation%20Moderation.md) | - |
| 2025 | arXiv | You need to MIMIC to get FAME- Solving Meeting Transcript Scarcity with Multi-Agent Conversations | [查看](https://arxiv.org/abs/2502.13001) | [摘要](paper/Data-arXiv-2025-You%20need%20to%20MIMIC%20to%20get%20FAME-%20Solving%20Meeting%20Transcript%20Scarcity%20with%20Multi-Agent%20Conversations.md) | - |
| 2026 | arXiv | PIVOTSBench- Evaluating Fine-Grained Interpersonal Relationship Reasoning in Multimodal Large Language Models | [查看](https://arxiv.org/abs/2606.23092) | [摘要](paper/Data-arXiv-2026-PIVOTSBench-%20Evaluating%20Fine-Grained%20Interpersonal%20Relationship%20Reasoning%20in%20Multimodal%20Large%20Language%20Models.md) | - |
| 2026 | arXiv | TIDES- A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics | [查看](https://arxiv.org/abs/2608.01724) | [摘要](paper/Data-arXiv-2026-TIDES-%20A%20Longitudinal%20Bilingual%20Dataset%20for%20Modeling%20Multi-Party%20Social%20Dynamics.md) | - |

</details>

---

<a id="repo-structure"></a>
## 📁 仓库结构

```
Awesome-Social-AI/
├── image/              # 存放论文相关的图片、图表等
├── paper/              # 论文摘要（main，按 8 个方向前缀命名）
├── Example.md          # 论文摘要的撰写范例
└── README.md           # 本说明文件
```

---

<a id="contributing"></a>
## ✍️ 如何贡献
我们鼓励所有成员积极贡献自己阅读的论文摘要，请严格遵循以下步骤：

### 1. Fork & Clone
Fork 本仓库到你的 GitHub 账户，然后克隆到本地。
```
git clone https://github.com/你的用户名/Awesome-Social-AI.git && cd Awesome-Social-AI
```

### 2. 添加原始仓库为 upstream
```
git remote add upstream https://github.com/lucianma05-create/Awesome-Social-AI.git
```

### 3. 每次准备撰写新摘要前，请先同步主分支并创建一个独立分支：
1)  切换回主分支并拉取上游最新代码
```
git checkout main
git pull upstream main
```
2) 创建并切换到一个新分支 (分支名建议反映论文内容)
```
git checkout -b 分支名
```
### 4. 命名规范
```
\paper 下的文件名请严格按照以下格式命名，以便于检索和管理：
[方向]-[会议/期刊名]-[年份]-[论文名(完整的名字而不是缩写)].md
示例: Memory-NeurIPS-2023-Retrieval-Augmented-Generation.md
研究方向请从当前 8 个方向中选择最接近的归类；确需新增方向时，请先在组内讨论后再添加。
当前方向前缀：PD、ED、Recommend、Coop、ToM、Emotion、Norms、Memory、RLHF、US、Data。
\image 下的文件命名为 [年]-[月]-[日]-[编号]-[姓名缩写].png
示例：2024010101mmh.png
```
### 5. 填写内容
a. 参照 Example.md 中的模板，填写论文的各项信息，确保内容精炼、准确。 

b. 或者可以使用我们专门开发的 [Auto-Summary](https://github.com/lucianma05-create/Auto-Summary), 请在自动化生成后进行必要的人工校对和修改。

### 6. 修改 README.md
参照 README.md 中的表格，增加新论文的链接、摘要和代码；可以用以下提示词提示codex或copilot进行自动化填充：
```
请根据 paper 目录新增的 .md 文件，按 README.md 里现有表格格式补全相应方向的行，填 链接、摘要、代码 字段，缺失用 - 
```
或运行仓库自带的同步脚本，自动把 paper/ 目录的新论文填入表格：
```
python scripts/update_readme.py --dry-run   # 预览改动
python scripts/update_readme.py             # 应用改动
```
### 7. 提交、同步与推送
1) 暂存并提交本地更改
```
git add .
git commit -m "你的提交信息，例如：Add summary for [论文名]"
```
2)  推送当前功能分支到你个人的 GitHub (origin)
```
git push origin 分支名
```
### 8. 发起 Pull Request
```
向本仓库的主分支发起一个 Pull Request (PR)，并等待审核合并。
```
---

<a id="about"></a>
## 🧠 关于我们

本仓库由 NWPU Crowd-HMT-Lab Social-AI-Group 维护。
