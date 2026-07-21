---
type: guidance
title: 'AzureでRAGを構築する: ベクトル/全文/ハイブリッド検索によるインデックス設計と情報検索フェーズ'
title_original: 'Develop a RAG solution on Azure: Information retrieval phase'
industry: cross-industry
cloud:
- azure
patterns:
- rag
- full-text-search
components:
- Azure AI Search
- Azure OpenAI
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval
published_at: '2026-07-02'
---

## 概要

RAGソリューション構築シリーズのうち、チャンクの埋め込み生成後に行う「情報検索」フェーズを扱う記事。Azure AI SearchでのベクトルインデックスのHNSW/KNNアルゴリズムやefConstruction/efSearch/mパラメータの設定方法、ベクトル検索・全文検索・ハイブリッド検索(Reciprocal Rank Fusionによる再ランキング)の使い分けを、サンプルコード付きで解説している。

## 設計のポイント

- チャンク数が多いデータセットではHNSWのefConstructionを高めに設定して索引品質を上げ、チャンク数が少ない場合は低めにして構築時間・コストを抑えるなど、データ規模に応じてインデックスパラメータをチューニングする。
- クエリを埋め込む前にチャンク埋め込み時と全く同じ前処理(小文字化など)と同一の埋め込みモデルを適用し、クエリベクトルとチャンクベクトルの空間的整合性を保証する。
- 意味は似ているがキーワードや固有表現が異なるコンテンツには全文検索、意味的類似性を捉えたい場合はベクトル検索を使い分け、両方を組み合わせるハイブリッド検索ではReciprocal Rank Fusionで結果を再ランキングする。
- ハイブリッドクエリ内の各ベクトルクエリに個別の重み(デフォルト1.0)を設定できるため、フィールドごとの重要度に応じてRRFスコアへの寄与度を調整し検索精度を最適化する。

## 使いどころ

- RAGパイプラインでチャンクの埋め込み生成が終わり、次に検索インデックス設計と検索方式選定を行う開発者。
- キーワード一致と意味的類似性の両方が重要なFAQやナレッジベース検索を構築したい場合。
- Azure AI Search以外のベクトルストアを使う場合でも、インデックス/検索パラメータ設計の考え方を参考にしたいチーム。
