---
type: case
title: 非エンジニアのPMがClaude Codeのマルチエージェント構成で6週間開発したストレス管理アプリ「Respiro」
title_original: How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks
company: Respiro
industry: healthcare
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- spec-driven-development
components:
- Claude Code
- Claude Opus 4.6
- Sentry
- Amplitude
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks
published_at: '2026-05-01'
---

## 概要

プログラミング経験のないプロジェクトマネージャーが、Claude Codeを使い15以上の役割特化型サブエージェント（TCAアーキテクト、Swift開発者、Metal専門家、コードレビュアーなど）を並列稼働させるマルチエージェント体制で、ストレス検知・呼吸法アプリ「Respiro」をわずか6週間でiOS App Storeまでリリースした。React Native製MVPの限界に直面した際もSwiftへの全面書き換えを数時間で完了し、App Store申請や外部SaaS連携、マーケティング施策までClaudeの支援で進めた。

## 設計のポイント

- 役割ごとに専門特化したサブエージェント（アーキテクト・開発者・専門技術者・レビュアー）を並列稼働させるマルチエージェント構成でチームのように管理する
- 技術的制約（テスト端末の欠如など）が判明した時点でスタックを丸ごと書き換える判断を素早く下し、Claude Codeで数時間のうちに再実装する
- スクリーンショットを渡してClaudeに画面を解釈させ、外部サービスの複雑な管理画面操作を対話的にガイドしてもらう

## 使いどころ

- コーディング経験のない起業家やPMが、自らアプリを設計・実装・出荷したい場合
- App Store申請や外部SaaS連携など非開発タスクをAIの対話ガイドで進めたい場合
- 少人数・個人開発でマルチエージェント体制を組み、並列に開発を進めたい場合
