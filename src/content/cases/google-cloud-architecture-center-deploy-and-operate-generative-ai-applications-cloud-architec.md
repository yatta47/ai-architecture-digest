---
type: guidance
title: 基盤モデル時代のDevOps/MLOpsをどう作り変えるか——生成AIアプリケーションのライフサイクル運用論
title_original: Deploy and operate generative AI applications
industry: cross-industry
cloud:
- gcp
patterns:
- llmops
- prompt-optimization
- fine-tuning
components: []
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/deploy-operate-generative-ai-applications
published_at: '2026-07-19'
---

## 概要

予測AI向けのDevOps/MLOpsのプラクティスを、基盤モデル（LLM）を使った生成AIアプリケーション向けに適応させる方法論。発見・開発実験・デプロイ・本番監視・継続改善という生成AIアプリのライフサイクルと、プロンプトテンプレートやチェーン定義など新たに管理が必要な成果物を整理する。

## 設計のポイント

- 基盤モデル選定では品質・レイテンシ/スループット・開発運用コスト・利用コスト・コンプライアンスの5軸で評価する
- プロンプトテンプレート・チェーン定義・埋め込みモデル・検索データストア・ファインチューニング済みアダプタなど生成AI特有の成果物をガバナンス対象として管理する
- 継続的改善はモデルの再学習だけでなく、プロンプト調整・モデル差し替え・複数モデルの組み合わせも手段として位置付ける

## 使いどころ

- 既存のMLOps体制を持つ組織が、予測AIから生成AI（基盤モデル）運用へプロセスを拡張する際の指針として
- プロンプト・チェーン・アダプタなど生成AI特有の成果物管理をこれから設計するAIプラットフォームチーム
