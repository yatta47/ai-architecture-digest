---
type: case
title: Salesforce Agentforceを支える統合AI実行エンジン「Unified Planner」の設計
title_original: 'Inside Unified Planner: The AI Brain Behind Agentforce'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- unified-runtime
- parallel-execution
- multi-model-routing
- voice-agent
components:
- Agentforce
- Unified Planner
- Agent Graph
- Voice Planner
- MuleSoft
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/inside-unified-planner-the-ai-brain-behind-agentforce/
published_at: '2026-06-29'
---

## 概要

Salesforceは、音声・チャット・テキストなど全てのAgentforce体験を横断する単一のAI実行・推論エンジン「Unified Planner」を開発した。従来は低遅延重視のVoice Plannerと推論・オーケストレーション重視のAgent Graphが別々に進化し、機能重複や体験の不一致を生んでいたが、プラットフォーム管理の処理と顧客定義のビジネスロジックを分離した上で多くの処理を並列実行に再設計し、応答時間を約20秒から約2.3秒へと短縮した。

## 設計のポイント

- プロンプトインジェクション検知や割り込み処理などプラットフォーム管理の処理と、顧客が定義するビジネスワークフローを明確に分離し、各システムの専門性を保ったまま基盤を統合した。
- プロンプトインジェクション検知・引用生成・グラウンディング検証・ナレッジ検索といった従来は逐次実行だった処理を並列実行に再設計し、レイテンシを大幅に削減した。
- 顧客が定義するツール呼び出しについても依存関係がない限り並列実行できるよう設定可能にし、基盤側だけでなくワークフロー全体の遅延も改善した。
- 特定用途向けの軽量な内部分類器を活用しつつ、開発者が要件に応じてモデルを選べるようにすることで、レイテンシと推論品質を両立させた。

## 使いどころ

- 音声・チャット・テキストなど複数のインタラクションモードを持つAIエージェントプラットフォームを単一のランタイムで支えたい場合。
- 音声のような即応性が求められる場面と、複雑な推論が必要なエンタープライズワークフローを同じ基盤上で両立させたいケース。
- 別々に進化してきた複数の実行エンジンを、重複や体験の不一致を解消しながら統合したいプラットフォームチーム。
- 自社サービスだけでなく別製品（例: MuleSoft）にも同じ実行基盤を提供し、拡張性を保ったまま機能を共通化したい場合。
