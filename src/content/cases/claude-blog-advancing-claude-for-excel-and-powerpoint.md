---
type: announcement
title: Excel・PowerPoint間でコンテキストを共有するClaudeアドインとSkills機能
title_original: Advancing Claude for Excel and PowerPoint
company: Anthropic
industry: financial-services
cloud:
- aws
- gcp
- azure
patterns:
- ai-agent
- context-engineering
components:
- Claude for Excel
- Claude for PowerPoint
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-excel-powerpoint-updates
published_at: '2026-03-11'
---

## 概要

Claude for ExcelとPowerPointが会話コンテキストを共有し、開いているファイルをまたいで一貫した作業ができるようになった。財務モデルの監査やコンプス分析などの定型ワークフローを「Skills」として保存し、ワンクリックで再実行できる。

## 設計のポイント

- ExcelとPowerPointの会話コンテキストをアプリ間で共有し、都度データセットを説明し直す手間をなくす
- 頻出ワークフロー（モデル監査・LBO/DCF構築・コンプス分析）をSkillsとして事前定義し、ワンクリックの定型アクション化する
- Bedrock/Vertex AI/Foundry経由のLLMゲートウェイをサポートし、既存のコンプライアンス体制のままアドインを配布できる

## 使いどころ

- 財務アナリストが複数ワークブックとピッチデックをまたいで比較分析・資料作成を行う場面
- 組織単位で標準化したい定型分析・レビュー手順をチーム全体に配布したい場合
