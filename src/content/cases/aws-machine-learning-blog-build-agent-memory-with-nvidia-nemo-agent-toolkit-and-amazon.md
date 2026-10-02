---
type: guidance
title: NeMo Agent ToolkitのメモリにAmazon S3 VectorsをEKS上で組み込む
title_original: Build agent memory with NVIDIA NeMo Agent Toolkit and Amazon S3 Vectors
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- memory-consolidation
components:
- Amazon S3 Vectors
- NVIDIA NeMo Agent Toolkit
- Amazon EKS
- Amazon Titan Text Embeddings V2
- Amazon Bedrock
- boto3
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-agent-memory-with-nvidia-nemo-agent-toolkit-and-amazon-s3-vectors/
published_at: '2026-10-01'
---

## 概要

NVIDIA NeMo Agent Toolkit(NAT)の記憶サブシステムに、Amazon S3 Vectorsをカスタムメモリプロバイダーとして実装しEKSへデプロイする手順を示した記事。MemoryEditorインターフェースを実装し、マルチエージェントの投資調査を例に永続メモリを構成する。強い書き込み整合性や最大20億ベクトルへのスケールが選定理由として挙げられている。

## 設計のポイント

- MemoryEditor(add_items/search/remove_items)を実装するだけで、独自バックエンドをNATのプラグインとして差し替えられる。
- メモリの本文は非フィルタ可能メタデータにし、検索用メタデータだけをフィルタ対象にする。
- 強い書き込み整合性により、複数エージェントが書いた記憶が直後から他エージェントに見える。
- テナントごとにインデックスを分けて、IAMで隔離する。

## 使いどころ

- 複数エージェント間で長期記憶を共有する本番システムを構築するチーム。
- アイドルコストなしで大規模な記憶ストアを持ちたいとき。
- NATの既存プロバイダー(Mem0やRedis等)では規模やコストが合わない場合。
