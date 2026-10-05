<div align="center">

# 🌐 Awesome Social AI

> A curated collection of research on socially intelligent conversational agents.
>
> Focusing on conversational agents that understand social contexts, reason about others' states, engage in appropriate interactions, and adapt through long-term interaction.

[![Awesome](https://img.shields.io/badge/Awesome-0066CC?style=for-the-badge&logo=awesome-lists&logoColor=white)](https://github.com/sindresorhus/awesome)
[![License](https://img.shields.io/badge/License-Apache%202.0-red?style=for-the-badge&logo=apache&logoColor=white)](http://www.apache.org/licenses/LICENSE-2.0)
[![Papers](https://img.shields.io/badge/Papers-279-2ea44f?style=for-the-badge)](paper)
[![Summaries](https://img.shields.io/badge/Summaries-121-007ec6?style=for-the-badge)](README.md)
[![Views](https://komarev.com/ghpvc/?username=lucianma05-create&repo=Awesome-Social-AI&label=Views&color=orange&style=for-the-badge)](https://github.com/lucianma05-create/Awesome-Social-AI)
</div>

**[English](README.md)** | **[简体中文](README_CN.md)**

**We curate Social AI research papers for conversational agents with continuously updated Chinese summaries, helping you quickly get up to speed with representative work in this field. The repository is under active development. Follow and Star ⭐**

<a id="toc"></a>
## 📑 Table of Contents

- [🌐 Awesome Social AI](https://github.com/lucianma05-create/Awesome-Social-AI)
  - [📑 Table of Contents](#toc)
  - [🎯 Scope & Structure](#social-ai)
  - [📚 Paper List](#papers)
    - [Persuasion & Negotiation](#pd)
    - [Empathy & Emotional Support](#ed)
    - [Conversational Recommendation](#recommend)
    - [Cooperation & Collaboration](#coop)
    - [Theory of Mind](#tom)
    - [Affect & Social Perception](#emotion)
    - [Social Context, Norms & Morality](#norms)
    - [Social Memory & Adaptation](#memory)
    - [Learning, Planning & Alignment](#rlhf)
    - [User Simulation & Interactive Environments](#us)
    - [Benchmark & Evaluation](#data)
  - [🏷️ Keyword System](#keywords)
  - [📁 Repository Structure](#repo-structure)
  - [✍️ How to Contribute](#contributing)
  - [🧠 About Us](#about)

<a id="social-ai"></a>
## 🎯 Scope & Structure

**Social AI** is the field of research and construction of AI systems that can interact appropriately with humans or other agents in dynamic social situations. This repository focuses on its **conversational agent** side: language interaction is the primary modality; multimodal or embodied work is included only when it explicitly serves interactive social agents.

Social intelligence here comprises four interacting groups of abilities:

- **Social perception & understanding**: recognizing emotions, intentions, beliefs, relationships, roles, and group dynamics from verbal and non-verbal cues;
- **Social context modeling & reasoning**: combining norms, culture, relationships, tasks, and interaction history to infer others' states, common ground, and the consequences of actions;
- **Social action & interaction**: achieving social goals through communication, collaboration, support, coordination, or influence, while maintaining appropriate relationships;
- **Social learning & adaptation**: using interaction feedback and long-term social memory to adapt the understanding of users, relationships, and situations.

This definition draws on research on social perception, social knowledge, social memory, social reasoning, mental-state modeling, and social interaction. See [Mathur et al., 2024](https://aclanthology.org/2024.emnlp-main.1143/) and [Ziems et al., 2024](https://aclanthology.org/2024.findings-acl.163/).

Each paper has one **primary section** for browsing plus cross-cutting **Keywords** describing its goal, capabilities, contexts, and methods. The primary section organizes the repository for browsing and does not imply a mutually exclusive theoretical hierarchy:

- **Task layer · Social tasks**
  - [Persuasion & Negotiation](#pd) — research, methods, and evaluation for strategic dialogue such as persuasion and negotiation
  - [Empathy & Emotional Support](#ed) — empathetic dialogue, emotional support, and counseling
  - [Conversational Recommendation](#recommend) — conversational recommender systems
  - [Cooperation & Collaboration](#coop) — cooperation, collaboration, and multi-party consensus building
- **Capability layer · Social cognition**
  - [Theory of Mind](#tom) — mental-state modeling, intention and belief reasoning
  - [Affect & Social Perception](#emotion) — affective states, social cues, and emotion reasoning
  - [Social Context, Norms & Morality](#norms) — roles, relationships, culture, norms, and moral contexts
  - [Social Memory & Adaptation](#memory) — long-term social memory, personalization, and interaction adaptation
- **Method layer · Supporting techniques**
  - [Learning, Planning & Alignment](#rlhf) — learning, planning, and alignment methods serving social adaptation
- **Resource layer · Research infrastructure**
  - [User Simulation & Interactive Environments](#us) — user simulation, interactive environments, and simulation
  - [Benchmark & Evaluation](#data) — benchmarks, datasets, and evaluation

Excluded: pure computational social science / "AI for social science" work, pure static emotion classification, pure visual ToM, pure general RL or alignment work. Work is included as an exception when it explicitly serves conversational or interactive social agents.

**Reference papers:**
> 1. [Towards Social AI: A Survey on Understanding Social Interactions](https://arxiv.org/abs/2409.15316)
> 2. [Advancing Social Intelligence in AI Agents: Technical Challenges and Open Questions](https://aclanthology.org/2024.emnlp-main.1143/)

<a id="papers"></a>
## 📚 Paper List

> This catalogue is auto-generated from `metadata/papers.json` and renders each paper in the Awesome-RLHF style: Publisher, Keywords, Code, and Summary. Titles stay clean; keywords appear as a separate field whose meaning is defined by the controlled vocabulary and mapping below. A Summary link appears only when a local Chinese note exists. See [metadata/KEYWORDS.md](metadata/KEYWORDS.md) for the full vocabulary, definitions, and review policy.

<a id="pd"></a>
<details>
<summary>🗣️ <b>Persuasion & Negotiation</b> · 46 papers</summary>

<!-- CATALOGUE:START -->
- [A Systematic Framework for Designing and Evaluating Persuasive Systems](https://doi.org/10.1007/978-3-540-68504-3_15)
  - Publisher: `PERSUASIVE 2008`
  - Keywords: `Method` · `Influence` · `Social Context` · `Relationship & Role`
  - Summary: [Summary](paper/PD-PERSUASIVE-2008-A%20Systematic%20Framework%20for%20Designing%20and%20Evaluating%20Persuasive%20Systems.md)
- [Measure Of Belief Change as an Evaluation of Persuasion](https://www.researchgate.net/publication/228964262_Measure_Of_Belief_Change_as_an_Evaluation_of_Persuasion)
  - Keywords: `Evaluation` · `Influence`
  - Summary: [Summary](paper/PD-%E6%9C%AA%E6%8F%90%E5%8F%8A-2008-Measure%20Of%20Belief%20Change%20as%20an%20Evaluation%20of%20Persuasion.md)
- [Reinforcement Learning of Cooperative Persuasive Dialogue Policies using Framing](https://aclanthology.org/C14-1161/)
  - Publisher: `COLING 2014`
  - Keywords: `Method` · `Influence` · `Social Context` · `RL` · `User Simulation` · `Reward Modeling`
  - Summary: [Summary](paper/PD-COLING-2014-Reinforcement-Learning-of-Cooperative-Persuasive-Dialogue-Policies-using-Framing.md)
- [Persuasive Argumentation and Emotions- An Empirical Evaluation with Users](https://doi.org/10.1007/978-3-319-58071-5_50)
  - Publisher: `HCI 2017`
  - Keywords: `Method` · `Influence` · `Social Context`
  - Summary: [Summary](paper/PD-HCI-2017-Persuasive%20Argumentation%20and%20Emotions-%20An%20Empirical%20Evaluation%20with%20Users.md)
- [Improving Dialog Systems for Negotiation with Personality Modeling](https://arxiv.org/abs/2010.09954)
  - Publisher: `arXiv 2020`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Social Context` · `Personalization` · `User Simulation`
- [Opponent Modeling in Negotiation Dialogues by Related Data Adaptation](https://arxiv.org/abs/2205.00344)
  - Publisher: `arXiv 2022`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Multi-party` · `Supervised Learning`
- [Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback](https://arxiv.org/abs/2305.10142)
  - Publisher: `arXiv 2023`
  - Keywords: `Method` · `Coordination` · `Social Memory & Adaptation` · `Relationship & Role` · `Self-play` · `Multi-turn`
  - Summary: [Summary](paper/PD-arXiv-2023-Improving-Language-Model-Negotiation-with-Self-Play-and-In-Context-Learning-from-AI-Feedback.md)
- [Strategic argumentation dialogues for persuasion- Framework and experiments based on modelling the beliefs and concerns of the persuadee](https://doi.org/10.3233/AAC-210005)
  - Publisher: `ArgComp 2023`
  - Keywords: `Method` · `Influence` · `Mental-State Modeling` · `Interaction Management` · `Personalization` · `Planning` · `Multi-turn`
  - Summary: [Summary](paper/PD-ArgComp-2023-Strategic%20argumentation%20dialogues%20for%20persuasion-%20Framework%20and%20experiments%20based%20on%20modelling%20the%20beliefs%20and%20concerns%20of%20the%20persuadee.md)
- [Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation](https://papers.nips.cc/paper_files/paper/2024/hash/984dd3db213db2d1454a163b65b84d08-Abstract-Datasets_and_Benchmarks_Track.html)
  - Publisher: `NeurIPS 2024`
  - Keywords: `Benchmark` · `Coordination` · `Interaction Management` · `Social Perception` · `Multi-party` · `Relationship & Role` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/S-Abdelnabi/LLM-Deliberation)
- [Debating with More Persuasive LLMs Leads to More Truthful Answers](https://proceedings.mlr.press/v235/khan24a.html)
  - Publisher: `ICML 2024`
  - Keywords: `Evaluation` · `Influence` · `Mental-State Modeling` · `Self-play`
  - Code: [GitHub / Project](https://github.com/ucl-dark/llm_debate)
- [How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs](https://aclanthology.org/2024.acl-long.773/)
  - Publisher: `ACL 2024`
  - Keywords: `Method` · `Influence` · `Social Context` · `Norms & Morality` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/CHATS-lab/persuasive_jailbreaker)
- [Measuring Bargaining Abilities of LLMs: A Benchmark and A Buyer-Enhancement Method](https://aclanthology.org/2024.findings-acl.213/)
  - Publisher: `ACL 2024`
  - Keywords: `Method` · `Coordination` · `Interaction Management` · `Relationship & Role` · `Planning`
  - Code: [GitHub / Project](https://github.com/TianXiaSJTU/AmazonPriceHistory)
- [NegotiationToM: A Benchmark for Stress-testing Machine Theory of Mind on Negotiation Surrounding](https://aclanthology.org/2024.findings-emnlp.244/)
  - Publisher: `EMNLP 2024`
  - Keywords: `Benchmark` · `Coordination` · `Mental-State Modeling` · `Relationship & Role`
  - Code: [GitHub / Project](https://github.com/HKUST-KnowComp/NegotiationToM)
- [Plug-and-Play Policy Planner for LLM-Powered Dialogue Agents](https://arxiv.org/pdf/2311.00262.pdf)
  - Publisher: `ICLR 2024`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `Supervised Learning` · `RL` · `Self-play`
  - Code: [GitHub / Project](https://github.com/dengyang17/PPDPP)
  - Summary: [Summary](paper/PD-ICLR-2024-Plug-and-Play%20Policy%20Planner%20for%20LLM-Powered%20Dialogue%20Agents.md)
- [ASTRO: Automatic Strategy Optimization For Non-Cooperative Dialogues](https://aclanthology.org/2025.findings-acl.22.pdf)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `Influence` · `Interaction Management` · `Planning` · `RL` · `Self-play`
  - Code: [GitHub / Project](https://github.com/SCUNLP/ASTRO)
  - Summary: [Summary](paper/PD-ACL-2025-ASTRO:%20Automatic%20Strategy%20Optimization%20For%20Non-Cooperative%20Dialogues.md)
- [Battling against Tough Resister- Strategy Planning with Adversarial Game for Non-collaborative Dialogues](https://aclanthology.org/2025.acl-long.184/)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `Influence` · `Mental-State Modeling` · `Interaction Management` · `Multi-party` · `RL` · `Self-play` · `Planning` · `Multi-turn`
  - Summary: [Summary](paper/PD-ACL-2025-Battling%20against%20Tough%20Resister-%20Strategy%20Planning%20with%20Adversarial%20Game%20for%20Non-collaborative%20Dialogues.md)
- [Communication is All You Need: Persuasion Dataset Construction via Multi-LLM Communication](https://aclanthology.org/2025.naacl-long.203/)
  - Publisher: `NAACL 2025`
  - Keywords: `Method` · `Influence` · `Social Context` · `Norms & Morality` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/HF-heaven/LLM-based_persuasion_simulator)
- [Disagreements in Reasoning: How a Model's Thinking Process Dictates Persuasion in Multi-Agent Systems](https://arxiv.org/abs/2503.09999)
  - Publisher: `arXiv 2025`
  - Keywords: `Evaluation` · `General Interaction`
  - Summary: [Summary](paper/PD-arXiv-2025-Disagreements-in-Reasoning-How-a-Model%E2%80%99s-Thinking-Process-Dictates-Persuasion-in-Multi-Agent-Systems.md)
- [Durably reducing conspiracy beliefs through dialogues with AI](https://www.science.org/doi/10.1126/science.adq1814)
  - Publisher: `Science 2025`
  - Keywords: `Evaluation` · `Influence` · `Interaction Management` · `Multi-turn`
  - Summary: [Summary](paper/PD-Science-2025-Durably%20reducing%20conspiracy%20beliefs%20through%20dialogues%20with%20AI.md)
- [Enhancing LLM-Based Persuasion Simulations with Cultural and Speaker-Specific Information](https://aclanthology.org/2025.findings-emnlp.808)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Influence` · `Social Context` · `Culture` · `Relationship & Role` · `Planning`
  - Code: [GitHub / Project](https://github.com/HF-heaven/Cross-Cultural-Persuasion-Simulations)
  - Summary: [Summary](paper/PD-EMNLP-2025-Enhancing%20LLM-Based%20Persuasion%20Simulations%20with%20Cultural%20and%20Speaker-Specific%20Information.md)
- [Enhancing Persuasive Dialogue Agents by Synthesizing Cross-Disciplinary Communication Strategies](https://aclanthology.org/2025.emnlp-industry.158/)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Influence` · `Social Context` · `Planning`
  - Summary: [Summary](paper/PD-EMNLP-2025-Enhancing%20Persuasive%20Dialogue%20Agents%20by%20Synthesizing%20Cross-Disciplinary%20Communication%20Strategies.md)
- [EPO: Explicit Policy Optimization for Strategic Reasoning in LLMs via RL](https://aclanthology.org/2025.acl-long.747/)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `General Interaction` · `Social Context` · `RL` · `Reward Modeling` · `Self-play` · `Multi-turn`
  - Summary: [Summary](paper/PD-ACL-2025-EPO-Explicit-Policy-Optimization-for-Strategic-Reasoning-in-LLMs-via-RL.md)
- [EvoEmo: Evolved Emotional Policies for Adversarial LLM Agents in Multi-Turn Price Negotiation](https://arxiv.org/abs/2502.07483)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction`
  - Summary: [Summary](paper/PD-arXiv-2025-EvoEmo-Evolved-Emotional-Policies-for-Adversarial-LLM-Agents-in-Multi-Turn-Price-Negotiation.md)
- [From Simulation to Strategy: Automating Personalized Interaction Planning for Conversational Agents](https://arxiv.org/abs/2502.13289)
  - Publisher: `arXiv 2025`
  - Keywords: `Dataset` · `General Interaction` · `Supervised Learning`
  - Summary: [Summary](paper/PD-arXiv-2025-From-Simulation-to-Strategy-Automating-Personalized-Interaction-Planning-for-Conversational-Agents.md)
- [Human Choice Prediction in Language-based Persuasion Games- Simulation-based Off-Policy Evaluation](https://doi.org/10.1162/TACL.a.16)
  - Publisher: `TACL 2025`
  - Keywords: `Method` · `Influence` · `Mental-State Modeling` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/eilamshapira/HumanChoicePrediction)
  - Summary: [Summary](paper/PD-TACL-2025-Human%20Choice%20Prediction%20in%20Language-based%20Persuasion%20Games-%20Simulation-based%20Off-Policy%20Evaluation.md)
- [LLM Can be a Dangerous Persuader- Empirical Study of Persuasion Safety in Large Language Models](https://arxiv.org/abs/2504.10430)
  - Publisher: `arXiv 2025`
  - Keywords: `Evaluation` · `Influence` · `Mental-State Modeling` · `Norms & Morality` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/PLUM-Lab/PersuSafety)
  - Summary: [Summary](paper/PD-arXiv-2025-LLM%20Can%20be%20a%20Dangerous%20Persuader-%20Empirical%20Study%20of%20Persuasion%20Safety%20in%20Large%20Language%20Models.md)
- [Measuring and Benchmarking Large Language Models' Capabilities to Generate Persuasive Language](https://aclanthology.org/2025.naacl-long.506/)
  - Publisher: `NAACL 2025`
  - Keywords: `Dataset` · `Influence` · `Affect` · `Supervised Learning`
- [Persuade Me if You Can- A Framework for Evaluating Persuasion Effectiveness and Susceptibility Among Large Language Models](https://arxiv.org/abs/2503.01829)
  - Publisher: `NeurIPS 2025`
  - Keywords: `Evaluation` · `Influence` · `Interaction Management` · `Relationship & Role` · `Norms & Morality` · `Multi-turn`
  - Code: [GitHub / Project](https://beyzabozdag.github.io/PMIYC/)
  - Summary: [Summary](paper/PD-NeurIPS-2025-Persuade%20Me%20if%20You%20Can-%20A%20Framework%20for%20Evaluating%20Persuasion%20Effectiveness%20and%20Susceptibility%20Among%20Large%20Language%20Models.md)
- [Persuasion Should be Double-Blind: A Multi-Domain Dialogue Dataset With Faithfulness Based on Causal Theory of Mind](https://arxiv.org/abs/2501.10832)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `User Simulation`
  - Summary: [Summary](paper/PD-arXiv-2025-Persuasion-Should-be-Double-Blind-A-Multi-Domain-Dialogue-Dataset-With-Faithfulness-Based-on-Causal-Theory-of-Mind.md)
- [Persuasion-Dynamics in LLMs: Investigating Robustness and Adaptability in Knowledge and Safety with DuET-PD](https://aclanthology.org/2025.emnlp-main.81/)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Influence` · `Social Context` · `Norms & Morality` · `Preference Optimization` · `Multi-turn`
  - Summary: [Summary](paper/PD-EMNLP-2025-Persuasion-Dynamics-in-LLMs-Investigating-Robustness-and-Adaptability-in-Knowledge-and-Safety-with-DuET-PD.md)
- [Persuasive Conversational Agents for Environmental Sustainability: A Survey](https://doi.org/10.1145/3774751)
  - Publisher: `CSUR 2025`
  - Keywords: `Survey` · `Influence`
  - Summary: [Summary](paper/PD-CSUR-2025-Persuasive-Conversational-Agents-for-Environmental-Sustainability-A-Survey.md)
- [PRINCIPLES- Synthetic Strategy Memory for Proactive Dialogue Agents](https://arxiv.org/abs/2509.17459)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Support` · `Interaction Management` · `Self-play` · `Retrieval`
  - Code: [GitHub / Project](https://huggingface.co/spaces/kimnamssya/Principles)
  - Summary: [Summary](paper/PD-EMNLP-2025-PRINCIPLES-%20Synthetic%20Strategy%20Memory%20for%20Proactive%20Dialogue%20Agents.md)
- [Profiling LLM Copyright Infringement Risks under Adversarial Persuasive Prompting](https://aclanthology.org/2025.findings-emnlp.855/)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Influence` · `Planning`
  - Code: [GitHub / Project](https://github.com/Rongite/Persuasion)
  - Summary: [Summary](paper/PD-EMNLP-2025-Profiling-LLM-Copyright-Infringement-Risks-under-Adversarial-Persuasive-Prompting.md)
- [Simulation-free hierarchical latent policy planning for proactive dialogues](https://arxiv.org/abs/2412.14584)
  - Publisher: `AAAI 2025`
  - Keywords: `Method` · `Support` · `Interaction Management` · `RL`
  - Summary: [Summary](paper/PD-AAAI-2025-Simulation-free%20hierarchical%20latent%20policy%20planning%20for%20proactive%20dialogues.md)
- [Teaching models to balance resisting and accepting persuasion](https://aclanthology.org/2025.naacl-long.412/)
  - Publisher: `NAACL 2025`
  - Keywords: `Method` · `Influence` · `Social Context` · `Multi-party` · `Preference Optimization` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/esteng/persuasion_balanced_training)
- [The Levers of Political Persuasion](https://www.science.org/doi/10.1126/science.aea3884)
  - Publisher: `Science 2025`
  - Keywords: `Evaluation` · `Influence` · `Social Perception` · `Personalization` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/kobihackenburg/scaling-conversational-AI)
  - Summary: [Summary](paper/PD-Science-2025-The%20Levers%20of%20Political%20Persuasion.md)
- [ToMAP: Training Opponent-Aware LLM Persuaders with Theory of Mind](https://arxiv.org/abs/2505.22961)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `Influence` · `Mental-State Modeling` · `Relationship & Role` · `RL` · `Supervised Learning` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/ulab-uiuc/ToMAP)
  - Summary: [Summary](paper/PD-arXiv-2025-ToMAP:%20Training%20Opponent-Aware%20LLM%20Persuaders%20with%20Theory%20of%20Mind.md)
- [Verbalized Bayesian Persuasion](https://arxiv.org/abs/2503.15477)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Reward Modeling` · `RL`
  - Summary: [Summary](paper/PD-arXiv-2025-Verbalized-Bayesian-Persuasion.md)
- [A Comprehensive Survey of Computational Persuasion](https://dl.acm.org/doi/10.1145/3800687)
  - Publisher: `CSUR 2026`
  - Keywords: `Survey` · `Influence`
  - Code: [GitHub / Project](https://github.com/beyzabozdag/PersuasionSurvey)
  - Summary: [Summary](paper/PD-CSUR-2026-A%20Comprehensive%20Survey%20of%20Computational%20Persuasion.md)
- [MA2P: A Meta-Cognitive Autonomous Intelligent Agents Framework for Complex Persuasion](https://aclanthology.org/2026.findings-acl.1550/)
  - Publisher: `Findings of ACL 2026`
  - Keywords: `Method` · `Influence` · `Mental-State Modeling` · `Social Memory & Adaptation` · `Interaction Management` · `Planning`
- [METRO: Towards Strategy Induction from Expert Dialogue Transcripts for Non-collaborative Dialogues](https://arxiv.org/pdf/2604.11427v3.pdf)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Influence` · `Interaction Management` · `Social Memory & Adaptation` · `Planning`
  - Code: [GitHub / Project](https://github.com/Humphrey-0125/METRO)
  - Summary: [Summary](paper/PD-arXiv-2026-METRO:%20Towards%20Strategy%20Induction%20from%20Expert%20Dialogue%20Transcripts%20for%20Non-collaborative%20Dialogues.md)
- [One Model, All Roles- Multi-Turn, Multi-Agent Self-Play Reinforcement Learning for Conversational Social Intelligence](https://arxiv.org/abs/2602.03109)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Interaction Management` · `Multi-party` · `Norms & Morality` · `Relationship & Role` · `RL` · `Self-play` · `Multi-turn`
- [Personality-Aware Reinforcement Learning for Persuasive Dialogue with LLM-Driven Simulation](https://arxiv.org/abs/2601.06877)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Influence` · `Mental-State Modeling` · `Social Context` · `Personalization` · `RL` · `User Simulation` · `Retrieval` · `Multi-turn`
  - Summary: [Summary](paper/PD-arXiv-2026-Personality-Aware-Reinforcement-Learning-for-Persuasive-Dialogue-with-LLM-Driven-Simulation.md)
- [RebuttalAgent: Strategic Persuasion in Academic Rebuttal via Theory of Mind](https://arxiv.org/abs/2601.15715)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `Influence` · `Mental-State Modeling` · `Social Context` · `Relationship & Role` · `Supervised Learning` · `RL` · `Reward Modeling`
  - Code: [GitHub / Project](https://github.com/Zhitao-He/RebuttalAgent)
  - Summary: [Summary](paper/PD-ICLR-2026-RebuttalAgent:%20Strategic%20Persuasion%20in%20Academic%20Rebuttal%20via%20Theory%20of%20Mind.md)
- [Strategic Planning and Rationalizing on Trees Make LLMs Better Debaters](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ee3ce0121939f42098cdefd3ea025bf1-Abstract-Conference.html)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `Influence` · `Interaction Management` · `Social Perception` · `Multi-party` · `Planning` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/LeiLiLab/TreeDebater)
- [Towards Strategic Persuasion with Language Models](https://arxiv.org/abs/2509.22989v2)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `Influence` · `RL`
  - Summary: [Summary](paper/PD-ICLR-2026-Towards%20Strategic%20Persuasion%20with%20Language%20Models.md)
<!-- CATALOGUE:END -->



















</details>

<a id="ed"></a>
<details>
<summary>❤️‍🩹 <b>Empathy & Emotional Support</b> · 27 papers</summary>

<!-- CATALOGUE:START -->
- [Towards Emotional Support Dialog Systems](https://aclanthology.org/2021.acl-long.269/)
  - Publisher: `ACL 2021`
  - Keywords: `Dataset` · `Support` · `Affect` · `Relationship & Role`
  - Code: [GitHub / Project](https://github.com/thu-coai/Emotional-Support-Conversation)
- [Improving Multi-turn Emotional Support Dialogue Generation with Lookahead Strategy Planning](https://arxiv.org/abs/2210.04242)
  - Publisher: `arXiv 2022`
  - Keywords: `Method` · `Support` · `Affect` · `Mental-State Modeling` · `Planning` · `Multi-turn`
- [MISC: A Mixed Strategy-Aware Model integrating COMET for Emotional Support Conversation](https://arxiv.org/abs/2203.13560)
  - Publisher: `arXiv 2022`
  - Keywords: `Method` · `Support` · `Mental-State Modeling`
- [CharacterChat- Learning towards Conversational AI with Personalized Social Support](https://arxiv.org/abs/2308.10278)
  - Publisher: `arXiv 2023`
  - Keywords: `System` · `Support` · `Social Memory & Adaptation` · `Personalization` · `Relationship & Role` · `User Simulation` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/morecry/CharacterChat)
  - Summary: [Summary](paper/ED-arXiv-2023-CharacterChat-%20Learning%20towards%20Conversational%20AI%20with%20Personalized%20Social%20Support.md)
- [Facilitating Multi-turn Emotional Support Conversation with Positive Emotion Elicitation: A Reinforcement Learning Approach](https://arxiv.org/abs/2307.07994)
  - Publisher: `arXiv 2023`
  - Keywords: `Method` · `Support` · `Affect` · `Interaction Management` · `RL` · `Reward Modeling` · `Multi-turn`
- [SoulChat- Improving LLMs’ Empathy, Listening, and Comfort Abilities through Fine-tuning with Multi-turn Empathy Conversations](https://aclanthology.org/2023.findings-emnlp.83.pdf)
  - Publisher: `EMNLP 2023`
  - Keywords: `Dataset` · `Support` · `Affect` · `Relationship & Role` · `Supervised Learning` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/scutcyr/SoulChat)
  - Summary: [Summary](paper/ED-EMNLP-2023-SoulChat-%20Improving%20LLMs%E2%80%99%20Empathy%2C%20Listening%2C%20and%20Comfort%20Abilities%20through%20Fine-tuning%20with%20Multi-turn%20Empathy%20Conversations.md)
- [TransESC: Smoothing Emotional Support Conversation via Turn-Level State Transition](https://aclanthology.org/2023.findings-acl.420/)
  - Publisher: `ACL 2023`
  - Keywords: `Method` · `Support` · `Affect` · `Interaction Management` · `Planning`
  - Code: [GitHub / Project](https://github.com/circle-hit/TransESC)
- [Can Large Language Models be Good Emotional Supporter? Mitigating Preference Bias on Emotional Support Conversation](https://aclanthology.org/2024.acl-long.813/)
  - Publisher: `ACL 2024`
  - Keywords: `Evaluation` · `Support` · `Affect`
  - Code: [GitHub / Project](https://github.com/1eastar/EmotionalSupport)
- [EmoBench- Evaluating the Emotional Intelligence of Large Language Models](https://github.com/Sahandfer/EmoBench)
  - Publisher: `ACL 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Affect`
  - Code: [GitHub / Project](https://github.com/Sahandfer/EmoBench)
  - Summary: [Summary](paper/ED-ACL-2024-EmoBench-%20Evaluating%20the%20Emotional%20Intelligence%20of%20Large%20Language%20Models.md)
- [ESCoT: Towards Interpretable Emotional Support Dialogue Systems](https://aclanthology.org/2024.acl-long.723/)
  - Publisher: `ACL 2024`
  - Keywords: `Method` · `Support` · `Affect` · `Mental-State Modeling` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/TeigenZhang/ESCoT)
- [Beyond Verbal Cues: Emotional Contagion Graph Network for Causal Emotion Entailment](https://aclanthology.org/2025.findings-acl.88/)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Social Perception` · `Planning`
  - Code: [GitHub / Project](https://github.com/Yu-Fangxu/ECGN)
- [Chain of Strategy Optimization Makes Large Language Models Better Emotional Supporter](https://arxiv.org/abs/2503.05362)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Support` · `Affect` · `Mental-State Modeling` · `Preference Optimization` · `Planning` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/XingYuSSS/CSO)
  - Summary: [Summary](paper/ED-EMNLP-2025-Chain%20of%20Strategy%20Optimization%20Makes%20Large%20Language%20Models%20Better%20Emotional%20Supporter.md)
- [Customizing Emotional Support: How Do Individuals Construct and Interact With LLM-Powered Chatbots](https://doi.org/10.1145/3706598.3713453)
  - Publisher: `CHI 2025`
  - Keywords: `System` · `Support` · `Social Memory & Adaptation` · `Personalization` · `Longitudinal`
- [Echo-N1- Affective RL Frontier](https://arxiv.org/abs/2512.00344v1)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Mental-State Modeling` · `Personalization` · `RL`
  - Summary: [Summary](paper/ED-arXiv-2025-Echo-N1-%20Affective%20RL%20Frontier.md)
- [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by Modelling MiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.81/)
  - Publisher: `NAACL 2025`
  - Keywords: `Method` · `Support` · `Affect` · `Interaction Management` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/cw-wan/EmoDynamiX-v2)
- [Feel the Difference? A Comparative Analysis of Emotional Arcs in Real and LLM-Generated CBT Sessions](https://arxiv.org/abs/2508.20764)
  - Publisher: `EMNLP 2025`
  - Keywords: `Evaluation` · `Support` · `Affect` · `Relationship & Role`
- [Look Beyond Feeling: Unveiling Latent Needs from Implicit Expressions for Proactive Emotional Support](https://aclanthology.org/2025.emnlp-main.1094/)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Support` · `Affect` · `Mental-State Modeling` · `Supervised Learning`
- [PsyDial- A Large-scale Long-term Conversational Dataset for Mental Health Support](https://aclanthology.org/2025.acl-long.1049/)
  - Publisher: `ACL 2025`
  - Keywords: `Dataset` · `Support` · `Affect` · `Relationship & Role` · `Retrieval` · `Longitudinal`
  - Code: [GitHub / Project](https://github.com/qiuhuachuan/PsyDial)
  - Summary: [Summary](paper/ED-ACL-2025-PsyDial:%20A%20Large-scale%20Long-term%20Conversational%20Dataset%20for%20Mental%20Health%20Support.md)
- [PsyDT- Using LLMs to Construct the Digital Twin of Psychological Counselor with Personalized Counseling Style for Psychological Counseling](https://arxiv.org/pdf/2412.13660)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `Support` · `Personalization`
  - Code: [GitHub / Project](https://github.com/scutcyr/SoulChat2.0)
  - Summary: [Summary](paper/ED-ACL-2025-PsyDT-%20Using%20LLMs%20to%20Construct%20the%20Digital%20Twin%20of%20Psychological%20Counselor%20with%20Personalized%20Counseling%20Style%20for%20Psychological%20Counseling.md)
- [Reinforcement Learning with Verifiable Emotion Rewards for Empathetic Agents](https://arxiv.org/abs/2507.03112v1)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `Support` · `Affect` · `Mental-State Modeling` · `RL` · `Reward Modeling` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/Tencent/DigitalHuman/tree/main/RLVER)
  - Summary: [Summary](paper/ED-arXiv-2025-Reinforcement%20Learning%20with%20Verifiable%20Emotion%20Rewards%20for%20Empathetic%20Agents.md)
- [SAGE- Steering and Refining Dialog Generation with State-Action Augmentation](https://arxiv.org/abs/2503.03040)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Interaction Management` · `Planning` · `Longitudinal`
  - Code: [GitHub / Project](https://github.com/apple/ml-sage-dialog-gen)
  - Summary: [Summary](paper/ED-arXiv-2025-SAGE-%20Steering%20and%20Refining%20Dialog%20Generation%20with%20State-Action%20Augmentation.md)
- [The Pursuit of Empathy: Evaluating Small Language Models for PTSD Dialogue Support](https://aclanthology.org/2025.emnlp-main.1573/)
  - Publisher: `EMNLP 2025`
  - Keywords: `Dataset` · `Support` · `Affect` · `Personalization` · `Supervised Learning`
- [Affective Flow Language Model for Emotional Support Conversation](https://arxiv.org/abs/2602.08826v1)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Support` · `Affect` · `Interaction Management` · `Supervised Learning` · `Preference Optimization` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/chzou25-lgtm/AffectiveFlow)
  - Summary: [Summary](paper/ED-arXiv-2026-Affective%20Flow%20Language%20Model%20for%20Emotional%20Support%20Conversation.md)
- [Emotion Trajectory-aware Retrieval for Markov-driven Emotion Anticipation in LLM-based Emotional Support Conversation](https://aclanthology.org/2026.findings-acl.2127/)
  - Publisher: `Findings of ACL 2026`
  - Keywords: `Method` · `Support` · `Affect` · `Mental-State Modeling` · `Retrieval` · `Planning` · `Supervised Learning`
- [EMPA: Evaluating Persona-Aligned Empathy as a Process](https://arxiv.org/abs/2603.00552)
  - Publisher: `arXiv 2026`
  - Keywords: `Evaluation` · `Support` · `Social Memory & Adaptation` · `Mental-State Modeling` · `Personalization` · `User Simulation` · `Longitudinal`
  - Code: [GitHub / Project](https://github.com/KAYA-HAI/EMPA-Benchmark-EPMSandbox)
  - Summary: [Summary](paper/ED-arXiv-2026-EMPA:%20Evaluating%20Persona-Aligned%20Empathy%20as%20a%20Process.md)
- [PsyProbe: Proactive and Interpretable Dialogue through User State Modeling for Exploratory Counseling](https://arxiv.org/abs/2601.19096)
  - Publisher: `arXiv 2026`
  - Keywords: `System` · `Support` · `Mental-State Modeling` · `Social Memory & Adaptation` · `Interaction Management` · `Culture` · `Planning`
- [You Never Know a Person, You Only Know Their Defenses- Detecting Levels of Psychological Defense Mechanisms in Supportive Conversations](https://aclanthology.org/2026.findings-acl.708/)
  - Publisher: `ACL 2026`
  - Keywords: `Dataset` · `Support` · `Mental-State Modeling` · `Relationship & Role` · `Supervised Learning`
<!-- CATALOGUE:END -->



















</details>

<a id="recommend"></a>
<details>
<summary>🛍️ <b>Conversational Recommendation</b> · 26 papers</summary>

<!-- CATALOGUE:START -->
- [Towards Conversational Recommendation over Multi-Type Dialogs](https://github.com/PaddlePaddle/models/tree/develop/PaddleNLP/Research/ACL2020-DuRecDial)
  - Publisher: `ACL 2020`
  - Keywords: `Dataset` · `Recommendation` · `Personalization`
  - Code: [GitHub / Project](https://github.com/PaddlePaddle/models/tree/develop/PaddleNLP/Research/ACL2020-DuRecDial)
  - Summary: [Summary](paper/Recommend-ACL-2020-Towards%20Conversational%20Recommendation%20over%20Multi-Type%20Dialogs.md)
- [User Memory Reasoning for Conversational Recommendation](https://arxiv.org/abs/2006.00184)
  - Publisher: `arXiv 2020`
  - Keywords: `Method` · `Recommendation` · `Social Memory & Adaptation` · `Interaction Management` · `Personalization` · `Retrieval` · `Supervised Learning`
- [RevCore- Review-augmented Conversational Recommendation](https://aclanthology.org/2021.findings-acl.104/)
  - Publisher: `ACL 2021`
  - Keywords: `Method` · `Recommendation` · `Affect` · `Retrieval` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/JD-AI-Research-NLP/RevCore)
  - Summary: [Summary](paper/Recommend-ACL-2021-RevCore-%20Review-augmented%20Conversational%20Recommendation.md)
- [Improving conversational recommendation systems via counterfactual data simulation](https://dl.acm.org/doi/10.1145/3580305.3599387)
  - Publisher: `KDD 2023`
  - Keywords: `Method` · `Recommendation` · `Mental-State Modeling` · `Interaction Management` · `Personalization` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/RUCAIBox/CFCRS)
  - Summary: [Summary](paper/Recommend-KDD-2023-Improving%20conversational%20recommendation%20systems%20via%20counterfactual%20data%20simulation.md)
- [Large Language Models as Zero-Shot Conversational Recommenders](https://doi.org/10.1145/3583780.3614949)
  - Publisher: `CIKM 2023`
  - Keywords: `Method` · `Recommendation` · `Social Perception` · `Personalization` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/AaronHeee/LLMs-as-Zero-Shot-Conversational-RecSys)
- [Rethinking the Evaluation for Conversational Recommendation in the Era of Large Language Models](https://aclanthology.org/2023.emnlp-main.621/)
  - Publisher: `EMNLP 2023`
  - Keywords: `Evaluation` · `Recommendation` · `Interaction Management` · `User Simulation` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/RUCAIBox/iEvaLM-CRS)
  - Summary: [Summary](paper/Recommend-EMNLP-2023-Rethinking%20the%20Evaluation%20for%20Conversational%20Recommendation%20in%20the%20Era%20of%20Large%20Language%20Models.md)
- [Beyond Persuasion: Towards Conversational Recommender System with Credible Explanations](https://aclanthology.org/2024.findings-emnlp.247)
  - Publisher: `EMNLP 2024`
  - Keywords: `Method` · `Recommendation` · `Social Context` · `Planning` · `Self-play`
  - Code: [GitHub / Project](https://github.com/mumen798/PC-CRS)
  - Summary: [Summary](paper/Recommend-EMNLP-2024-Beyond%20Persuasion:%20Towards%20Conversational%20Recommender%20System%20with%20Credible%20Explanations.md)
- [Broadening the View: Demonstration-augmented Prompt Learning for Conversational Recommendation](https://doi.org/10.1145/3626772.3657755)
  - Publisher: `SIGIR 2024`
  - Keywords: `Method` · `Recommendation` · `Social Context` · `Retrieval` · `Supervised Learning`
- [How Reliable is Your Simulator- Analysis on the Limitations of Current LLM-based User Simulators for Conversational Recommendation](https://doi.org/10.1145/3589335.3651955)
  - Publisher: `WWW 2024`
  - Keywords: `Evaluation` · `Recommendation` · `Interaction Management` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/RUCAIBox/iEvaLM-CRS/)
  - Summary: [Summary](paper/Recommend-WWW-2024-How%20Reliable%20is%20Your%20Simulator-%20Analysis%20on%20the%20Limitations%20of%20Current%20LLM-based%20User%20Simulators%20for%20Conversational%20Recommendation.md)
- [LLM-REDIAL: A Large-Scale Dataset for Conversational Recommender Systems Created from User Behaviors with LLMs](https://aclanthology.org/2024.findings-acl.529/)
  - Publisher: `ACL 2024`
  - Keywords: `Dataset` · `Recommendation` · `User Simulation` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/LitGreenhand/LLM-Redial)
  - Summary: [Summary](paper/Recommend-ACL-2024-LLM-REDIAL:%20A%20Large-Scale%20Dataset%20for%20Conversational%20Recommender%20Systems%20Created%20from%20User%20Behaviors%20with%20LLMs.md)
- [Mitigating Matthew Effect: Multi-Hypergraph Boosted Multi-Interest Self-Supervised Learning for Conversational Recommendation](https://aclanthology.org/2024.emnlp-main.86/)
  - Publisher: `EMNLP 2024`
  - Keywords: `Method` · `Recommendation` · `Social Memory & Adaptation` · `Self-play`
  - Code: [GitHub / Project](https://github.com/zysensmile/HiCore)
- [Pearl: A Review-driven Persona-Knowledge Grounded Conversational Recommendation Dataset](https://aclanthology.org/2024.findings-acl.65/)
  - Publisher: `ACL 2024`
  - Keywords: `Dataset` · `Recommendation` · `Personalization` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/kkmjkim/PEARL)
- [Reindex-Then-Adapt- Improving Large Language Models for Conversational Recommendation](https://arxiv.org/abs/2405.12119)
  - Publisher: `arXiv 2024`
  - Keywords: `Method` · `Recommendation` · `Interaction Management`
  - Summary: [Summary](paper/Recommend-arXiv-2024-Reindex-Then-Adapt-%20Improving%20Large%20Language%20Models%20for%20Conversational%20Recommendation.md)
- [A Causal-Based Attribute Selection Strategy for Conversational Recommender Systems](https://ieeexplore.ieee.org/abstract/document/10891447)
  - Publisher: `TKDE 2025`
  - Keywords: `Method` · `Recommendation` · `Social Context` · `Personalization` · `Planning`
  - Summary: [Summary](paper/Recommend-TKDE-2025-A%20Causal-Based%20Attribute%20Selection%20Strategy%20for%20Conversational%20Recommender%20Systems.md)
- [A Framework for Generating Conversational Recommendation Datasets from Behavioral Interactions](https://arxiv.org/abs/2506.17285)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `Recommendation` · `Interaction Management` · `Social Memory & Adaptation` · `Personalization` · `User Simulation` · `Planning` · `Multi-turn`
  - Summary: [Summary](paper/Recommend-arXiv-2025-A%20Framework%20for%20Generating%20Conversational%20Recommendation%20Datasets%20from%20Behavioral%20Interactions.md)
- [Bridging Conversational and Collaborative Signals for Conversational Recommendation](https://doi.org/10.1145/3701716.3715486)
  - Publisher: `WWW 2025`
  - Keywords: `Method` · `Recommendation`
  - Summary: [Summary](paper/Recommend-WWW-2025-Bridging%20Conversational%20and%20Collaborative%20Signals%20for%20Conversational%20Recommendation.md)
- [Collaborative Retrieval for Large Language Model-based Conversational Recommender Systems](https://dl.acm.org/doi/10.1145/3589334.3645347)
  - Publisher: `WWW 2025`
  - Keywords: `Method` · `Recommendation` · `Interaction Management` · `Personalization` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/yaochenzhu/CRAG)
  - Summary: [Summary](paper/Recommend-WWW-2025-Collaborative%20Retrieval%20for%20Large%20Language%20Model-based%20Conversational%20Recommender%20Systems.md)
- [Empowering Retrieval-based Conversational Recommendation with Contrasting User Preferences](https://aclanthology.org/2025.naacl-long.392/)
  - Publisher: `NAACL 2025`
  - Keywords: `Method` · `Recommendation` · `Affect` · `Mental-State Modeling` · `Supervised Learning` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/kookeej/CORAL)
- [LLM-based Conversational Recommendation Agents with Collaborative Verbalized Experience](https://aclanthology.org/2025.findings-emnlp.119/)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Recommendation` · `Social Memory & Adaptation` · `Personalization` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/yaochenzhu/CRAVE)
  - Summary: [Summary](paper/Recommend-EMNLP-2025-LLM-based%20Conversational%20Recommendation%20Agents%20with%20Collaborative%20Verbalized%20Experience.md)
- [MSCRS: Multi-modal Semantic Graph Prompt Learning Framework for Conversational Recommender Systems](https://arxiv.org/abs/2504.10921)
  - Publisher: `SIGIR 2025`
  - Keywords: `Method` · `Recommendation` · `Social Perception` · `Supervised Learning` · `Retrieval`
- [Towards Efficient Conversational Recommendations- Expected Value of Information Meets Bandit Learning](https://doi.org/10.1145/3696410.3714773)
  - Publisher: `WWW 2025`
  - Keywords: `Method` · `Recommendation` · `Interaction Management` · `RL` · `Multi-turn`
  - Summary: [Summary](paper/Recommend-WWW-2025-Towards%20Efficient%20Conversational%20Recommendations-%20Expected%20Value%20of%20Information%20Meets%20Bandit%20Learning.md)
- [Towards Personalized Conversational Sales Agents](https://arxiv.org/abs/2504.08754)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Influence` · `Social Context` · `Mental-State Modeling` · `Personalization` · `User Simulation`
  - Summary: [Summary](paper/Recommend-EMNLP-2025-Towards%20Personalized%20Conversational%20Sales%20Agents.md)
- [Not All Information Brings Benefits- Personalization-Driven Agent Debate for Conversational Recommendation](https://doi.org/10.1145/3774904.3792152)
  - Publisher: `WWW 2026`
  - Keywords: `Method` · `Recommendation` · `Social Memory & Adaptation` · `User Simulation`
  - Summary: [Summary](paper/Recommend-WWW-2026-Not%20All%20Information%20Brings%20Benefits-%20Personalization-Driven%20Agent%20Debate%20for%20Conversational%20Recommendation.md)
- [Optimizing Multi-Turn Interactive Recommendation Agents via Generative Intrinsic Motivation](https://doi.org/10.1145/3774904.3792209)
  - Publisher: `WWW 2026`
  - Keywords: `Method` · `Recommendation` · `Interaction Management` · `RL` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/XueyangFeng/GIMO)
  - Summary: [Summary](paper/Recommend-WWW-2026-Optimizing%20Multi-Turn%20Interactive%20Recommendation%20Agents%20via%20Generative%20Intrinsic%20Motivation.md)
- [Rank-GRPO: Training LLM-based Conversational Recommender Systems with Reinforcement Learning](https://arxiv.org/abs/2510.20150)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `Recommendation` · `Interaction Management` · `RL` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/yaochenzhu/Rank-GRPO)
- [User Simulator-Guided Multi-Turn Preference Optimization for Reasoning LLM-based Conversational Recommendation](https://arxiv.org/abs/2604.03671)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Recommendation` · `Mental-State Modeling` · `Social Memory & Adaptation` · `Personalization` · `User Simulation` · `Preference Optimization` · `RL` · `Supervised Learning` · `Reward Modeling` · `Multi-turn`
  - Summary: [Summary](paper/Recommend-arXiv-2026-User%20Simulator-Guided%20Multi-Turn%20Preference%20Optimization%20for%20Reasoning%20LLM-based%20Conversational%20Recommendation.md)
<!-- CATALOGUE:END -->



















</details>

<a id="coop"></a>
<details>
<summary>🤝 <b>Cooperation & Collaboration</b> · 12 papers</summary>

<!-- CATALOGUE:START -->
- [AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts](https://doi.org/10.1145/3491102.3517582)
  - Publisher: `CHI 2022`
  - Keywords: `System` · `General Interaction` · `Interaction Management`
- [Human-level play in the game of Diplomacy by combining language models with strategic reasoning](https://doi.org/10.1126/science.ade9097)
  - Publisher: `Science 2022`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Interaction Management` · `Multi-party` · `Planning` · `RL`
- [AI can help humans find common ground in democratic deliberation](https://doi.org/10.1126/science.adq2852)
  - Publisher: `Science 2024`
  - Keywords: `Method` · `Coordination` · `Social Context` · `Multi-party` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/google-deepmind/habermas_machine)
- [Building Cooperative Embodied Agents Modularly with Large Language Models](https://mlanthology.org/iclr/2024/zhang2024iclr-building/)
  - Publisher: `ICLR 2024`
  - Keywords: `Method` · `Coordination` · `Interaction Management` · `Embodied` · `Multi-party` · `Planning` · `Supervised Learning` · `Longitudinal`
- [Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents](https://arxiv.org/abs/2404.16698)
  - Publisher: `NeurIPS 2024`
  - Keywords: `Method` · `Coordination` · `Social Context` · `Mental-State Modeling` · `Multi-party` · `Planning`
  - Code: [GitHub / Project](https://github.com/giorgiopiatti/govsim)
- [Decision-Oriented Dialogue for Human-AI Collaboration](https://aclanthology.org/2024.tacl-1.50/)
  - Publisher: `TACL 2024`
  - Keywords: `Method` · `Coordination` · `Interaction Management` · `Multi-party` · `Self-play` · `User Simulation`
- [Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View](https://aclanthology.org/2024.acl-long.782/)
  - Publisher: `ACL 2024`
  - Keywords: `Method` · `Coordination` · `Social Perception` · `Multi-party`
  - Code: [GitHub / Project](https://github.com/zjunlp/MachineSoM)
- [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352)
  - Publisher: `ICLR 2024`
  - Keywords: `Method` · `Coordination` · `Interaction Management` · `Multi-party` · `Relationship & Role` · `Planning`
  - Code: [GitHub / Project](https://github.com/FoundationAgents/MetaGPT)
- [Should we be going MAD- A Look at Multi-Agent Debate Strategies for LLMs](https://arxiv.org/abs/2311.17371)
  - Publisher: `ICML 2024`
  - Keywords: `Evaluation` · `General Interaction` · `Interaction Management` · `Multi-party` · `Self-play`
  - Code: [GitHub / Project](https://github.com/instadeepai/DebateLLM)
- [Your Co-Workers Matter- Evaluating Collaborative Capabilities of Language Models in Blocks World](https://aclanthology.org/2024.findings-acl.294/)
  - Publisher: `ACL 2024`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Interaction Management` · `Multi-party` · `Planning`
- [LLM Strategic Reasoning: Agentic Study through Behavioral Game Theory](https://arxiv.org/abs/2502.20432)
  - Publisher: `NeurIPS 2025`
  - Keywords: `Evaluation` · `Coordination` · `Mental-State Modeling` · `Norms & Morality`
- [Playing repeated games with large language models](https://doi.org/10.1038/s41562-025-02172-y)
  - Publisher: `Nature Human Behaviour 2025`
  - Keywords: `Evaluation` · `Coordination` · `Social Context` · `Multi-party` · `Planning`
  - Code: [GitHub / Project](https://github.com/eliaka/repeatedgames)
<!-- CATALOGUE:END -->



















</details>

<a id="tom"></a>
<details>
<summary>💭 <b>Theory of Mind</b> · 26 papers</summary>

<!-- CATALOGUE:START -->
- [Bayesian Theory of Mind- Modeling Joint Belief-Desire Attribution](https://www.semanticscholar.org/paper/Explore-Theory-of-Mind:-Program-guided-adversarial-Sclar-Yu/3c52a1e1c3dc0ef5e1e638e11bbc3a2f09900dc6)
  - Publisher: `CogSci 2011`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling`
  - Summary: [Summary](paper/ToM-CogSci-2011-Bayesian%20Theory%20of%20Mind-%20Modeling%20Joint%20Belief-Desire%20Attribution.md)
- [Theory of Mind as Inverse Reinforcement Learning](https://doi.org/10.1016/j.cobeha.2019.04.010)
  - Publisher: `COBS 2019`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `RL`
  - Summary: [Summary](paper/ToM-COBS-2019-Theory-of-Mind-as-Inverse-Reinforcement-Learning.md)
- [MindCraft: Theory of Mind Modeling for Situated Dialogue in Collaborative Tasks](https://arxiv.org/abs/2109.06275)
  - Publisher: `arXiv 2021`
  - Keywords: `Dataset` · `Coordination` · `Mental-State Modeling` · `Social Context` · `Embodied` · `Multi-party` · `Supervised Learning`
- [Theory of Mind for Multi-Agent Collaboration via Large Language Models](https://arxiv.org/abs/2310.10701)
  - Publisher: `arXiv 2023`
  - Keywords: `Evaluation` · `Coordination` · `Mental-State Modeling` · `Social Perception` · `Multi-party` · `Planning` · `RL`
- [MindDial: Enhancing Conversational Agents with Theory-of-Mind for Common Ground Alignment and Negotiation](https://aclanthology.org/2024.sigdial-1.63/)
  - Publisher: `SIGDIAL 2024`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Social Context` · `Multi-party` · `Supervised Learning`
- [Think Twice: Perspective-Taking Improves Large Language Models' Theory-of-Mind Capabilities](https://aclanthology.org/2024.acl-long.451/)
  - Publisher: `ACL 2024`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Planning`
  - Code: [GitHub / Project](https://github.com/shawnsihyunlee/simulatedtom)
- [AutoToM- Scaling Model-based Mental Inference via Automated Agent Modeling](https://arxiv.org/abs/2502.15676)
  - Publisher: `NeurIPS 2025`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Perception` · `Embodied` · `Planning`
  - Summary: [Summary](paper/ToM-NeurIPS-2025-AutoToM-%20Scaling%20Model-based%20Mental%20Inference%20via%20Automated%20Agent%20Modeling.md)
- [Beyond Words: Integrating Theory of Mind into Conversational Agents for Human-Like Belief, Desire, and Intention Alignment](https://aclanthology.org/2025.findings-acl.287/)
  - Publisher: `Findings of ACL 2025`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Context` · `Supervised Learning`
- [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://arxiv.org/abs/2407.07086)
  - Publisher: `ICLR 2025`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Social Context` · `Social Memory & Adaptation` · `Multi-party` · `Planning` · `RL`
- [Machine Theory of Mind Needs Machine Validation](https://aclanthology.org/2025.findings-acl.951.pdf)
  - Publisher: `ACL 2025`
  - Keywords: `Evaluation` · `General Interaction` · `Mental-State Modeling`
  - Summary: [Summary](paper/ToM-ACL-2025-Machine%20Theory%20of%20Mind%20Needs%20Machine%20Validation.md)
- [MetaMind- Modeling Human Social Thoughts with Metacognitive Multi-Agent Systems](https://arxiv.org/abs/2505.18943)
  - Publisher: `NeurIPS 2025`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Context` · `Culture` · `Norms & Morality` · `Planning`
  - Code: [GitHub / Project](https://github.com/XMZhangAI/MetaMind)
  - Summary: [Summary](paper/ToM-NeurIPS-2025-MetaMind-%20Modeling%20Human%20Social%20Thoughts%20with%20Metacognitive%20Multi-Agent%20Systems.md)
- [MINDGAMES: Do Large Language Models Have a Planning Theory of Mind?](https://arxiv.org/pdf/2507.16196v1.pdf)
  - Publisher: `arXiv 2025`
  - Keywords: `Evaluation` · `Influence` · `Mental-State Modeling`
  - Code: [GitHub / Project](https://github.com/jlcmoore/mindgames)
  - Summary: [Summary](paper/ToM-arXiv-2025-MINDGAMES:%20Do%20Large%20Language%20Models%20Have%20a%20Planning%20Theory%20of%20Mind.md)
- [Modeling the Mental World for Embodied AI- A Comprehensive Review](https://arxiv.org/pdf/2601.02378)
  - Publisher: `arXiv 2025`
  - Keywords: `Survey` · `Coordination` · `Mental-State Modeling` · `Social Context` · `Embodied`
  - Summary: [Summary](paper/ToM-arXiv-2025-Modeling%20the%20Mental%20World%20for%20Embodied%20AI-%20A%20Comprehensive%20Review.md)
- [Overcoming Multi-step Complexity in Multimodal Theory-of-Mind Reasoning- A Scalable Bayesian Planner](https://arxiv.org/abs/2506.01301)
  - Publisher: `ICML 2025`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Planning`
  - Summary: [Summary](paper/ToM-ICML-2025-Overcoming%20Multi-step%20Complexity%20in%20Multimodal%20Theory-of-Mind%20Reasoning-%20A%20Scalable%20Bayesian%20Planner.md)
- [Theory of Mind in Large Language Models- Assessment and Enhancement](https://aclanthology.org/2025.acl-long.1522.pdf)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling`
  - Summary: [Summary](paper/ToM-ACL-2025-Theory%20of%20Mind%20in%20Large%20Language%20Models-%20Assessment%20and%20Enhancement.md)
- [ToM-agent: Large Language Models as Theory of Mind Aware Generative Agents with Counterfactual Reflection](https://arxiv.org/abs/2501.15355)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Memory & Adaptation` · `Planning`
  - Summary: [Summary](paper/ToM-arXiv-2025-ToM-agent-%20Large%20Language%20Models%20as%20Theory%20of%20Mind%20Aware%20Generative%20Agents%20with%20Counterfactual%20Reflection.md)
- [ToM-RL: Reinforcement Learning Unlocks Theory of Mind in Small LLMs](https://arxiv.org/abs/2504.01698)
  - Publisher: `arXiv 2025`
  - Keywords: `Evaluation` · `General Interaction` · `Mental-State Modeling` · `RL` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/bigai-ai/ToM-R)
  - Summary: [Summary](paper/ToM-arXiv-2025-ToM-RL-Reinforcement-Learning-Unlocks-Theory-of-Mind-in-Small-LLMs.md)
- [Infusing Theory of Mind into Socially Intelligent LLM Agents](https://arxiv.org/abs/2509.22887)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Memory & Adaptation` · `Relationship & Role` · `Planning` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/eujhwang/toma)
  - Summary: [Summary](paper/ToM-arXiv-2026-Infusing%20Theory%20of%20Mind%20into%20Socially%20Intelligent%20LLM%20Agents.md)
- [Let's Put Ourselves in Sally's Shoes: Shoes of Others Prefilling Improves Theory of Mind in LLMs](https://aclanthology.org/2026.findings-eacl.6/)
  - Publisher: `EACL 2026`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Planning`
  - Summary: [Summary](paper/ToM-EACL-2026-Lets-Put-Ourselves-in-Sallys-Shoes-Shoes-of-Others-Prefilling-Improves-Theory-of-Mind-in-LLMs.md)
- [Mental World Modeling](https://arxiv.org/abs/2607.27201)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Context`
- [MetaMind- General and Cognitive World Models in Multi-Agent Systems by Meta-Theory of Mind](https://arxiv.org/abs/2603.00808)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Social Context` · `Multi-party` · `Self-play`
  - Summary: [Summary](paper/ToM-arXiv-2026-MetaMind-%20General%20and%20Cognitive%20World%20Models%20in%20Multi-Agent%20Systems%20by%20Meta-Theory%20of%20Mind.md)
- [Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental States](https://arxiv.org/abs/2609.15972)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Support` · `Mental-State Modeling` · `Social Memory & Adaptation` · `Social Context` · `Personalization` · `User Simulation` · `Supervised Learning` · `Longitudinal`
- [MindClaw- Closed-Loop Embodied Mental-State Reasoning for Precision Intervention](https://arxiv.org/abs/2606.01063)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Support` · `Mental-State Modeling` · `Social Perception` · `Interaction Management` · `Embodied` · `Planning`
  - Summary: [Summary](paper/ToM-arXiv-2026-MindClaw-%20Closed-Loop%20Embodied%20Mental-State%20Reasoning%20for%20Precision%20Intervention.md)
- [Reality vs Counterfactual- Multi-World Contrastive Reinforcement Learning for Enhancing MLLM’s Theory of Mind in Egocentric Videos](https://ojs.aaai.org/index.php/AAAI/article/view/37162)
  - Publisher: `AAAI 2026`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Embodied`
  - Summary: [Summary](paper/ToM-AAAI-2026-Reality%20vs%20Counterfactual-%20Multi-World%20Contrastive%20Reinforcement%20Learning%20for%20Enhancing%20MLLM%E2%80%99s%20Theory%20of%20Mind%20in%20Egocentric%20Videos.md)
- [UserHarness- Harnessing User Minds for Stronger Agent Theory-of-Mind](https://arxiv.org/abs/2605.27721)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling`
  - Summary: [Summary](paper/ToM-arXiv-2026-UserHarness-%20Harnessing%20User%20Minds%20for%20Stronger%20Agent%20Theory-of-Mind.md)
- [Video-Only ToM- Enhancing Theory of Mind in Multimodal Large Language Models](https://arxiv.org/abs/2603.24484)
  - Publisher: `CVPR 2026`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Single-turn`
  - Code: [GitHub / Project](https://founce.github.io/VisionToM/)
  - Summary: [Summary](paper/ToM-CVPR-2026-Video-Only%20ToM-%20Enhancing%20Theory%20of%20Mind%20in%20Multimodal%20Large%20Language%20Models.md)
<!-- CATALOGUE:END -->



















</details>

<a id="emotion"></a>
<details>
<summary>🎭 <b>Affect & Social Perception</b> · 10 papers</summary>

<!-- CATALOGUE:START -->
- [DialogueRNN- An Attentive RNN for Emotion Detection in Conversations](https://ojs.aaai.org/index.php/AAAI/article/view/4657)
  - Publisher: `AAAI 2019`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Social Context` · `Supervised Learning`
- [MELD- A Multimodal Multi-Party Dataset for Emotion Recognition in Conversations](https://aclanthology.org/P19-1050/)
  - Publisher: `ACL 2019`
  - Keywords: `Dataset` · `General Interaction` · `Affect` · `Multi-party`
- [COSMIC- COmmonSense knowledge for eMotion Identification in Conversations](https://arxiv.org/abs/2010.02795)
  - Publisher: `AAAI 2021`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Context`
- [InstructERC- Reforming Emotion Recognition in Conversation with Multi-task Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2309.11911)
  - Publisher: `arXiv 2023`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Social Context` · `Relationship & Role` · `Retrieval` · `Supervised Learning`
- [Knowledge-Bridged Causal Interaction Network for Causal Emotion Entailment](https://ojs.aaai.org/index.php/AAAI/article/view/26641)
  - Publisher: `AAAI 2023`
  - Keywords: `Method` · `Support` · `Affect` · `Social Context` · `Relationship & Role` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/circle-hit/KBCIN)
- [EmoLLMs: A Series of Emotional Large Language Models and Annotation Tools for Comprehensive Affective Analysis](https://arxiv.org/abs/2401.08508)
  - Publisher: `KDD 2024`
  - Keywords: `Method` · `Support` · `Affect` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/lzw108/EmoLLMs)
- [Emotion-LLaMA: Multimodal Emotion Recognition and Reasoning with Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c7f43ada17acc234f568dc66da527418-Abstract-Conference.html)
  - Publisher: `NeurIPS 2024`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Social Perception` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/ZebangCheng/Emotion-LLaMA)
- [TelME: Teacher-leading Multimodal Fusion Network for Emotion Recognition in Conversation](https://aclanthology.org/2024.naacl-long.5/)
  - Publisher: `NAACL 2024`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Multi-party` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/yuntaeyang/TelME)
- [CoE: A Clue of Emotion Framework for Emotion Recognition in Conversations](https://aclanthology.org/2025.acl-long.1148/)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Social Context` · `Relationship & Role` · `Supervised Learning`
- [Do LLMs Feel- Teaching Emotion Recognition with Prompts, Retrieval, and Curriculum Learning](https://arxiv.org/abs/2511.07061)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Mental-State Modeling` · `Social Perception` · `Retrieval` · `Supervised Learning` · `Multi-turn`
<!-- CATALOGUE:END -->



















</details>

<a id="norms"></a>
<details>
<summary>⚖️ <b>Social Context, Norms & Morality</b> · 15 papers</summary>

<!-- CATALOGUE:START -->
- [Social Chemistry 101- Learning to Reason about Social and Moral Norms](https://aclanthology.org/2020.emnlp-main.48/)
  - Publisher: `EMNLP 2020`
  - Keywords: `Dataset` · `General Interaction` · `Social Context` · `Norms & Morality` · `Supervised Learning`
- [Aligning AI With Shared Human Values](https://arxiv.org/abs/2008.02275)
  - Publisher: `ICLR 2021`
  - Keywords: `Dataset` · `General Interaction` · `Mental-State Modeling` · `Norms & Morality`
  - Code: [GitHub / Project](https://github.com/hendrycks/ethics)
- [Delphi- Towards Machine Ethics and Norms](https://arxiv.org/abs/2110.07574)
  - Publisher: `arXiv 2021`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Norms & Morality` · `Supervised Learning`
- [The Moral Integrity Corpus- A Benchmark for Ethical Dialogue Systems](https://arxiv.org/abs/2204.03021)
  - Publisher: `ACL 2022`
  - Keywords: `Dataset` · `General Interaction` · `Social Context` · `Norms & Morality` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/SALT-NLP/mic)
- [When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment](https://arxiv.org/abs/2210.01478)
  - Publisher: `NeurIPS 2022`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Context` · `Norms & Morality` · `Planning`
  - Code: [GitHub / Project](https://github.com/feradauto/MoralCoT)
- [Do the Rewards Justify the Means- Measuring Trade-Offs Between Rewards and Ethical Behavior in the MACHIAVELLI Benchmark](https://arxiv.org/abs/2304.03279)
  - Publisher: `ICML 2023`
  - Keywords: `Evaluation` · `General Interaction` · `Norms & Morality`
- [Evaluating the Moral Beliefs Encoded in LLMs](https://arxiv.org/abs/2307.14324)
  - Publisher: `NeurIPS 2023`
  - Keywords: `Evaluation` · `General Interaction` · `Mental-State Modeling` · `Norms & Morality`
  - Code: [GitHub / Project](https://github.com/ninodimontalcino/moralchoice)
- [NormBank- A Knowledge Bank of Situational Social Norms](https://arxiv.org/abs/2305.17008)
  - Publisher: `ACL 2023`
  - Keywords: `Dataset` · `General Interaction` · `Social Context` · `Relationship & Role` · `Culture` · `Norms & Morality`
  - Code: [GitHub / Project](https://github.com/SALT-NLP/normbank)
- [CultureBank- An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies](https://arxiv.org/abs/2404.15238)
  - Publisher: `arXiv 2024`
  - Keywords: `Dataset` · `General Interaction` · `Social Context` · `Culture` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/SALT-NLP/CultureBank)
- [Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties](https://arxiv.org/abs/2309.00779)
  - Publisher: `AAAI 2024`
  - Keywords: `Dataset` · `General Interaction` · `Social Context` · `Mental-State Modeling` · `Norms & Morality` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/tsor13/kaleido)
- [Emergent social conventions and collective bias in LLM populations](https://doi.org/10.1126/sciadv.adu9368)
  - Publisher: `Science Advances 2025`
  - Keywords: `Method` · `Coordination` · `Social Context` · `Multi-party` · `Self-play`
  - Code: [GitHub / Project](https://github.com/Ariel-Flint-Ashery/AI-norms)
- [Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?](https://aclanthology.org/2025.emnlp-main.154/)
  - Publisher: `EMNLP 2025`
  - Keywords: `Evaluation` · `General Interaction` · `Social Context` · `Culture`
- [Multiple LLM Agents Debate for Equitable Cultural Alignment](https://aclanthology.org/2025.acl-long.1210/)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `General Interaction` · `Social Context` · `Culture` · `Norms & Morality` · `Self-play`
  - Code: [GitHub / Project](https://github.com/dayeonki/cultural_debate)
- [NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models](https://aclanthology.org/2025.naacl-long.120/)
  - Publisher: `NAACL 2025`
  - Keywords: `Evaluation` · `General Interaction` · `Social Context` · `Culture` · `Norms & Morality`
  - Code: [GitHub / Project](https://github.com/Akhila-Yerukola/NormAd)
- [The Discordance Between Embedded Ethics and Cultural Inference in Large Language Models](https://aclanthology.org/2025.emnlp-main.743/)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `General Interaction` · `Social Context` · `Mental-State Modeling` · `Culture` · `Norms & Morality` · `Supervised Learning`
<!-- CATALOGUE:END -->



















</details>

<a id="memory"></a>
<details>
<summary>💾 <b>Social Memory & Adaptation</b> · 14 papers</summary>

<!-- CATALOGUE:START -->
- [Generative Agents- Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763)
  - Publisher: `UIST 2023`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Interaction Management` · `Multi-party` · `Planning`
  - Code: [GitHub / Project](https://github.com/joonspk-research/generative_agents)
  - Summary: [Summary](paper/Memory-UIST-2023-Generative%20Agents-%20Interactive%20Simulacra%20of%20Human%20Behavior.md)
- [MemoryBank- Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)
  - Publisher: `arXiv 2023`
  - Keywords: `Method` · `Support` · `Social Memory & Adaptation` · `Affect` · `Personalization` · `Retrieval` · `Longitudinal`
  - Code: [GitHub / Project](https://github.com/zhongwanjun/memorybank-siliconfriend)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
  - Publisher: `NeurIPS 2023`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `RL`
  - Code: [GitHub / Project](https://github.com/noahshinn/reflexion)
- [ExpeL: LLM Agents Are Experiential Learners](https://ojs.aaai.org/index.php/AAAI/article/view/29936)
  - Publisher: `AAAI 2024`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/LeapLabTHU/ExpeL)
- [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831)
  - Publisher: `NeurIPS 2024`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/OSU-NLP-Group/HippoRAG)
- [A-Mem: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Retrieval` · `Longitudinal`
  - Code: [GitHub / Project](https://github.com/WujiangXu/AgenticMemory)
  - Summary: [Summary](paper/Memory-arXiv-2025-A-Mem:%20Agentic%20Memory%20for%20LLM%20Agents.md)
- [Evo-Memory- Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](https://arxiv.org/abs/2511.20857)
  - Publisher: `arXiv 2025`
  - Keywords: `Benchmark` · `General Interaction` · `Social Memory & Adaptation`
  - Code: [GitHub / Project](https://github.com/WujiangXu/AgenticMemory)
  - Summary: [Summary](paper/Memory-arXiv-2025-Evo-Memory-%20Benchmarking%20LLM%20Agent%20Test-time%20Learning%20with%20Self-Evolving%20Memory.md)
- [Hello again! LLM-powered personalized agent for long-term dialogue](https://aclanthology.org/2025.naacl-long.272/)
  - Publisher: `NAACL 2025`
  - Keywords: `Method` · `Support` · `Social Memory & Adaptation` · `Social Perception` · `Mental-State Modeling` · `Personalization` · `Retrieval` · `Longitudinal`
- [Human-inspired Episodic Memory for Infinite Context LLMs](https://arxiv.org/abs/2407.09450)
  - Publisher: `ICLR 2025`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/em-llm/EM-LLM-model)
- [In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Interaction Management` · `Personalization` · `RL` · `Retrieval` · `Longitudinal`
- [Remember Me, Refine Me- A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://arxiv.org/abs/2512.10696)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Retrieval`
  - Code: [GitHub / Project](https://github.com/agentscope-ai/ReMe)
  - Summary: [Summary](paper/Memory-arXiv-2025-Remember%20Me%2C%20Refine%20Me-%20A%20Dynamic%20Procedural%20Memory%20Framework%20for%20Experience-Driven%20Agent%20Evolution.md)
- [SHARE: Shared memory-aware open-domain long-term dialogue dataset constructed from movie script](https://aclanthology.org/2025.acl-long.704/)
  - Publisher: `ACL 2025`
  - Keywords: `Dataset` · `General Interaction` · `Social Memory & Adaptation` · `Relationship & Role` · `Longitudinal`
- [MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `RL`
  - Summary: [Summary](paper/Memory-ICLR-2026-MemAgent:%20Reshaping%20Long-Context%20LLM%20with%20Multi-Conv%20RL-based%20Memory%20Agent.md)
- [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://proceedings.iclr.cc/paper_files/paper/2026/hash/980ea04d23d1f6908964eba2a74afe45-Abstract-Conference.html)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Self-play`
  - Code: [GitHub / Project](https://github.com/google-research/reasoning-bank)
  - Summary: [Summary](paper/Memory-ICLR-2026-ReasoningBank:%20Scaling%20Agent%20Self-Evolving%20with%20Reasoning%20Memory.md)
<!-- CATALOGUE:END -->



















</details>

<a id="rlhf"></a>
<details>
<summary>🤖 <b>Learning, Planning & Alignment</b> · 24 papers</summary>

<!-- CATALOGUE:START -->
- [Deep Dyna-Q: Integrating Planning for Task-Completion Dialogue Policy Learning](https://arxiv.org/abs/1801.06176)
  - Publisher: `arXiv 2018`
  - Keywords: `Method` · `Coordination` · `Interaction Management` · `RL` · `Planning` · `User Simulation`
- [The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games](https://arxiv.org/abs/2103.01955)
  - Publisher: `NeurIPS 2022`
  - Keywords: `Method` · `Coordination` · `Multi-party` · `RL`
  - Code: [GitHub / Project](https://github.com/marlbenchmark/on-policy)
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
  - Publisher: `NeurIPS 2022`
  - Keywords: `Method` · `General Interaction` · `Supervised Learning` · `RL` · `Reward Modeling`
- [Direct Preference Optimization- Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)
  - Publisher: `NeurIPS 2023`
  - Keywords: `Method` · `General Interaction` · `Preference Optimization`
  - Summary: [Summary](paper/RLHF-NeurIPS-2023-Direct%20Preference%20Optimization-%20Your%20Language%20Model%20is%20Secretly%20a%20Reward%20Model.md)
- [Prompt-Based Monte-Carlo Tree Search for Goal-oriented Dialogue Policy Planning](https://arxiv.org/abs/2305.13660)
  - Publisher: `arXiv 2023`
  - Keywords: `Method` · `Influence` · `Interaction Management` · `Planning` · `User Simulation`
- [ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL](https://arxiv.org/abs/2402.19446)
  - Publisher: `ICML 2024`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `RL` · `Planning` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/YifeiZhou02/ArCHer)
- [KTO: Model Alignment as Prospect Theoretic Optimization](https://arxiv.org/abs/2402.01306)
  - Publisher: `ICML 2024`
  - Keywords: `Method` · `General Interaction` · `Affect` · `Preference Optimization`
  - Code: [GitHub / Project](https://github.com/ContextualAI/HALOs)
- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)
  - Publisher: `ICLR 2024`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `Reward Modeling` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/openai/prm800k)
- [RLAIF vs. RLHF- Scaling Reinforcement Learning from Human Feedback with AI Feed](https://arxiv.org/abs/2309.00267v3)
  - Publisher: `ICML 2024`
  - Keywords: `Method` · `General Interaction` · `RL` · `Reward Modeling` · `Supervised Learning`
  - Summary: [Summary](paper/RLHF-ICML-2024-RLAIF%20vs.%20RLHF-%20Scaling%20Reinforcement%20Learning%20from%20Human%20Feedback%20with%20AI%20Feed.md)
- [DCPO- Dynamic Clipping Policy Optimization](https://arxiv.org/abs/2509.02333v2)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `RL`
  - Code: [GitHub / Project](https://github.com/lime-RL/DCPO)
  - Summary: [Summary](paper/RLHF-arXiv-2025-DCPO-%20Dynamic%20Clipping%20Policy%20Optimization.md)
- [Dream to Chat: Model-based Reinforcement Learning on Dialogues with User Belief Modeling](https://arxiv.org/abs/2508.16876)
  - Publisher: `EMNLP 2025`
  - Keywords: `Method` · `Support` · `Mental-State Modeling` · `Affect` · `RL` · `User Simulation`
  - Summary: [Summary](paper/RLHF-EMNLP-2025-Dream%20to%20Chat:%20Model-based%20Reinforcement%20Learning%20on%20Dialogues%20with%20User%20Belief%20Modeling.md)
- [Enhancing User Engagement in Socially-Driven Dialogue through Interactive LLM Alignments](https://arxiv.org/abs/2506.21497v1)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `Support` · `Interaction Management` · `Relationship & Role` · `Planning` · `Preference Optimization`
  - Summary: [Summary](paper/RLHF-arXiv-2025-Enhancing-User-Engagement-in-Socially-Driven-Dialogue-through-Interactive-LLM-Alignments.md)
- [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071v2)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `RL`
  - Summary: [Summary](paper/RLHF-arXiv-2025-Group%20Sequence%20Policy%20Optimization.md)
- [MAPO: Mixed Advantage Policy Optimization for Long-Horizon Multi-Turn Dialogue](https://arxiv.org/pdf/2603.06194)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `RL` · `Reward Modeling` · `Multi-turn`
  - Summary: [Summary](paper/RLHF-arXiv-2025-MAPO:%20Mixed%20Advantage%20Policy%20Optimization%20for%20Long-Horizon%20Multi-Turn%20Dialogue.md)
- [MCA-Model-Based Causal RL for Efficient Dialogue Policy](https://aclanthology.org/2025.coling-main.490/)
  - Publisher: `COLING 2025`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `Social Context` · `RL` · `Planning`
  - Summary: [Summary](paper/RLHF-COLING-2025-MCA-Model-Based-Causal-RL-for-Efficient-Dialogue-Policy.md)
- [Moral Alignment for LLM Agents](https://arxiv.org/abs/2410.01639)
  - Publisher: `ICLR 2025`
  - Keywords: `Method` · `General Interaction` · `Social Context` · `Norms & Morality` · `RL` · `Reward Modeling`
  - Code: [GitHub / Project](https://github.com/liza-tennant/LLM_morality)
- [Training Turn-by-Turn Verifiers for Dialogue Tutoring Agents: The Curious Case of LLMs as Your Coding Tutors](https://arxiv.org/abs/2502.13311)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `Support` · `Mental-State Modeling` · `Personalization` · `User Simulation`
- [VinePPO: Refining Credit Assignment in RL Training of LLMs](https://arxiv.org/abs/2410.01679)
  - Publisher: `ICML 2025`
  - Keywords: `Method` · `General Interaction` · `RL`
  - Code: [GitHub / Project](https://github.com/McGill-NLP/VinePPO)
- [World Models Should Prioritize the Unification of Physical and Social Dynamics](https://arxiv.org/pdf/2510.21219/)
  - Publisher: `NeurIPS 2025`
  - Keywords: `Method` · `General Interaction` · `Social Context`
  - Summary: [Summary](paper/RLHF-NeurIPS-2025-World-Models-Should-Prioritize-the-Unification-of-Physical-and-Social-Dynamics.md)
- [Better LLM Reasoning via Dual-Play](https://arxiv.org/abs/2511.11881v3)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `Self-play`
  - Code: [GitHub / Project](https://hcy123902.github.io/PasoDoble/)
  - Summary: [Summary](paper/RLHF-arXiv-2026-Better%20LLM%20Reasoning%20via%20Dual-Play.md)
- [Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student Dialogues](https://arxiv.org/abs/2605.01097)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Support` · `Mental-State Modeling` · `Social Context` · `Relationship & Role` · `Supervised Learning`
- [Planning-Guided Tutoring with Assessment-Driven Memory for Pedagogical LLM Tutors](https://aclanthology.org/2026.acl-long.325/)
  - Publisher: `ACL 2026`
  - Keywords: `Method` · `Support` · `Mental-State Modeling` · `Interaction Management` · `Social Memory & Adaptation` · `Planning` · `Multi-turn`
- [Toward Evaluative Thinking: Meta-Policy Optimization with Evolving Reward Models](https://arxiv.org/pdf/2504.20157)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `General Interaction` · `Reward Modeling`
  - Summary: [Summary](paper/RLHF-ICLR-2026-Toward-Evaluative-Thinking-Meta-Policy-Optimization-with-Evolving-Reward-Models.md)
- [TreeSearch for LLM Agent Reinforcement Learning](https://arxiv.org/abs/2509.21240)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `RL` · `Planning` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/AMAP-ML/Tree-GRPO)
  - Summary: [Summary](paper/RLHF-ICLR-2026-TreeSearch%20for%20LLM%20Agent%20Reinforcement%20Learning.md)
<!-- CATALOGUE:END -->



















</details>

<a id="us"></a>
<details>
<summary>🕹️ <b>User Simulation & Interactive Environments</b> · 37 papers</summary>

<!-- CATALOGUE:START -->
- [A Survey of Statistical User Simulation Techniques for RL Dialogue Management](https://doi.org/10.1017/S0269888906000944)
  - Publisher: `KER 2006`
  - Keywords: `Survey` · `General Interaction` · `User Simulation` · `RL`
  - Summary: [Summary](paper/US-KER-2006-A-Survey-of-Statistical-User-Simulation-Techniques-for-RL-Dialogue-Management.md)
- [Neural User Simulation for Corpus-based Policy Optimisation of Spoken Dialogue Systems](https://arxiv.org/abs/1805.06966)
  - Publisher: `arXiv 2018`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `User Simulation` · `RL`
- [Domain-independent User Simulation with Transformers for Task-oriented Dialogue Systems](https://arxiv.org/abs/2106.08838)
  - Publisher: `arXiv 2021`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `User Simulation` · `RL`
- [Transferable Dialogue Systems and User Simulators](https://arxiv.org/abs/2107.11904)
  - Publisher: `arXiv 2021`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `Self-play` · `RL` · `User Simulation`
- [GenTUS: Simulating User Behaviour and Language in Task-oriented Dialogues with Generative Transformers](https://arxiv.org/abs/2208.10817)
  - Publisher: `arXiv 2022`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `User Simulation` · `RL`
- [Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](https://arxiv.org/abs/2208.10264)
  - Publisher: `arXiv 2022`
  - Keywords: `Evaluation` · `General Interaction` · `Social Perception` · `User Simulation`
- [Metaphorical User Simulators for Evaluating Task-oriented Dialogue Systems](https://doi.org/10.1145/3596510)
  - Publisher: `TOIS 2023`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `User Simulation`
  - Code: [GitHub / Project](http://github.com/sunnweiwei/MetaSim)
  - Summary: [Summary](paper/US-TOIS-2023-Metaphorical%20User%20Simulators%20for%20Evaluating%20Task-oriented%20Dialogue%20Systems.md)
- [Adversarial Socialbots Modeling Based on Structural Information Principles](https://ojs.aaai.org/index.php/AAAI/article/view/27793)
  - Publisher: `AAAI 2024`
  - Keywords: `Method` · `Influence` · `Social Context` · `Multi-party` · `Planning`
  - Code: [GitHub / Project](https://github.com/SELGroup/SIASM)
  - Summary: [Summary](paper/US-AAAI-2024-Adversarial%20Socialbots%20Modeling%20Based%20on%20Structural%20Information%20Principles.md)
- [An In-depth Investigation of User Response Simulation for Conversational Search](https://dl.acm.org/doi/10.1145/3589334.3645447)
  - Publisher: `WWW 2024`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `User Simulation`
  - Code: [GitHub / Project](https://anonymous.4open.science/r/UserSimulation-7091)
  - Summary: [Summary](paper/US-WWW-2024-An%20In-depth%20Investigation%20of%20User%20Response%20Simulation%20for%20Conversational%20Search.md)
- [Enhancing Dialogue State Tracking Models through LLM-backed User-Agents Simulation](https://arxiv.org/abs/2405.13037)
  - Publisher: `arXiv 2024`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `User Simulation` · `Supervised Learning`
- [Evaluating Large Language Models as Generative User Simulators for Conversational Recommendation](https://arxiv.org/abs/2403.09738)
  - Publisher: `arXiv 2024`
  - Keywords: `Evaluation` · `Recommendation` · `Social Perception` · `User Simulation`
- [LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals](https://arxiv.org/abs/2411.10109)
  - Publisher: `arXiv 2024`
  - Keywords: `Method` · `General Interaction` · `Social Context` · `Personalization` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/StanfordHCI/genagents)
- [OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://arxiv.org/abs/2411.11581)
  - Publisher: `arXiv 2024`
  - Keywords: `System` · `General Interaction` · `Social Perception` · `Multi-party` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/camel-ai/oasis)
- [PlatoLM: Teaching LLMs in Multi-Round Dialogue via a User Simulator](https://aclanthology.org/2024.acl-long.424/)
  - Publisher: `ACL 2024`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `User Simulation` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/FreedomIntelligence/PlatoLM)
- [SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://arxiv.org/abs/2310.11667)
  - Publisher: `ICLR 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Social Perception` · `Relationship & Role` · `User Simulation`
  - Code: [GitHub / Project](https://sotopia.world)
  - Summary: [Summary](paper/US-ICLR-2024-SOTOPIA-%20Interactive%20Evaluation%20for%20Social%20Intelligence%20in%20Language%20Agents.md)
- [Strength Lies in Differences! Improving Strategy Planning for Non-collaborative Dialogues via Diversified User Simulation](https://arxiv.org/pdf/2403.06769v3.pdf)
  - Publisher: `arXiv 2024`
  - Keywords: `Method` · `Influence` · `Social Context` · `Social Memory & Adaptation` · `Personalization` · `User Simulation` · `Self-play`
  - Summary: [Summary](paper/US-arXiv-2024-Strength%20Lies%20in%20Differences%21%20Improving%20Strategy%20Planning%20for%20Non-collaborative%20Dialogues%20via%20Diversified%20User%20Simulation.md)
- [A LLM-based Controllable, Scalable, Human-Involved User Simulator Framework for Conversational Recommender Systems](https://doi.org/10.1145/3696410.3714858)
  - Publisher: `WWW 2025`
  - Keywords: `Method` · `Recommendation` · `Social Memory & Adaptation` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/zlxxlz1026/CSHI)
  - Summary: [Summary](paper/US-WWW-2025-A%20LLM-based%20Controllable%2C%20Scalable%2C%20Human-Involved%20User%20Simulator%20Framework%20for%20Conversational%20Recommender%20Systems.md)
- [Consistent Client Simulation for Motivational Interviewing-based Counseling](https://arxiv.org/abs/2502.02802)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `Support` · `Mental-State Modeling` · `Social Memory & Adaptation` · `Relationship & Role` · `User Simulation`
- [Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents](https://arxiv.org/abs/2505.19997)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Planning`
- [Foundations of PEERS: Assessing LLM Role Performance in Educational Simulations](https://aclanthology.org/2025.acl-srw.66/)
  - Publisher: `ACL SRW 2025`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `Relationship & Role` · `User Simulation`
- [Generating Diverse Personas for User Simulators to Test Interview Dialogue Systems](https://aclanthology.org/2025.sigdial-1.54/)
  - Publisher: `SIGDIAL 2025`
  - Keywords: `Method` · `General Interaction` · `Social Perception` · `Personalization` · `User Simulation`
  - Summary: [Summary](paper/US-SIGDIAL-2025-Generating%20Diverse%20Personas%20for%20User%20Simulators%20to%20Test%20Interview%20Dialogue%20Systems.md)
- [Goal Alignment in LLM-Based User Simulators for Conversational AI](https://arxiv.org/abs/2507.20152)
  - Publisher: `NeurIPS 2025`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `User Simulation` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/Shuhaibm/user_simulator_goal_alignment)
  - Summary: [Summary](paper/US-NeurIPS-2025-Goal%20Alignment%20in%20LLM-Based%20User%20Simulators%20for%20Conversational%20AI.md)
- [Know You First and Be You Better: Modeling Human-Like User Simulators via Implicit Profiles](https://aclanthology.org/2025.acl-long.1025/)
  - Publisher: `ACL 2025`
  - Keywords: `Method` · `General Interaction` · `Social Memory & Adaptation` · `Mental-State Modeling` · `Personalization` · `Supervised Learning` · `RL` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/wangkevin02/USP)
- [Preference Tree with Look-Ahead: Training Goal-Oriented Dialogue with Virtual Patient](https://openreview.net/forum?id=fTVhWlzCuk)
  - Publisher: `ICLR 2025`
  - Keywords: `Method` · `Support` · `Affect` · `Interaction Management` · `Personalization` · `Planning` · `Preference Optimization` · `User Simulation` · `Multi-turn`
- [Simulating Before Planning- Constructing Intrinsic User World Model for User-Tailored Dialogue Policy Planning](https://doi.org/10.1145/3726302.3730084)
  - Publisher: `SIGIR 2025`
  - Keywords: `Method` · `General Interaction` · `Social Context` · `Personalization` · `Planning`
  - Summary: [Summary](paper/US-SIGIR-2025-Simulating%20Before%20Planning-%20Constructing%20Intrinsic%20User%20World%20Model%20for%20User-Tailored%20Dialogue%20Policy%20Planning.md)
- [Stop Playing the Guessing Game! Evaluating Conversational Recommender Systems via Target-free User Simulation](https://aclanthology.org/2025.findings-emnlp.1067/)
  - Publisher: `Findings of EMNLP 2025`
  - Keywords: `Evaluation` · `Recommendation` · `Interaction Management` · `User Simulation` · `Multi-turn`
- [Theory and Toolkits for User Simulation in the Era of Generative AI- User Modeling, Synthetic Data Generation, and System Evaluation](https://doi.org/10.1145/3726302.3731697)
  - Publisher: `SIGIR 2025`
  - Keywords: `Survey` · `General Interaction` · `User Simulation`
  - Summary: [Summary](paper/US-SIGIR-2025-Theory%20and%20Toolkits%20for%20User%20Simulation%20in%20the%20Era%20of%20Generative%20AI-%20User%20Modeling%2C%20Synthetic%20Data%20Generation%2C%20and%20System%20Evaluation.md)
- [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045)
  - Publisher: `ICLR 2025`
  - Keywords: `Benchmark` · `General Interaction` · `Interaction Management` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/sierra-research/tau-bench)
- [A Survey on LLM-based Conversational User Simulation](https://arxiv.org/abs/2604.24977)
  - Publisher: `arXiv 2026`
  - Keywords: `Survey` · `General Interaction`
- [Flipping the Dialogue: Training and Evaluating User Language Models](https://arxiv.org/abs/2510.06552)
  - Publisher: `ICLR 2026`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `User Simulation` · `Supervised Learning` · `Multi-turn`
  - Code: [GitHub / Project](https://huggingface.co/microsoft/UserLM-8b)
- [From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents](https://doi.org/10.1145/3800683)
  - Publisher: `CSUR 2026`
  - Keywords: `Survey` · `General Interaction` · `Social Context` · `Multi-party`
  - Code: [GitHub / Project](https://github.com/FudanDISC/SocialAgent)
- [HumanLLM: Towards Personalized Understanding and Simulation of Human Nature](https://arxiv.org/abs/2601.15793)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Memory & Adaptation` · `Personalization` · `Supervised Learning`
- [HumanLM: Simulating Users with State Alignment Beats Response Imitation](https://arxiv.org/abs/2603.03303)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Social Context` · `Personalization` · `RL`
- [SEAD: Self-Evolving Agent for Multi-Turn Service Dialogue](https://arxiv.org/abs/2602.03548)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Coordination` · `Interaction Management` · `Mental-State Modeling` · `Personalization` · `User Simulation` · `Self-play`
- [Simulated Customers Never Walk Away: Decision Fidelity of LLM User Simulators Measured Against Real Purchase Outcomes](https://arxiv.org/abs/2606.20708)
  - Publisher: `arXiv 2026`
  - Keywords: `Evaluation` · `Influence` · `Mental-State Modeling` · `Personalization` · `User Simulation`
- [Small Agents, Big Gains: Journey-Aware and Critic-Guided Simulation for Long-Horizon Shopping Dialogues](https://aclanthology.org/2026.acl-industry.39/)
  - Publisher: `ACL Industry 2026`
  - Keywords: `Method` · `General Interaction` · `Interaction Management` · `Social Memory & Adaptation` · `Personalization` · `User Simulation` · `Reward Modeling`
- [UserLM-R1: Modeling Human Reasoning in User Language Models with Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2601.09215)
  - Publisher: `arXiv 2026`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Social Context` · `Relationship & Role` · `RL` · `Supervised Learning`
<!-- CATALOGUE:END -->



















</details>

<a id="data"></a>
<details>
<summary>📊 <b>Benchmark & Evaluation</b> · 42 papers</summary>

<!-- CATALOGUE:START -->
- [Social-IQ- A Question Answering Benchmark for Artificial Social Intelligence](https://openaccess.thecvf.com/content_CVPR_2019/html/Zadeh_Social-IQ_A_Question_Answering_Benchmark_for_Artificial_Social_Intelligence_CVPR_2019_paper.html)
  - Publisher: `CVPR 2019`
  - Keywords: `Benchmark` · `General Interaction` · `Social Perception`
- [FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions](https://aclanthology.org/2023.emnlp-main.890/)
  - Publisher: `EMNLP 2023`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling` · `Multi-party` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/skywalker023/fantom)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
  - Publisher: `NeurIPS 2023`
  - Keywords: `Evaluation` · `General Interaction`
  - Code: [GitHub / Project](https://github.com/lm-sys/FastChat)
- [Social-IQ 2.0 Challenge- Benchmarking Multimodal Social Understanding](https://cmu-multicomp-lab.github.io/social-iq-2.0/)
  - Publisher: `ICCV 2023`
  - Keywords: `Benchmark` · `General Interaction` · `Social Perception`
  - Code: [GitHub / Project](https://github.com/abwilf/Social-IQ-2.0-Challenge)
- [Understanding Social Reasoning in Language Models with Language Models](https://arxiv.org/abs/2306.15448)
  - Publisher: `NeurIPS 2023`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/cicl-stanford/procedural-evals-tom)
- [Agent-as-a-Judge- Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934)
  - Publisher: `ICML 2024`
  - Keywords: `Method` · `General Interaction`
  - Code: [GitHub / Project](https://github.com/metauto-ai/agent-as-a-judge)
  - Summary: [Summary](paper/Data-ICML-2024-Agent-as-a-Judge-%20Evaluate%20Agents%20with%20Agents.md)
- [Evaluating Intention Detection Capability of Large Language Models in Persuasive Dialogues](https://aclanthology.org/2024.acl-long.90.pdf)
  - Publisher: `ACL 2024`
  - Keywords: `Evaluation` · `Influence` · `Mental-State Modeling` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/Syuko4omi/LLM_intention_detection_public)
  - Summary: [Summary](paper/Data-ACL-2024-Evaluating%20Intention%20Detection%20Capability%20of%20Large%20Language%20Models%20in%20Persuasive%20Dialogues.md)
- [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/)
  - Publisher: `ACL 2024`
  - Keywords: `Dataset` · `General Interaction` · `Social Memory & Adaptation` · `Multi-party` · `Retrieval` · `Longitudinal`
  - Code: [GitHub / Project](https://github.com/snap-research/locomo)
- [MM-SOC: Benchmarking Multimodal Large Language Models in Social Media Platforms](https://aclanthology.org/2024.findings-acl.370/)
  - Publisher: `ACL 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Social Perception` · `Multi-party` · `Supervised Learning`
  - Code: [GitHub / Project](https://github.com/claws-lab/MMSoc)
- [MMToM-QA: Multimodal Theory of Mind Question Answering](https://aclanthology.org/2024.acl-long.851/)
  - Publisher: `ACL 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling` · `Planning`
  - Code: [GitHub / Project](https://github.com/chuanyangjin/MMToM-QA)
- [OpenToM: A Comprehensive Benchmark for Evaluating Theory-of-Mind Reasoning Capabilities of Large Language Models](https://aclanthology.org/2024.acl-long.466/)
  - Publisher: `ACL 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling`
  - Code: [GitHub / Project](https://github.com/seacowx/OpenToM)
- [SimpleToM: Exposing the Gap between Explicit ToM Inference and Implicit ToM Application in LLMs](https://arxiv.org/abs/2410.13648)
  - Publisher: `arXiv 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling` · `Social Perception` · `Relationship & Role`
- [SocialBench: Sociality Evaluation of Role-Playing Conversational Agents](https://aclanthology.org/2024.findings-acl.125/)
  - Publisher: `ACL 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Social Perception` · `Relationship & Role` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/X-PLUG/SocialBench)
- [ToMBench: Benchmarking Theory of Mind in Large Language Models](https://aclanthology.org/2024.acl-long.847/)
  - Publisher: `ACL 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling`
  - Code: [GitHub / Project](https://github.com/zhchen18/ToMBench)
- [Who is ChatGPT? Benchmarking LLMs' Psychological Portrayal Using PsychoBench](https://arxiv.org/abs/2310.01386)
  - Publisher: `ICLR 2024`
  - Keywords: `Benchmark` · `General Interaction` · `Affect` · `Mental-State Modeling` · `Relationship & Role` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/CUHK-ARISE/PsychoBench)
- [Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLM Communication](https://aclanthology.org/2025.naacl-main.287/)
  - Publisher: `NAACL 2025`
  - Keywords: `Method` · `Influence` · `Interaction Management` · `Multi-party` · `Norms & Morality` · `User Simulation`
  - Code: [GitHub / Project](https://github.com/HF-heaven/LLM-based_persuasion_simulator)
  - Summary: [Summary](paper/Data-NAACL-2025-Communication%20Makes%20Perfect:%20Persuasion%20Dataset%20Construction%20via%20Multi-LLM%20Communication.md)
- DICE-BENCH- Evaluating the Tool-Use Capabilities of Large Language Models in Multi-Round, Multi-Party Dialogues
  - Publisher: `ACL 2025`
  - Keywords: `Benchmark` · `Coordination` · `Interaction Management` · `Multi-party` · `User Simulation` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/snuhcc/DICE-Bench)
- [EducationQ: Evaluating LLMs' Teaching Capabilities Through Multi-Agent Dialogue Framework](https://arxiv.org/abs/2504.14928)
  - Publisher: `arXiv 2025`
  - Keywords: `Method` · `Support` · `Interaction Management` · `Social Perception` · `Relationship & Role` · `User Simulation`
- [Explore theory of mind: program-guided adversarial data generation for theory of mind reasoning](https://arxiv.org/abs/2412.12175)
  - Publisher: `ICLR 2025`
  - Keywords: `Method` · `General Interaction` · `Mental-State Modeling` · `Planning`
  - Code: [GitHub / Project](https://github.com/facebookresearch/exploretom)
  - Summary: [Summary](paper/Data-ICLR-2025-Explore%20Theory%20of%20Mind-%20PROGRAM-GUIDED%20ADVERSARIAL%20DATA%20GENERATION%20FOR%20THEORY%20OF%20MIND%20REASONING.md)
- [In Search of the Lost Arch in Dialogue- A Dependency Dialogue Acts Corpus for Multi-Party Dialogues](https://aclanthology.org/2025.findings-acl.1032/)
  - Publisher: `ACL 2025`
  - Keywords: `Dataset` · `General Interaction` · `Interaction Management` · `Social Perception` · `Multi-party` · `Supervised Learning`
- [LLMs and their Limited Theory of Mind: Evaluating Mental State Annotations in Situated Dialogue](https://arxiv.org/abs/2509.02292)
  - Publisher: `arXiv 2025`
  - Keywords: `Evaluation` · `Coordination` · `Mental-State Modeling` · `Multi-party` · `Supervised Learning`
- [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)
  - Publisher: `ICLR 2025`
  - Keywords: `Benchmark` · `General Interaction` · `Social Memory & Adaptation` · `Interaction Management` · `Personalization` · `Retrieval` · `Longitudinal`
  - Code: [GitHub / Project](https://github.com/xiaowu0162/LongMemEval)
- [MOMENT S- A Comprehensive Multimodal Benchmark for Theory of Mind](https://aclanthology.org/2025.findings-emnlp.1230.pdf)
  - Publisher: `EMNLP 2025`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling` · `Social Perception` · `Multi-party`
  - Code: [GitHub / Project](https://github.com/villacu/MoMentS)
  - Summary: [Summary](paper/Data-EMNLP-2025-MOMENT%20S-%20A%20Comprehensive%20Multimodal%20Benchmark%20for%20Theory%20of%20Mind.md)
- [MuMA-ToM- Multi-modal Multi-Agent Theory of Mind](https://arxiv.org/abs/2408.12574)
  - Publisher: `AAAI 2025`
  - Keywords: `Method` · `Coordination` · `Mental-State Modeling` · `Social Context` · `Multi-party` · `Embodied`
  - Code: [GitHub / Project](https://scai.cs.jhu.edu/projects/MuMA-ToM/)
  - Summary: [Summary](paper/Data-AAAI-2025-MuMA-ToM-%20Multi-modal%20Multi-Agent%20Theory%20of%20Mind.md)
- [PersonaGym: Evaluating Persona Agents and LLMs](https://arxiv.org/abs/2407.18416)
  - Publisher: `EMNLP 2025`
  - Keywords: `Evaluation` · `General Interaction` · `Social Context` · `Personalization`
  - Code: [GitHub / Project](https://github.com/vsamuel2003/PersonaGym)
- [SocialEval: Evaluating Social Intelligence of Large Language Models](https://aclanthology.org/2025.acl-long.1496/)
  - Publisher: `ACL 2025`
  - Keywords: `Benchmark` · `General Interaction` · `Social Perception` · `Mental-State Modeling`
  - Code: [GitHub / Project](https://github.com/thu-coai/SocialEval)
- [ToM-SSI: Evaluating Theory of Mind in Situated Social Interactions](https://arxiv.org/abs/2509.05066)
  - Publisher: `arXiv 2025`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling` · `Social Perception` · `Multi-party` · `Embodied`
- [ToMATO: Verbalizing the Mental States of Role-Playing LLMs for Benchmarking Theory of Mind](https://arxiv.org/abs/2501.08838)
  - Publisher: `AAAI 2025`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling` · `Relationship & Role`
  - Code: [GitHub / Project](https://github.com/nttmdlab-nlp/ToMATO)
  - Summary: [Summary](paper/Data-AAAI-2025-ToMATO-%20Verbalizing%20the%20Mental%20States%20of%20Role-Playing%20LLMs%20for%20Benchmarking%20Theory%20of%20Mind.md)
- [Towards Dynamic Theory of Mind- Evaluating LLM Adaptation to Temporal Evolution of Human States](https://arxiv.org/abs/2505.17663)
  - Publisher: `ACL 2025`
  - Keywords: `Evaluation` · `General Interaction` · `Mental-State Modeling` · `Multi-party` · `Multi-turn`
  - Code: [GitHub / Project](https://github.com/GAIR-NLP/DynToM)
  - Summary: [Summary](paper/Data-ACL-2025-Towards%20Dynamic%20Theory%20of%20Mind-%20Evaluating%20LLM%20Adaptation%20to%20Temporal%20Evolution%20of%20Human%20States.md)
- [WHoW- A Cross-domain Approach for Analysing Conversation Moderation](https://aclanthology.org/2025.naacl-long.105/)
  - Publisher: `NAACL 2025`
  - Keywords: `Evaluation` · `Coordination` · `Interaction Management` · `Multi-party`
- [You need to MIMIC to get FAME- Solving Meeting Transcript Scarcity with Multi-Agent Conversations](https://arxiv.org/abs/2502.13001)
  - Publisher: `arXiv 2025`
  - Keywords: `Dataset` · `General Interaction` · `Social Context` · `Social Perception` · `Multi-party` · `Relationship & Role` · `User Simulation`
- [Beyond Fixed Psychological Personas: State Beats Trait, but Language Models are State-Blind](https://arxiv.org/abs/2601.15395)
  - Publisher: `arXiv 2026`
  - Keywords: `Dataset` · `General Interaction` · `Affect` · `Personalization` · `Reward Modeling`
- [DialToM: A Theory of Mind Benchmark for Forecasting State-Driven Dialogue Trajectories](https://arxiv.org/abs/2604.20443)
  - Publisher: `arXiv 2026`
  - Keywords: `Benchmark` · `General Interaction` · `Mental-State Modeling` · `Social Context` · `Supervised Learning`
- [Does Theory of Mind Improvement Really Benefit Human-AI Interactions? Empirical Findings from Interactive Evaluations](https://arxiv.org/abs/2605.15205)
  - Publisher: `arXiv 2026`
  - Keywords: `Evaluation` · `General Interaction` · `Mental-State Modeling`
- [EnactToM- An Evolving Benchmark for Functional Theory of Mind in Embodied Agents](https://arxiv.org/abs/2605.09826)
  - Publisher: `arXiv 2026`
  - Keywords: `Benchmark` · `Coordination` · `Mental-State Modeling` · `Social Perception` · `Embodied` · `Multi-party`
  - Code: [GitHub / Project](https://enact-tom.github.io/)
  - Summary: [Summary](paper/Data-arXiv-2026-EnactToM-%20An%20Evolving%20Benchmark%20for%20Functional%20Theory%20of%20Mind%20in%20Embodied%20Agents.md)
- [ES-MemEval- Benchmarking Conversational Agents on Personalized Long-Term Emotional Support](https://doi.org/10.1145/3774904.3792143)
  - Publisher: `WWW 2026`
  - Keywords: `Benchmark` · `Support` · `Social Memory & Adaptation` · `Mental-State Modeling` · `Personalization` · `Longitudinal`
  - Code: [GitHub / Project](https://github.com/slptongji/ES-MemEval)
  - Summary: [Summary](paper/Data-WWW-2026-ES-MemEval-%20Benchmarking%20Conversational%20Agents%20on%20Personalized%20Long-Term%20Emotional%20Support.md)
- [Large language model psychometrics- A systematic review of evaluation, validation, and enhancement](https://arxiv.org/abs/2505.08245)
  - Publisher: `arXiv 2026`
  - Keywords: `Survey` · `General Interaction`
  - Code: [GitHub / Project](https://github.com/valuebyte-ai/Awesome-LLM-Psychometrics)
  - Summary: [Summary](paper/Data-arXiv-2026-Large%20language%20model%20psychometrics-%20A%20systematic%20review%20of%20evaluation%2C%20validation%2C%20and%20enhancement.md)
- [MME-Emotion: A Holistic Evaluation Benchmark for Emotional Intelligence in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/50d277e84b2bcbaadcd84548a87e8cc4-Abstract-Conference.html)
  - Publisher: `ICLR 2026`
  - Keywords: `Benchmark` · `General Interaction` · `Affect` · `Social Perception` · `Multi-party`
  - Code: [GitHub / Project](https://github.com/QwenAudio/MME-Emotion)
- [PIVOTSBench- Evaluating Fine-Grained Interpersonal Relationship Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2606.23092)
  - Publisher: `arXiv 2026`
  - Keywords: `Benchmark` · `General Interaction` · `Social Perception` · `Social Context` · `Relationship & Role`
- [RecToM: A Benchmark for Evaluating Machine Theory of Mind in LLM-based Conversational Recommender Systems](https://arxiv.org/abs/2511.22275)
  - Publisher: `AAAI 2026`
  - Keywords: `Benchmark` · `Recommendation` · `Mental-State Modeling` · `Social Context` · `Personalization`
  - Code: [GitHub / Project](https://github.com/CGCL-codes/RecToM)
  - Summary: [Summary](paper/Data-AAAI-2026-RecToM-%20A%20Benchmark%20for%20Evaluating%20Machine%20Theory%20of%20Mind%20in%20LLM-based%20Conversational%20Recommender%20Systems.md)
- [Simulated Students in Tutoring Dialogues: Substance or Illusion?](https://arxiv.org/abs/2601.04025)
  - Publisher: `arXiv 2026`
  - Keywords: `Evaluation` · `Support` · `Mental-State Modeling` · `Relationship & Role` · `Supervised Learning` · `Preference Optimization`
- [TIDES- A Longitudinal Bilingual Dataset for Modeling Multi-Party Social Dynamics](https://arxiv.org/abs/2608.01724)
  - Publisher: `arXiv 2026`
  - Keywords: `Dataset` · `Coordination` · `Social Context` · `Interaction Management` · `Multi-party` · `Relationship & Role` · `Supervised Learning` · `Longitudinal`
<!-- CATALOGUE:END -->



















</details>

---

<a id="keywords"></a>
## 🏷️ Keyword System

Keywords are assigned along facets, so paper type, research goal, social capability, social context, and method are not conflated into one layer:

| Facet | Single-choice | Purpose |
| --- | --- | --- |
| `Type` | Yes | Whether the main contribution is a system, method, dataset, benchmark, evaluation, or survey. |
| `Goal` | Yes | The main social interaction goal, such as influence, support, recommendation, or coordination. |
| `Capability` | No | Social capabilities involved, such as affect, mental-state modeling, social context, or social memory. |
| `Context` | No | Settings such as personalization, relationships & roles, norms & culture, multi-party, or embodied. |
| `Approach` | No | Key technical routes, such as planning, RL, preference optimization, or user simulation. |
| `Horizon` | Yes | Single-turn, multi-turn, or cross-session / long-term interaction. |

See [metadata/KEYWORDS.md](metadata/KEYWORDS.md) for the full vocabulary, boundary definitions, evidence requirements, and review policy. The repository now generates a cross-browsable keyword index from the metadata.

---

<a id="repo-structure"></a>
## 📁 Repository Structure

```
Awesome-Social-AI/
├── image/              # Images and figures for papers
├── paper/              # Chinese paper summaries (filename prefix is the primary section, not the full labels)
├── metadata/           # Controlled keyword vocabulary and structured paper metadata
├── scripts/            # README sync, metadata validation, and other tools
├── Example.md          # Paper summary template
├── README.md           # This document (English)
└── README_CN.md        # This document (简体中文)
```

---

<a id="contributing"></a>
## ✍️ How to Contribute

Contributions are welcome! The flow is simple: fork this repository → create a branch → add papers following the conventions below → open a PR for review.

### Naming conventions

- Name files under `paper/` strictly as `[Section]-[Venue]-[Year]-[Full paper title].md`, e.g. `Memory-NeurIPS-2023-Retrieval-Augmented-Generation.md`
- The filename prefix is the paper's **primary section** — pick the closest of the 11 existing prefixes; it does not replace the keywords. Discuss in the group before adding a new prefix. Current prefixes: PD, ED, Recommend, Coop, ToM, Emotion, Norms, Memory, RLHF, US, Data
- Name files under `image/` as `[Year]-[Month]-[Day]-[Number]-[Initials].png`, e.g. `2024010101mmh.png`

### Adding content

1. Write the Chinese summary following the [Example.md](Example.md) template
2. Add a structured record in `metadata/papers.json`: `type`, `goal`, `horizon` are single-choice; capabilities, contexts, and approaches are multi-choice. All label values must come from the [keyword vocabulary](metadata/KEYWORDS.md); add paper evidence for every multi-choice label
3. Validate and rebuild the catalogue before committing:

```bash
python scripts/validate_metadata.py --paper-dir paper
python scripts/render_readme_catalog.py
```

You can also use [Auto-Summary](https://github.com/lucianma05-create/Auto-Summary) to draft summaries, then proofread them manually.

---

<a id="about"></a>
## 🧠 About Us

Maintained by the NWPU Crowd-HMT-Lab Social-AI-Group.
