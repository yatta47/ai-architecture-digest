---
type: guidance
title: 本番AIエージェントのトレースを自動調査し障害パターンを特定するArize AXの「Signal」
title_original: How to debug production AI agents with Signal in Arize AX
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- root-cause-analysis
- eval
components:
- Arize AX
- Signal
- OpenInference
- GitHub
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/debug-production-ai-agents-with-signal-tutorial/
published_at: '2026-08-04'
---

## 概要

Arize AXに組み込まれたマネージドエージェント「Signal」は、本番AIエージェントのトレースを定期的にレビューし、繰り返し発生する失敗パターンを根拠・推定原因・推奨対応付きで優先順位付けされたIssueにまとめる。トレース計装、行動契約を表す評価(evaluations)の追加、Signalの有効化という3ステップのチュートリアルとして紹介されており、リポジトリ接続時にはコード修正のプルリクエスト提案まで行うが、最終的なマージ判断は人間のエンジニアに委ねられる。

## 設計のポイント

- トレースをエージェントの実際の挙動を示す唯一の真実源として扱い、最終応答だけでなくツール呼び出し・ルーティング遷移・再試行・セッション情報まで計装する
- 汎用的な品質スコアではなく、ルーティング正解性やツール呼び出し必須性などユーザーに可視な行動契約を評価器として定義し、調査の起点を明確にする
- 自己改善ループを「本番挙動→証拠→調査→提案→人間の承認」という制御された段階に分離し、エージェントが無検証でコードを書き換え・デプロイすることは許さない
- リポジトリ連携やPR作成はオプトインの追加機能とし、まずトレースのみの調査から始めて段階的に導入できるようにする

## 使いどころ

- 大量の本番トレースの中から、ルーティング誤り・ツール誤選択・空の検索結果などエージェント特有の失敗パターンを人手では追いきれないチームが自動集約・優先順位付けしたい場合
- 評価に落ちた実行群が単一のルーティング欠陥なのか複数の無関係なツール障害なのかを切り分けたい開発者
- コーディングエージェントによる修正提案をプルリクエストとして受け取りつつ、レビューとマージは人間が行う安全なワークフローを構築したい組織
- データセット・評価・実験を通じて、提案された修正が実際にエージェントを改善したかを検証したいチーム
