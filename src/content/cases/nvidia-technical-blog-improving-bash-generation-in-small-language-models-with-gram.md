---
type: case
title: 文法制約デコーディングで小型LLMのBashコマンド生成精度を改善
title_original: Improving Bash Generation in Small Language Models with Grammar-Constrained Decoding
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- inference-optimization
- guardrails
- eval
components:
- grammargen
- llama.cpp
- llguidance
- tree-sitter-bash
- Qwen3-0.6B
- SmolLM2-360M-Instruct
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/improving-bash-generation-in-small-language-models-with-grammar-constrained-decoding/
published_at: '2026-06-11'
---

## 概要

NVIDIA AI Red Teamは、--helpドキュメントやJSONツールスキーマからLarkグラミアを自動生成するgrammargenを開発し、llama.cpp上でllguidanceを介した文法制約デコーディングを小型LLMのBashコマンド生成に適用した。tree-sitter-bashで構文検証しつつ「constrained retry」を組み合わせる評価パイプラインにより、13モデル・299タスクで平均パス率を62.5%から75.2%に改善し、Qwen3-0.6Bでは16.7%から59.2%まで向上した。

## 設計のポイント

- コマンドのヘルプ出力やJSONスキーマから構造化された証拠を抽出し、Larkグラミアへ自動変換することで手書き文法のブリトルさを回避する
- オプションの有界反復(bounded repetition)を用いてデコーディング状態を有限に保ち、実用的な速度でグラミアを適用できるようにする
- ネイティブ生成をまず試し、tree-sitter-bashでエラーが出た場合のみ文法制約デコーディングへリトライすることで、ネイティブ相当以上の性能を保ちつつ1コマンドのみ実行する
- 文法はすべての受理コマンドの安全性を保証するものではなく、あくまでデコーディング境界を定義するものとし、ポリシーは追加の文法制約や別レイヤーの制御として実装する

## 使いどころ

- 小型・軽量なLLMをエージェントのコマンド実行コンポーネントとして信頼性高く使いたい場合
- セキュリティレッドチームがエージェントの安全なツール呼び出し境界(構文的に妥当な範囲)を設計・検証する場面
- リソース制約のあるエッジ/オンプレ環境で小型モデルの成功率を底上げしたいエージェント開発者
