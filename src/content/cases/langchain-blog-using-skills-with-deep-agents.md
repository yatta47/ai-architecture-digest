---
type: announcement
title: Deep Agents CLIにAnthropicのAgent Skillsサポートを追加
title_original: Using skills with Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- deepagents-CLI
- Claude Code
- Agent Skills
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/using-skills-with-deep-agents
published_at: '2026-08-25'
---

## 概要

LangChainはオープンソースのコーディングエージェントdeepagents-CLIに、Anthropicが提唱するAgent Skillsのサポートを追加した。Claude CodeやManusのような汎用エージェントが少数のbash/ファイルシステムツールで多様な操作をこなせているのと同じ発想で、動的に読み込まれるSKILL.mdフォルダ群を使い、ツール定義を事前にすべてコンテキストへ積む代わりに必要な分だけ段階的に開示する。

## 設計のポイント

- 汎用エージェントは専用バウンドツールを多数持つ代わりに、bash＋ファイルシステムという少数のツールと、動的読み込み可能なスキルフォルダの組み合わせで多様な操作をこなす
- スキルはYAMLフロントマターだけを常時ロードし、本文（SKILL.md）はエージェントが必要と判断したときだけ読み込む段階的開示（progressive disclosure）でコンテキスト消費を抑える
- 多数の類似・重複したツール定義から選ばせるより、少数の原子的ツール＋スキルの構成の方が認知負荷が下がり、スキルはエージェント間・セッション間で共有・合成しやすい

## 使いどころ

- 幅広いが同時には使わない機能群を、ツール定義でコンテキストを圧迫せずにエージェントへ持たせたいコーディング/運用エージェントの開発チーム
- 公開されているAgent Skillsの資産を、Claude Code以外の自前のエージェントハーネスでも再利用したいチーム
