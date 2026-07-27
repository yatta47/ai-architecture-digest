---
type: announcement
title: エージェントをPythonクラスとして設計するハーネス「NOOA」
title_original: Six Agent Harness Capabilities for Higher Model Performance
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- memory-consolidation
- eval
components:
- NOOA
- SWE-bench Verified
- CyberGym L1
- ARC-AGI-3
- SQLite
- GPT-5.5
- Opus 4.6
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/
published_at: '2026-07-27'
---

## 概要

NVIDIA LabsはエージェントをPythonの単一クラスとして表現するオープンソースフレームワーク「NOOA」を公開した。型付き入出力・参照渡し・コードとしての行動などの設計原則により、SWE-bench VerifiedやCyberGym L1、ARC-AGI-3でSOTA相当の精度を、従来ハーネスの約半分のトークン数で達成した。人間可読なSQLiteストアに長期記憶を蓄積・自己整理させることでコンテキスト圧縮や要約パイプラインを不要にしている。

## 設計のポイント

- エージェントを単一のPythonクラスとして実装し、メソッド・フィールド・docstring・型注釈をそれぞれ能力・状態・プロンプト・契約として扱う
- メソッド本体を省略記号にしてLLM駆動ループに実行時補完させ、通常のPythonコードと同じ開発ツールでレビュー・テスト・バージョン管理できるようにする
- オブジェクトをシリアライズせず参照渡しすることで、コンテキストに載せる情報を要約せずに絞り込みトークンコストを削減する
- 長期記憶を型付きレコードとしてSQLiteに保存し、バックグラウンドの整理処理で重複統合・関連付け・不要情報の刈り込みを行う

## 使いどころ

- 複雑なエージェントの振る舞いをコードとして差分レビューやユニットテストで検証したいチーム
- コンテキスト圧縮や要約パイプラインを組まずに長期タスクを継続させたいエージェント開発者
- ソフトウェアエンジニアリングやセキュリティ診断など高精度かつ低コストなベンチマーク性能が必要な場面
