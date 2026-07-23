---
type: case
title: Outtakeが構築した自律型サイバー捜査エージェント「Recon Agent」
title_original: How Outtake built a cyber investigator on Claude
company: Outtake
industry: other
cloud: []
patterns:
- ai-agent
- root-cause-analysis
- eval
components:
- Claude Code
- Claude Agent SDK
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude
published_at: '2026-07-22'
---

## 概要

サイバーセキュリティ企業Outtakeは、Claude CodeとClaude Agent SDKを用いて、フィッシングサイトなどの攻撃者ネットワーク全体を自律的に調査・解体する「Recon Agent」を構築した。人間の専門家が行う調査プロセスをまず標準化し、Claude Codeでプロトタイピングした後、Agent SDKで本番グレードのハーネスに移行することで、数時間に及ぶ長時間自律セッションでも軌道を外れない設計を実現した。

## 設計のポイント

- まず人間自身が実際の調査を行い「良い調査とは何か」を定義してから自動化に着手する
- Claude Codeでプロトタイピングし、オーケストレーションレベルでは厳密に制約しつつ判断が必要な部分は自由に改善させる設計原則を確立する
- 本番化ではClaude Agent SDKに移行し、メモリ・コンテキスト・ファイルシステムをより細かく制御する
- 開発初期からエージェント評価(evals)を組み込み、安価かつ迅速に反復できるループを構築する

## 使いどころ

- なりすましサイトやフィッシングネットワークなど攻撃者インフラ全体を追跡したいセキュリティチーム
- 数時間に及ぶ長時間自律エージェントセッションの軌道維持が課題になっているプロダクト
- コード生成・実行や外部システムとの対話が必要な高度に技術的な調査タスクの自動化
