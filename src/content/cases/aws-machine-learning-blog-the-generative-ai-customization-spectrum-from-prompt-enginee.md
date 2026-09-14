---
type: guidance
title: 生成AIカスタマイズ手法を8段階で選ぶ意思決定フレームワーク
title_original: 'The generative AI customization spectrum: From prompt engineering to custom models on AWS'
industry: cross-industry
cloud:
- aws
patterns:
- prompt-optimization
- rag
- fine-tuning
- llmops
components:
- Amazon Bedrock
- Amazon SageMaker
- Amazon Nova Forge
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/the-generative-ai-customization-spectrum-from-prompt-engineering-to-custom-models-on-aws/
published_at: '2026-09-14'
---

## 概要

AWSは生成AIのカスタマイズ手法を「そのまま使う」「プロンプトエンジニアリング」「RAG/キャッシュ/蒸留」「ファインチューニング/継続事前学習/独自モデル構築」の3カテゴリ8段階に整理した意思決定フレームワークを公開した。過剰投資（不要なファインチューニング）と過小投資（本来必要な学習データ投入をせず延々プロンプト調整）の両方のコストを避けるため、最も単純な段階から始めて精度・レイテンシ・ドメイン要件が満たせない場合のみ次段階へ進むことを推奨する。

## 設計のポイント

- 最も単純な手法（そのまま利用）から始め、必要が生じた場合のみ次の段階へエスカレーションする
- 各ステップにエスカレーションの判断基準（例: プロンプトが約2000トークンを超える、ドメイン固有の幻覚が続く）を明示する
- RAGやキャッシュ、蒸留など『モデルの重みは変えずに周辺を強化する』段階を、ファインチューニングより先に検討する
- 各段階をAWSの具体的サービス（Bedrock、SageMaker、Nova Forge）にマッピングし実装の見通しを立てやすくする

## 使いどころ

- 生成AI導入プロジェクトの立ち上げ時にどの手法から着手すべきか判断したいチーム
- ファインチューニングに飛びつく前にコストと効果を見積もりたい場合
- プロンプトエンジニアリングで頭打ちになり次の投資段階を検討している場合
