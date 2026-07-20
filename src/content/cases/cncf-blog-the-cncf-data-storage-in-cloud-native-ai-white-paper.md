---
type: guidance
title: クラウドネイティブAI/MLワークロード向けデータストレージ設計の白書
title_original: The CNCF Data Storage in Cloud Native AI White Paper
industry: cross-industry
cloud: []
patterns:
- rag
- memory-consolidation
- context-engineering
- data-federation
components:
- Apache Parquet
- Apache Iceberg
- Milvus
- Fluid
- Apache Kafka
- Kubernetes
outcome:
  type: speed
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/report-whitepaper/2026/07/08/the-cncf-data-storage-in-cloud-native-ai-white-paper/
published_at: '2026-07-08'
---

## 概要

CNCF TAG InfrastructureがKubernetes上でのデータ分析・AI/MLワークロード向けストレージ設計をまとめた白書を公開した。小ファイル問題やコンピュート・ストレージ分離によるボトルネックといった課題に対し、データレイクハウス(Parquet/Iceberg)とベクトルDB(Milvus)の統合、Fluidによる分散キャッシュ、CSI/COSIによる標準インターフェースを提案する。また学習・推論・エージェントAIという3フェーズごとに異なるストレージ要件(チェックポイント、KV/Prefixキャッシュ、短期・長期メモリ)を整理している。

## 設計のポイント

- モデル学習・推論・エージェントAIの3フェーズで異なるストレージ特性(スループット重視/低レイテンシ/メモリ階層)を分けて設計する
- データレイクハウス(Parquet/Iceberg)とベクトルDB(Milvus)を組み合わせてRAG向けのハイブリッド構成にする
- Fluidなどの分散キャッシュでデータローカリティを確保しGPU利用率の低下を防ぐ
- CSI/COSIなど標準化インターフェースでブロック・ファイル・オブジェクトストレージを統一的に扱う

## 使いどころ

- 大規模データセットの小ファイル問題に悩むMLインフラ担当者
- GPU利用率を上げたいモデル学習基盤のチーム
- RAGパイプラインのベクトル検索基盤を設計するAIプラットフォームエンジニア
- エージェントAIの短期・長期メモリのストレージ設計を検討する開発者
