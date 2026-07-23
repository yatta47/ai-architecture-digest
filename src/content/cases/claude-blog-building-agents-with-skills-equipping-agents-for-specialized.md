---
type: guidance
title: Agent Skillsによるドメイン知識のパッケージ化とエージェントの専門特化
title_original: 'Building agents with Skills: Equipping agents for specialized work'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Claude Code
- Claude Agent SDK
- MCP
- Agent Skills
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
published_at: '2026-01-22'
---

## 概要

AnthropicはClaude Codeやエージェント開発の実務を通じて、専用エージェントを個別に作るのではなく『Agent Skills』としてドメイン知識をファイル群にパッケージ化し、汎用エージェントに後付けで専門性を与える設計に転換した。Skillsはprogressive disclosure(段階的開示)によりメタデータ・SKILL.md本体・参照資料の3層でコンテキスト消費を抑えつつ、数百のスキルを1つのエージェントに搭載可能にする。

## 設計のポイント

- 専用エージェントを個別に構築するのではなく、コード実行可能な汎用エージェントにSkillsとしてドメイン知識を後付けする
- progressive disclosure(メタデータ→SKILL.md→referencesの3層)でコンテキストウィンドウを圧迫せずに大量のスキルを保持する
- 繰り返し書かれるスクリプトをSkill内のツールとして保存し、自己文書化されたコードとして再利用する
- 基盤スキル・パートナースキル・エンタープライズスキルに分けて、汎用/外部連携/組織固有ノウハウをそれぞれ管理する

## 使いどころ

- 組織固有のブランドガイドラインや業務手順をエージェントに繰り返し教え込む代わりに一度スキル化したい場合
- エンジニア以外(PM・アナリスト等)がGitやGoogle Driveでバージョン管理しながら業務knowledgeをエージェントに提供したい場合
- 多数の専門領域をカバーする必要があるが、コンテキストウィンドウの圧迫を避けたいエージェント設計者
