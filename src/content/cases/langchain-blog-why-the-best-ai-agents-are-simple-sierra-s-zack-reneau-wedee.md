---
type: case
title: Sierraのマルチモデル運用とモノリシック設計に学ぶ、シンプルなエージェント戦略
title_original: Why the best agents are simpler than you think
company: Sierra
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- ai-agent
- voice-agent
- context-engineering
components:
- Claude
- Gemini
- GPT
- LangGraph
- LangSmith
- Model Context Protocol (MCP)
outcome:
  type: revenue
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/why-the-best-agents-are-simpler-than-you-think-sierra-max-agency-podcast
published_at: '2026-06-25'
---

## 概要

顧客対応向け会話型AIプラットフォームのSierraが、複数モデルの並列運用やブランド単位の単一エージェント設計、成果報酬型の価格モデルなど、実運用で得た設計哲学をポッドキャストで語った記事。マルチエージェントへの分割は「組織図をそのまま出荷する」ことになりがちだとし、コンテキストを丸ごと持つモノリシックなエージェント設計を選好している。

## 設計のポイント

- 単一プロバイダに固定せず、タスクごとに最も精度の高いモデルを実測で選び、文字起こしなど用途別に複数モデルを並列運用する。
- チーム構造に合わせてエージェントを機能分割すると、各エージェントが部分的な文脈しか持てなくなるため、ブランド単位で全コンテキストを保持する単一エージェントを採用する。
- 音声エージェントは「聞く・考える・話す」を並列に処理するモジュラーアーキテクチャで自然な応答とレイテンシ低減を両立させる。
- 成果の価値が高いタスクには成果報酬型、コモディティ的なタスクには従量/シート課金を使い分けて価格モデルとインセンティブを一致させる。

## 使いどころ

- 複数チームがそれぞれ別エージェントを担当する体制を検討しているが、顧客体験の分断を避けたいプロダクトチーム。
- サポートだけでなく閲覧・予約・販売・ロイヤルティまで顧客ライフサイクル全体をカバーするエージェントを設計したいチーム。
- 複数のAIプロバイダを併用し、タスク特性に応じて文字起こしや推論のモデルを最適配分したい基盤エンジニアリングチーム。
- 音声応答の自然さと低レイテンシを両立させたいコンタクトセンター・音声エージェント開発チーム。
