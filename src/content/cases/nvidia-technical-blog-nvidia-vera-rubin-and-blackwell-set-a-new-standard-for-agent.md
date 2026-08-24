---
type: announcement
title: エージェント型コーディングセッションを再現するAgentXベンチマークで測るVera Rubinの電力あたり性能
title_original: NVIDIA Vera Rubin and Blackwell Set a New Standard for Agentic AI Performance per Watt
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- eval
components:
- NVIDIA Vera Rubin NVL72
- NVIDIA GB300 NVL72
- NVIDIA Dynamo
- SGLang
- TensorRT-LLM
- vLLM
- SemiAnalysis AgentX
- NVLink
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-vera-rubin-and-blackwell-set-a-new-standard-for-agentic-ai-performance-per-watt/
published_at: '2026-08-24'
---

## 概要

実運用のコーディングエージェントセッションを再生してエージェント型推論性能を評価するSemiAnalysisのAgentXベンチマークにより、NVIDIA Vera Rubin NVL72はGB300 NVL72比で最大30倍のAIファクトリー当たりスループット(トークン/メガワット)を達成した。GB300 NVL72もH200 NVL8比で大規模MoEモデルにおいて最大80倍の効率向上を示し、SGLang/TensorRT-LLM/vLLMなどのMoE推論ランタイムとDynamoのセッション認識サービングが効率化に寄与した。

## 設計のポイント

- 固定長プロンプトの静的ベンチマークではなく、実際のClaude Codeセッションを再生してKVキャッシュ再利用・ツール呼び出しの間隙・動的並行性を捕捉するベンチマーク設計を採用する
- スループットを「メガワットあたりトークン数」という電力効率指標で評価し、TTFT・E2Eレイテンシとのトレードオフを併記することで実用性を担保する
- MoEサービング向けのカーネル最適化(DeepGEMM)や混合精度フォーマット(MXFP4/MXFP8)、ラック規模のNVLinkファブリックをシステムレベルで組み合わせて効率を最大化する

## 使いどころ

- エージェント型ワークロード向けにGPUインフラの電力効率を比較検討したいAIファクトリー運用者
- コーディングエージェントのような長文脈・ツール呼び出しを伴う推論のベンチマーク設計を検討する場合
