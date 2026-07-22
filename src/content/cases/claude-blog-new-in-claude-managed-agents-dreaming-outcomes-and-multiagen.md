---
type: announcement
title: セッションを跨いで自己改善するエージェント基盤：ドリーミング・アウトカム・マルチエージェント編成
title_original: 'New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration'
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- memory-consolidation
- eval
- ai-agent
components:
- Claude Managed Agents
- Claude Console
- Claude Haiku
- Claude Opus
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/new-in-claude-managed-agents
published_at: '2026-05-19'
---

## 概要

Claude Managed Agentsに、過去セッションを振り返りパターンを抽出してメモリを再構成する「ドリーミング」、成功基準のルーブリックを独立したグレーダーで評価し自己修正させる「アウトカム」、複数の専門サブエージェントに作業を分担させる「マルチエージェントオーケストレーション」が追加された。Harvey・Netflix・Spiral by Every・Wisedocsなどの導入企業では、完了率の向上やレビュー時間の大幅短縮といった成果が報告されている。

## 設計のポイント

- 「メモリ」がセッション中に学んだ内容を記録し、「ドリーミング」がセッション間でそれを横断的に見直してパターンを抽出・再構成することで、単一エージェントでは気づけない共通の失敗や好みを自己改善に反映する。
- 「アウトカム」はルーブリックで成功基準を明示し、エージェントの推論とは別コンテキストのグレーダーが出力を評価、不合格なら差分を指摘して再試行させる仕組みで人手レビューを減らす。
- マルチエージェントオーケストレーションでは、リードエージェントがタスクを分解し、モデル・プロンプト・ツールが異なる専門サブエージェントへ並列委任し、共有ファイルシステムとイベント履歴で状態を同期する。

## 使いどころ

- Harveyのような長文契約ドラフティングを行う法務ワークフローで、ファイル形式の癖やツール固有の対処法をセッションをまたいで学習させたい場合。
- Netflixのプラットフォームチームのように、数百件のビルドログを並列処理して再発する問題だけを抽出したい大規模ログ分析。
- Spiral by Everyのように、ブランドボイスや編集方針といった主観的品質基準を自動採点し、基準を満たした出力だけを返したいコンテンツ生成業務。
- Wisedocsのように、社内ガイドラインへの適合を自動チェックし、レビュー時間を削減したい文書品質検査業務。
