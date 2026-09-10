---
type: guidance
title: LLMベースのモデル非依存PII検出器
title_original: Model-agnostic PII detection with LLMs
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- context-engineering
- llmops
components:
- Amazon Bedrock
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/model-agnostic-pii-detection-with-llms/
published_at: '2026-09-10'
---

## 概要

個人情報（PII）の検出ロジックをモデルの再学習ではなくプロンプト（指示）に持たせることで、Amazon Bedrock上の任意のLLMやセルフホスト型モデルに切り替え可能なPII検出器を構築する。9種のLLMベース検出器と5つの公開PIIコーパスで評価し、OpenAI PrivacyFilterとも比較した。

## 設計のポイント

- 検出対象エンティティと出力フォーマットをプロンプトに定義し、新しい項目の追加は一行の編集で済むようにする
- 推論バックエンドを『メッセージを渡すと文字列が返る』統一インターフェースにして、マネージドAPIと自社GPUホストの両方に対応する
- モデルはオフセット（文字位置）を返せないため、返ってきた値をテキスト中から正規表現で再特定する後処理層を用意する
- LLMが出しがちな類似ラベル（DATE→DATES等）をエイリアス表で正規化しつつ、対応不能なものはUNKとして可視化する

## 使いどころ

- 問い合わせログやHR記録など、固定スキーマでは捉えきれない自由記述にPIIが混在するデータのクレンジング
- 自社ファインチューニング用コーパスから、業界固有の識別子（社員IDなど）も含めてPIIを機械的に洗い出したい場合
