---
type: guidance
title: Bedrockで実装するマルチエージェント型の契約書類分類（ベクトル×プロンプト）
title_original: Implement vector-prompt document classification using Amazon Bedrock
industry: financial-services
cloud:
- aws
patterns:
- multi-agent-orchestration
- document-processing
- ai-agent
components:
- Amazon Bedrock
- Strands Agents SDK
- Anthropic Claude Haiku 4.5
- Amazon Titan Multimodal Embeddings G1
- FAISS
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/implement-vector-prompt-document-classification-using-amazon-bedrock/
published_at: '2026-08-18'
---

## 概要

保険会社が日々大量に扱うポリシー・宣誓書・裏書・規制書類は、似た文言でも用途が異なり誤分類がコンプライアンス違反につながりうる。本記事はStrands Agents SDKでDocument Analysis Agent(テキスト推論)、Vector Similarity Search Agent(レイアウト類似検索)、Validation Agent(検証・統合)の3エージェントを協調させ、単一モデルより高精度な文書分類を実現するマルチエージェント構成を解説する。

## 設計のポイント

- Validation Agentがオーケストレーターとなり他の専門エージェントをツールとして呼び出す「agents-as-tools」パターンにより、カスタムのオーケストレーションコードを書かずに合意形成・矛盾解決を行う
- Claude Haiku 4.5によるテキスト推論とTitan Multimodal Embeddingsによるレイアウト・視覚パターン認識を組み合わせ、文言が似ていても構造で判別できるようにする
- Vector Similarity Search AgentはFAISSで既知テンプレートとの高速な類似検索を行い、フォーム構造や表組みなどの視覚的特徴を捉える
- Validation Agentが各エージェントの結果を突き合わせて信頼度スコアを付与し、エッジケースを人によるレビューにフラグ立てする

## 使いどころ

- 保険・金融など、似た文言でも法的性質が異なる大量の文書を日次で分類する必要がある業務
- テキストだけ、あるいは画像だけの単一モデル分類では精度が不十分なエッジケースが多い文書処理
- 各エージェントの判断根拠を監査証跡として残したい、コンプライアンス要件の強い分類システム
