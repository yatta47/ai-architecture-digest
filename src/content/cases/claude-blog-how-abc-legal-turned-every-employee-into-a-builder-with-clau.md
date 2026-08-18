---
type: case
title: 全社員がエージェントを構築できる体制へ:ABC LegalのClaude Managed Agents導入
title_original: How ABC Legal Turned Every Employee into a Builder with Claude Managed Agents
company: ABC Legal
industry: other
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- event-driven
- ci-cd
components:
- Claude Enterprise
- Claude Managed Agents
- Claude Code
- NetSuite
- Slack
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
published_at: '2026-08-17'
---

## 概要

米国の法務文書配達企業ABC Legal(従業員1,100人)は、Claude Enterpriseの導入で現場発の自動化が自然発生した後、個人のPC上で動くバラバラなスケジュールタスクを、バージョン管理・監査・コストが一元化されたClaude Managed Agentsへ移行した。エンジニア以外を含む15人の運営委員会がClaude Codeでエージェントをgitリポジトリ上のコード(プロンプト+設定)として構築し、PRレビューを通じてのみ変更できる体制を1週間で立ち上げた。1か月で50件以上のエージェントが法務・経理・マーケティング・業務運用の各所で稼働し、対象業務の人的コストを最大約50%削減、約310人の従業員が日常的にClaudeを利用するまでに拡大した。

## 設計のポイント

- エージェントをプロンプト+設定のコードとして定義し、gitリポジトリでバージョン管理・PRレビュー・ロールバックを可能にする
- イベント駆動型と定期実行型の2種類のスターターテンプレートを用意し、誰でも複製してカスタマイズできるようにする
- Managed Agentsがランタイムを提供することで、非エンジニアでもソフトウェアを書かずに設定とプロンプトの記述だけでエージェントを構築できる
- 各エージェントに名前・オーナー・単一の役割を持たせ、監査ログとコストを一元的に可視化する

## 使いどころ

- 個人のPC上でバラバラに動いていた自動化スクリプトを、常時稼働・監査可能なクラウド実行に統合したい組織
- 開発チームを介さず業務部門の担当者が自らの反復業務を自動化したい全社的なAI活用
- コードレビュー、文書配送、経理のリマイタンス処理、裁判所への申立て却下対応など部門横断の反復業務の自動化
