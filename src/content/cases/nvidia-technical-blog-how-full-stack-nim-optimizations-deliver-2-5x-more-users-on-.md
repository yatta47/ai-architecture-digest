---
type: guidance
title: NIMフルスタック最適化でNemotron 3 Ultraの収容ユーザー数を2.5倍に
title_original: How Full-Stack NIM Optimizations Deliver 2.5x More Users on Nemotron 3 Ultra
industry: cross-industry
cloud: []
patterns:
- inference-optimization
components:
- NVIDIA NIM
- Nemotron 3 Ultra
- NVIDIA AI Enterprise
- NVIDIA AIPerf
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-full-stack-nim-optimizations-deliver-2-5x-more-users-on-nemotron-3-ultra/
published_at: '2026-09-10'
---

## 概要

NVIDIA NIM 2.0.12は、カーネル自動チューニング・テンソル並列・プレフィックス/状態再利用・MTP投機的デコードなどを組み合わせ、4xB200構成でユーザーあたり50TPSのインタラクティブ性を保ちながらベースラインの2.5倍のスループットを実現した。NIMは検証済み構成をコンテナ化して提供し、AIPerfで自社トラフィックに対するベンチマークも可能にする。

## 設計のポイント

- 精度・カーネル・並列化・スケジューリング・メモリ配分・デコード方式をシステム全体として同時最適化する
- 検証済み構成をマイクロサービス化して提供し、開発者はゼロから構成探索をしなくて済むようにする
- エージェント型ワークロード特有の長いプロンプトとコンテキスト再利用を前提にプレフィックス/状態キャッシュを設計する

## 使いどころ

- 同一GPUインフラでより多くの同時利用者を収容し、GPUあたりのコストを下げたい推論基盤チーム
- レイテンシSLOを保ちながらエージェント型AIワークロードのスループットを最大化したい場合
