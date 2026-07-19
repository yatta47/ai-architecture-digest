---
type: announcement
title: 低ハルシネーションの推論モデルGrok 4.3をBedrockのエージェント基盤に統合
title_original: Introducing Grok on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
- multi-model-routing
components:
- Amazon Bedrock
- Grok 4.3
- Mantle
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-grok-on-amazon-bedrock/
published_at: '2026-07-16'
---

## 概要

xAIのGrok 4.3がAmazon Bedrockで一般提供となり、新しい推論エンジンMantle上でOpenAI互換APIを通じて利用できるようになった。リクエスト単位で推論の深さ（none/low/medium/high）を切り替えられる設定可能な推論強度と100万トークンのコンテキストウィンドウにより、契約書レビューや与信分析など長文書を扱うエージェントワークロードに向く設計になっている。

## 設計のポイント

- 推論エフォートをリクエスト単位で制御できるようにし、分類のような低レイテンシタスクと深い分析タスクを同一モデルで使い分けられるようにする。
- ステートフルなResponses APIでは前ターンの推論トレースをサービス側が自動保持し、ステートレスにしたい場合は暗号化された推論コンテンツを明示的に往復させる選択肢を用意する。
- 本番用途には有効期限付きの短期ベアラートークンをIAM資格情報から生成する認証方式を推奨し、長期APIキーは検証用途に限定する。

## 使いどころ

- 契約書レビューや与信契約分析など、長文書に対する高精度な推論とツール呼び出しを組み合わせたいエージェント開発チーム。
- 推論コストとレイテンシをタスクごとに調整したい高頻度推論ワークロード。
- 既存のOpenAI SDKベースの実装をそのままBedrock上のモデルに向けたいチーム。
