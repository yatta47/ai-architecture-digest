---
type: guidance
title: 'NVIDIA XR AI: ARグラス/XRデバイス向けAIエージェント基盤'
title_original: Building AI Agents for AR Glasses and XR Devices with NVIDIA XR AI
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- voice-agent
- multi-agent-orchestration
components:
- NVIDIA XR AI
- NVIDIA Cosmos
- NVIDIA Nemotron
- Model Context Protocol
- NVIDIA NeMo Agent Toolkit
- NVIDIA CloudXR
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/building-ai-agents-for-ar-glasses-and-xr-devices-with-nvidia-xr-ai/
published_at: '2026-07-09'
---

## 概要

ARグラスやXRヘッドセット向けにライブのカメラ・マイク・エンタープライズデータ・ツール利用を統合するオープンソースライブラリ。NVIDIA CosmosによるVisual grounding、Nemotronによる音声理解と推論、MCP経由のエンタープライズ接続、NeMo Agent Toolkitによるオーケストレーションをモジュール化し、Stanford/Princetonの研究室やSiemensの製造現場実証などで応用が進む。

## 設計のポイント

- メディア転送・モデルサービス・ツールアクセス・エージェントオーケストレーション・クライアント配信を疎結合なモジュールに分離する
- 映像は共有メモリに留め軽量メタデータのみをやり取りし、タスクに必要な時だけ画像データを取得して不要な推論を減らす
- 参加者IDをルーティング境界にすることで複数クライアント・複数エージェントが同一ハブに接続するマルチユーザー構成に対応する

## 使いどころ

- フィールドサービスや製造現場でハンズフリーの手順ガイドや検証をARグラス越しに提供したい企業
- 研究室など専門作業中に音声で情報検索・システム操作を行いたい医療・製造分野のチーム
