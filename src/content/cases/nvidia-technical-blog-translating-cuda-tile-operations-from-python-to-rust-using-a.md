---
type: case
title: エージェント型AIでCUDAタイルカーネルをPythonからRustへ自動移植
title_original: Translating CUDA Tile Operations from Python to Rust Using Agentic AI
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- eval
components:
- TileGym
- cuTile Rust
- cuTile Python
- Triton-TileIR
- NVIDIA Nemotron
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/translating-cuda-tile-operations-from-python-to-rust-using-agentic-ai/
published_at: '2026-09-16'
---

## 概要

NVIDIAはTileGymリポジトリのCUDAタイルカーネルをcuTile PythonおよびTriton-TileIRからcuTile Rustへ自動変換するAIエージェントスキルを構築し、公開24オペレータ全てを移植してcuTile Python比平均99.5%の性能を達成した。各変換は解析・デバイスカーネル生成・ホスト/FFIコード生成・ベンチマークという段階に分かれた多段エージェントパイプラインで進み、各段階で機械的に検証可能な判定を経てから次へ進む。

## 設計のポイント

- 3つのフロントエンド(cuTile Python/Triton-TileIR/cuTile Rust)が同じCUDA Tile IRにコンパイルされる特性を利用し、参照実装と変換後カーネルのIRを直接diffして構造的等価性を検証する
- 暗黙的なJIT特殊化をRustのシグネチャ上で明示的に宣言し直す作業を変換の中心に据える
- 各パイプライン段階に機械検証可能な合否判定を設け、どの段階の出力も無条件には信頼せず次段階へ進める
- C-ABI層でコピーや追加アロケーションなしにテンソル記述子を受け渡し、遅延コンパイルを可能にする

## 使いどころ

- 大量の本番GPUカーネルを別言語・別ランタイムへ機械的に移植したいチーム
- 変換の正確性を機能テストだけでなく構造レベルでも保証したい高性能計算基盤
- AIエージェントに多段階の検証ゲートを設けて品質を担保したいコード変換パイプライン
