---
type: guidance
title: LLMサービングはスループットではなくgoodput（SLO達成リクエスト数）で見るべき理由
title_original: Why Goodput Matters More Than Throughput for LLM Serving
company: Akamas
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- llmops
components:
- vLLM
- Qwen2.5-7B
- Amazon EKS
- GuideLLM
- Prometheus
- Grafana
- NVIDIA DCGM Exporter
outcome:
  type: quality
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/20/why-goodput-matters-more-than-throughput-for-llm-serving/
published_at: '2026-07-20'
---

## 概要

LLMサービングのベンチマークではスループット（req/s）が重視されがちだが、著者はvLLM単体GPU環境でのチューニングを通じ、TTFT・TPOTなどのレイテンシSLOを満たした完了リクエスト数を表す『goodput』こそが実態を捉える指標だと指摘する。EKS上のNVIDIA A10GでQwen2.5-7BをvLLMで配信し、gpu_memory_utilization・max_num_batched_tokens・max_num_seqsの3設定のみを変えてGuideLLMで負荷をかけたところ、TTFT制約下でスループットを約50%改善した設定はp95 TPOTが約10倍に悪化するというトレードオフが判明した。チャットボット・reasoning・エージェント型など、ワークロードごとに効くレイテンシ指標が異なるため、目的のSLOに合わせたチューニングと計測手法（レートスイープ／飽和スループット、ウィンドウ集計）の使い分けが重要だとしている。

## 設計のポイント

- スループットではなくTTFT/TPOTのレイテンシSLOを満たした完了リクエスト数(goodput)を最適化目標に据える
- gpu_memory_utilization・max_num_batched_tokens・max_num_seqsという運用時に安全に変更できる3パラメータに絞ってKVキャッシュ量・バッチサイズ・同時実行数のトレードオフを調整する
- 実運用に近い負荷を再現するレートスイープと、上限を探る飽和スループットランを使い分けてベンチマークする
- 8点連続の安定区間からプラトーを読み取るウィンドウ集計ルールでメトリクスのジッターを除去し、再現性のある比較を行う

## 使いどころ

- チャットボット・reasoning・エージェント型のように、リクエストごとに支配的なレイテンシ指標(TTFT/TPOT)が異なるLLMサービングの容量設計に有効
- 本番導入前に単一GPUなど低コスト環境でvLLMサービング設定を再現性高くチューニングしたい場合に使える
- 『スループットは上がっているのに体感品質が落ちている』ケースの原因究明やSLO再設計の指針になる
