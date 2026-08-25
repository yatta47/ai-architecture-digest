---
type: guidance
title: AIネイティブSDLC：計画からデプロイ・保守までを機械可読アーティファクトでつなぐエージェント駆動プレイブック
title_original: The AI-Native SDLC Playbook
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- spec-driven-development
- ci-cd
- eval
- human-in-the-loop
components:
- Claude Code
- CLAUDE.md
- Claude Enterprise
- Claude Tag
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/the-ai-native-sdlc-playbook
published_at: '2026-08-21'
---

## 概要

Anthropicの記事は、エージェントによるコーディングで実装フェーズが速くなった結果、計画・レビュー・デプロイなど人間速度の工程がボトルネック化し、既存の承認ゲートやレビュー体制が破綻することを指摘する。各ステージ(計画・設計・構築・テスト・デプロイ・保守)を intent.md/spec.md/plan.md やdiff、PRレビュー、インシデント記録といったバージョン管理された機械可読アーティファクトの連鎖として再設計し、前段の出力を次段が読み込む非線形ループにすることで、人間はコミットのチェーンを監査証跡として判断が必要な箇所だけレビューする構成を提案している。

## 設計のポイント

- 各ステージの終わりに人間可読かつ機械実行可能なアーティファクト(intent.md、spec.mdなど)をバージョン管理にコミットし、次のステージがそれを読み込んで開始する
- 実装の高速化に合わせてレビュー体制も再設計し、規制対象/重要なコードだけ人間レビューに残し、その他はエージェントによる多層レビューとフックによる承認ゲートで担保する
- ステージ境界での一括QAゲートではなく、実装に継続的に評価(eval)を織り込む
- 本番監視もエージェントに担わせ、制御範囲の逸脱を検知したら新しいintent.mdとしてループへ書き戻す

## 使いどころ

- エージェントによる実装速度向上に対して、レビュー・承認プロセスが追いつかず監視待ちになっている開発組織
- 規制業種など、どこに人間レビューを残しどこを自動化するかを設計し直したいエンジニアリング/コンプライアンスチーム
- ドキュメント（要件・設計・監査証跡）をエージェントと人間が共通に読み書きできる形にしたいSDLC刷新プロジェクト
