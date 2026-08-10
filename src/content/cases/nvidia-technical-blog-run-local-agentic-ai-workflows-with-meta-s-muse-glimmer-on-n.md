---
type: announcement
title: Meta「Muse Glimmer」でNVIDIA GPU上のローカル長時間エージェントを実現
title_original: Run Local Agentic AI Workflows with Meta's Muse Glimmer on NVIDIA
company: Meta
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- inference-optimization
- fine-tuning
components:
- Muse Glimmer
- NVIDIA NIM
- SGLang
- vLLM
- NVIDIA GeForce RTX 5090
- NVIDIA DGX Spark
- NVIDIA DGX Station
- NVIDIA Jetson
- NeMo AutoModel
- NeMo RL
- NemoClaw
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-local-agentic-ai-workflows-with-metas-muse-glimmer-on-nvidia/
published_at: '2026-08-10'
---

## 概要

Metaは120K+コンテキストの30BパラメータDenseモデル「Muse Glimmer」をオープンウェイトで公開し、NVIDIAのGPU群（RTX 5090・DGX Spark・DGX Station・Jetson）上でのオンデバイス長時間エージェントワークロード向けに最適化した。MoEのルーティングオーバーヘッドを避けるDense構成により長文脈での一貫性と予測可能なレイテンシを確保しつつ、Blackwell Ultra上で単一GPUあたり20K tokens/秒を実現する。

## 設計のポイント

- 全パラメータをトークンごとに活性化するDenseアーキテクチャを採用し、MoEのルーティング分散による遅延・信頼性のばらつきを避け、長時間の複数ステップワークフローでの一貫性を優先
- モデルサイズを単一GPUのVRAMに収まる規模（30B）に抑えることで、モデルシャーディングや外部エンドポイントへの依存を排除し、機微データを含むエージェント処理をデバイス内で完結
- NVIDIA NIMコンテナ・SGLang・vLLMなど複数の推論スタックを用意し、開発者は用途に応じて簡易デプロイと細粒度制御を選択できる
- NeMo AutoModelでHugging Face形式のチェックポイントをそのままSFT/LoRAファインチューニングでき、NeMo RLで強化学習の追加最適化も可能

## 使いどころ

- コード生成や個人アシスタントなど、機密性の高いローカルファイル・認証情報を扱う常時稼働エージェント
- エアギャップ要件やコンプライアンス上クラウド推論が使えないオンプレ環境（ロボティクス・産業オートメーション・エッジ）
- トークン課金なしで長時間・高頻度のツール呼び出しを行うエージェントを開発したいチーム
