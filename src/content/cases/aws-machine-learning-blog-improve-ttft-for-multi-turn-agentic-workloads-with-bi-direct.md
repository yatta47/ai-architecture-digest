---
type: guidance
title: マルチターンのエージェント向けに双方向KV転送でTTFTを短縮する
title_original: Improve TTFT for multi-turn agentic workloads with bi-directional KV transfer in vLLM
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- ai-agent
- context-engineering
components:
- vLLM
- NVIDIA NIXL
- AWS EFA
- Amazon EC2 P5en
- Qwen3-32B
- GLM-5-FP8
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/improve-ttft-for-multi-turn-agentic-workloads-with-bi-directional-kv-transfer-in-vllm/
published_at: '2026-10-19'
---

## 概要

従来の分離推論はKVをprefillからdecodeへ一方向にしか送らないため、マルチターンでは前回の応答分まで再計算が発生する。双方向転送で計算済みコンテキストを再利用し、TTFTをQwen3-32Bで最大1.6倍、GLM-5-FP8で最大3.3倍短縮した。

## 設計のポイント

- decode側が持つ応答分のKVをprefill側へ戻し、次のターンで再計算を避ける。
- セッション状態をdecode側だけが持つ非対称さが、prefill側でのキャッシュ追い出しを招く点を解消する。
- 会話履歴が伸びるエージェントほど冗長なprefillが増えるため、効果が大きい。
- EFAのRDMAで転送し、アクセラレータ非依存の機能としてvLLMに寄与した。

## 使いどころ

- ツール呼び出しを重ねる長いエージェントセッションを低遅延で提供したい場面。
- 会話履歴の再計算でアクセラレータ容量が逼迫している推論基盤。
- チャットボットの応答性を会話が長くなっても保ちたいサービス。
