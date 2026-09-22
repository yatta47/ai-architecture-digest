---
type: guidance
title: 機密コンピューティング環境でLLM推論性能をほぼ落とさず維持する設計
title_original: Enabling Private High-Performance Production AI Inference with NVIDIA Confidential Computing
industry: cross-industry
cloud: []
patterns:
- confidential-computing
- inference-optimization
components:
- NVIDIA TensorRT LLM
- NVIDIA Blackwell GPU
- NVIDIA NVLink
- Intel TDX
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/enabling-private-high-performance-production-ai-inference-with-nvidia-confidential-computing/
published_at: '2026-09-22'
---

## 概要

機密仮想マシンと機密GPU、暗号化NVLinkによりLLM推論を信頼された実行環境内で処理できるNVIDIA Confidential Computingについて、TensorRT LLMが行ったCC有効時の性能検証を紹介する。長文脈・低並行度という最もオーバーヘッドが露見しやすい条件でも、スループットの96〜98%を維持しレイテンシ悪化は1〜4%に収まった。

## 設計のポイント

- ホスト-デバイス間転送はピン留めメモリの非同期優位性が失われるためCC環境ではページャブルメモリを選択するよう切り替えた
- トークンやサンプリングデータの読み戻しを非同期ワーカーに移しデコード中のスケジューラブロッキングを防いだ
- CUDAイベントのタイミングが不安定になるためカーネルオートチューナーはGPUのグローバルタイマーを使うよう変更した
- NVLS（NVLinkマルチキャスト）が使えないCC構成向けにトポロジーとメッセージサイズに応じた通信アルゴリズムを選択する必要がある

## 使いどころ

- 金融・医療など機密性の高いプロンプトやモデル資産を扱うLLM推論基盤
- 機密コンピューティング導入時の性能劣化を事前に見積もりたいAIプラットフォームチーム
- TensorRT LLMを自前でCC対応させる際のオーバーヘッド計測方法を知りたい場合
