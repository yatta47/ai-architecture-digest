---
type: guidance
title: Claude Cowork公式プロダクトガイド：知識労働を任せるデスクトップエージェント
title_original: The Claude Cowork product guide
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
components:
- Claude Cowork
- Slack
- Google Drive
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/the-claude-cowork-product-guide
published_at: '2026-06-05'
---

## 概要

Claude Coworkは、対話するだけのAIと異なりローカルファイルの読み書きやSlack・Google Driveなど連携アプリ横断のマルチステップ作業をこなし、実際のファイルやメッセージへの引用付きで成果物まで仕上げるデスクトップ常駐のナレッジワークエージェントである。本記事はサブエージェントや長時間実行・スケジュールタスクといった主要機能、チャット/Claude Code/Coworkの使い分け、リサーチブリーフや会議準備・定例レポートなど7つの代表的ワークフロー、マーケティングやプロダクト管理向けプラグインの使い方をまとめたプロダクトガイドである。

## 設計のポイント

- 対話型AIとは切り離し、ゴールと成果物・頻度を指定するだけで複数ステップの作業計画と実行を任せる設計とする
- ローカルファイルアクセスとSlack・Google Driveなど外部アプリ連携を組み合わせ、成果物に元ファイル・メッセージへの引用を付与する
- サブエージェントや長時間実行・スケジュールタスクにより、単発の応答ではなく継続的な業務遂行を可能にする
- チャット（対話ドラフト）・Claude Code（コーディング）・Cowork（アプリ横断のナレッジワーク）で用途に応じてツールを使い分けるプロダクトマトリクスを提示する

## 使いどころ

- 商談や会議前のリサーチブリーフ・準備資料を作りたい場合
- 定例レポートなど繰り返し発生するアプリ横断のドキュメント作成業務を自動化したい場合
- マーケティングやプロダクトマネジメント業務をプラグイン単位で標準化・効率化したい場合
- 対話だけでは完結しない、複数アプリをまたぐ成果物作成までを一気通貫でAIに任せたい場合
