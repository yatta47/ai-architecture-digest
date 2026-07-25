---
type: guidance
title: 'エージェントにSkillsとMCPどちらを使うべきか: LlamaAgents Builder開発での実体験比較'
title_original: 'Skills vs. MCP Tools for Agents: When to Use What'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- MCP
- LlamaAgents Builder
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what
published_at: '2026-07-19'
---

## 概要

MCPは外部サービス呼び出しとして予測可能・正確に実行できる一方、ツール数のスケーリングやレイテンシに難があり、Skillsはローカルで高速だが自然言語指示ゆえの解釈揺れ・幻覚リスクがあるとし、両者の実行モデルの違いを整理する。LlamaAgents Builderの開発では、ドキュメントMCPだけでエージェントが十分に正しいコードパターンを生成でき、Skillsを併用しても大きな改善は見られなかったという実体験を共有している。

## 設計のポイント

- MCPはツールを実行するかどうかだけをエージェントが判断すればよいのに対し、Skillsは『どのスキルを、いつ、どう使うか』まで自然言語解釈に委ねる必要があると整理した
- スキルはネットワーク呼び出しを伴わずローカルで完結するため低レイテンシだが、決定論的な実行保証はMCPに劣る
- 実際の開発では、豊富なドキュメントを提供するMCPだけで十分なケースがあり、Skillsを常に追加するのが最適とは限らないと実験で確認した

## 使いどころ

- 外部APIへの正確で予測可能な呼び出しが必要な処理にはMCPを選びたい設計判断
- セットアップコストを抑えつつ自然言語でエージェントの振る舞いを素早くカスタマイズしたい場合
