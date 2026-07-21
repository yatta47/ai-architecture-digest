---
type: announcement
title: NVIDIA GB300 NVL72、新エージェントAIベンチマークAA-AgentPerfでH200比最大20倍のエージェント処理性能を達成
title_original: NVIDIA Achieves Leading Agentic Coding Performance on First Agentic AI Benchmark
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- inference-optimization
- eval
components:
- NVIDIA GB300 NVL72
- NVIDIA H200
- NVIDIA Vera Rubin
- DeepSeek-V4-Pro
- SGLang
- TensorRT-LLM
- vLLM
- AA-AgentPerf
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-achieves-leading-agentic-coding-performance-on-first-agentic-ai-benchmark/
published_at: '2026-06-25'
---

## 概要

Artificial Analysisが開発した業界初のマルチベンダー向けエージェントAIベンチマーク「AA-AgentPerf」は、非決定的なツール呼び出しや可変長シーケンスを含む実運用に近いコーディングエージェントの実行トレースを用い、SLO(出力速度・TTFT)を満たしつつ何並列のエージェントを処理できるかをアクセラレータあたり・メガワットあたりで正規化して測定する。NVIDIA GB300 NVL72はWideEP/DeepEP、DeepGEMM、fused MoE、NVLinkスケールアップなどの最適化により、前世代のH200比で最大20倍のメガワットあたり同時エージェントスループットを達成し、次世代Vera Rubinではさらなる性能向上が見込まれている。

## 設計のポイント

- エージェントワークロードの性能評価では、非決定的なリクエスト列・ツール呼び出しレイテンシ・可変長シーケンスを含む実際のエージェント軌跡(trajectory)を再現することが重要で、静的なプロンプトのベンチマークでは不十分。
- スループットの絶対値ではなく、出力トークン速度とTTFTのSLO閾値を満たせる最大同時実行数を測定し、それをアクセラレータ数やメガワットで正規化することで、ハードウェア間の公平な比較とデータセンターの容量計画への転用が可能になる。
- テストセットを非公開に保つことで、特定ベンチマークに最適化したチューニング(ベンチマークハッキング)を防ぎ、測定結果の信頼性を担保する。
- MoEエキスパートをNVLinkドメイン全体に分散するWideEP/DeepEPや、NVLink通信とテンソルコア計算をオーバーラップさせるDeepGEMM/fused MoEなど、ハードウェアとランタイム(SGLang/TensorRT-LLM/vLLM)の協調設計がエージェント同時実行数のスケールに直結する。

## 使いどころ

- データセンターの電力予算に対して何セッション分のコーディングエージェントを収容できるかを見積もりたい容量計画担当者。
- GB300 NVL72やH200などのアクセラレータ世代を比較し、エージェント推論基盤への投資判断を行いたいインフラ意思決定者。
- SGLang・TensorRT-LLM・vLLMなどのエージェントランタイムを運用し、MoE並列化やNVLink活用の最適化効果を実測したいプラットフォームチーム。
