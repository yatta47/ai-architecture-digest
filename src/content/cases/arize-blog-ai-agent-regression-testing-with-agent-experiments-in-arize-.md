---
type: guidance
title: AIエージェントの変更による副作用を検出する回帰テスト手法
title_original: AI agent regression testing with Agent Experiments in Arize AX
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components:
- Arize AX
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/ai-agent-regression-testing-with-arize-ax/
published_at: '2026-09-14'
---

## 概要

Arize AXのAgent Experimentsを使い、エージェントへの修正が意図した問題を直しつつ他のワークフローを壊していないかを回帰テストする方法を解説する。あるデモでは注文キャンセルの安全性を高める修正によりタスク完了スコアが0.89から0.72へ低下する副作用が見つかり、単一の失敗ケースだけでなく既存の正常系も含めたデータセットでの比較が必要だと示した。

## 設計のポイント

- 修正前後の設定をベースライン/候補としてプリセット化し、同一データセットに対して並行実行して比較する
- 回帰データセットには失敗ケースだけでなく、共通の正常系ワークフローも含めて副作用を検知できるようにする
- 安全性（action safety）とタスク完了率を別々に評価し、片方だけでは見落とす劣化を捉える
- スコアの変化だけで判断せず、個々の結果のトレースを開いて実際の挙動を確認してから出荷判断する

## 使いどころ

- プロンプトやツール、ポリシーの修正がエージェントの別のワークフローに悪影響を与えていないか検証したい場合
- サポート・購買・調査など複数の業務を跨ぐエージェントの品質を継続的に保証したいチーム
- 本番稼働中のエージェントに対してリリース前の安全網を構築したい場合
