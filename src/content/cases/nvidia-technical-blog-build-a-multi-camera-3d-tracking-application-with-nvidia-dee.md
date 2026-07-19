---
type: guidance
title: 自然言語プロンプトから多カメラ3Dトラッキングパイプラインを自動構築
title_original: Build a Multi-Camera 3D Tracking Application with NVIDIA DeepStream 9.1 Skills
industry: cross-industry
cloud: []
patterns:
- video-intelligence
- ai-agent
components:
- NVIDIA DeepStream 9.1
- Claude Code
- Codex
- PeopleNetTransformer
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-a-multi-camera-3d-tracking-application-with-nvidia-deepstream-9-1-skills/
published_at: '2026-07-15'
---

## 概要

NVIDIA DeepStream 9.1は、複数カメラの映像を共有3D座標系に統合し同一物体に一貫したIDを保つMulti-View 3D Tracking（MV3DT）と、チェッカーボード等を使わずカメラの内部・外部パラメータを自動推定するAutoMagicCalib（AMC）を追加した。あわせて13種の「エージェント型スキル」を提供し、Claude CodeやCodexなどのコーディングエージェントが自然言語プロンプトだけでマルチカメラ3Dトラッキングパイプラインをデプロイできるようにしている。

## 設計のポイント

- 各カメラが独立して2D検出を3D世界座標へ逆投影し、MQTTでトラックレットを共有してから3D近接度でマッチングすることで、単一カメラでは失われがちな「視野をまたいだ同一性」を保つ。
- チェッカーボードなど物理的な校正手順を、動いている物体の軌跡から内部・外部パラメータを推定する自動キャリブレーションに置き換え、運用の中断を避ける。
- パイプラインの構築・デプロイをコーディングエージェント向けの「スキル」として提供し、自然言語の指示から実行可能な構成へ変換できるようにする。

## 使いどころ

- 倉庫の安全監視や小売店舗の動線分析など、単一カメラでは視野を外れると追跡が途切れる広域空間監視。
- 定期的なカメラ再配置・再校正が発生する現場で、手動キャリブレーションの手間を減らしたい場合。
- 自然言語の指示だけでビジョンAIパイプラインの構築・変更を行いたい開発チーム。
