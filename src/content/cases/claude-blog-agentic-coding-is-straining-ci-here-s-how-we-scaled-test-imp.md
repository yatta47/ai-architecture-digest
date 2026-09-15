---
type: case
title: CIジョブ25倍増に対応するため単一プロセスのテスト選択サービスをシャード分割で再設計
title_original: Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ci-cd
components:
- Claude Code
- Claude Tag
outcome:
  type: reliability
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
published_at: '2026-09-14'
---

## 概要

Anthropicは、Claudeによるコード生成量が8倍に増えCIジョブが6ヶ月で25倍に急増したことでテストインパクト分析(変更に対してどのテストを実行するか決定するサービス)がボトルネック化。単一プロセスの「リスナー/セレクター」構成を、コア増強→シャーディング→毎日再起動という3回の応急処置(それぞれ70日・29日・1日未満しか持たなかった)を経て、根本的なアーキテクチャ再設計に踏み切った。

## 設計のポイント

- 応急処置(マシン増強・部分並列化・再起動)は効果の持続期間が指数関数的に短くなり、早期に根本設計の見直しに投資する方が結果的に短時間で済む
- リスナーの遅延が閾値(50,000ジョブ)を超えたらClaude Tagの長期セッションが自動でアラートし対応を促す運用にした
- テスト結果の記録(リスナー)とテスト選択(セレクター)を単一ライターで同期させる設計が水平分割を阻んでいたため、パッケージ単位のシャードに分割してスケーラビリティを確保する方向に再設計した

## 使いどころ

- エージェントによるコード生成・レビューの高速化でCIジョブ量が急増しテスト選択サービスが逼迫しているエンジニアリング組織
- 変更のたびに全テストを実行するのが非現実的な規模のコードベースを持つチーム
