---
type: guidance
title: 並列エージェントで複数モダリティのデータを高信頼度に分類するアーキテクチャ
title_original: 'Agentic AI use case: Classify multimodal data'
industry: cross-industry
cloud:
- gcp
patterns:
- multi-agent-orchestration
- video-intelligence
- parallel-execution
components:
- Cloud Run
- Gemini Enterprise Agent Platform
- Gemini
- BigQuery
- Cloud Storage
- Google Cloud MCP servers
- Model Context Protocol (MCP)
- Agent Development Kit (ADK)
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-classify-multimodal-data
published_at: '2026-07-19'
---

## 概要

Google Cloudは、画像・動画・構造化データなど異種のマルチモーダルデータを複数の専門サブエージェントが並列に分析し、多数決や信頼度スコアで単一の高信頼度な分類結果を導く並列エージェントパターンのアーキテクチャを示す。医療診断や不正検知、品質管理などへの応用例を挙げる。

## 設計のポイント

- ルートエージェントがbefore_agent_callbackで環境設定や入力検証を行い、共有セッション状態に保存することで全サブエージェントの重複呼び出しとレイテンシを削減する
- 画像・動画・構造化データそれぞれに専門のサブエージェントを割り当て、独立して並列に分類と信頼度スコアを算出させる
- サブエージェントの分類結果が多数決で一致すればそのまま採用し、一致しない場合は最も信頼度が高い分類を採用するというシンプルな集約ルールを設ける
- 単一の巨大エージェントより専門化された複数エージェントの方が、指示の衝突を避けツールセットを絞り込めるため高速かつ堅牢な判断ができる

## 使いどころ

- 医療画像・症状・検査結果を独立分析し診断の確度を高めたい医療機関
- 領収書や請求書の視覚情報と取引データを突き合わせて不正を検知したい金融機関
- 外観検査・センサーデータ・仕様確認を組み合わせて製品の合否判定をしたい製造業
