---
type: announcement
title: Copilot CLIのスキル・カスタムエージェント・MCP利用状況をUsage Metrics APIで取得
title_original: Agentic CLI customizations now in the Usage Metrics API
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot CLI
- Model Context Protocol (MCP)
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-17-agentic-cli-customizations-now-in-the-usage-metrics-api
published_at: '2026-09-17'
---

## 概要

GitHub Copilot CLIの利用状況レポートAPIが、スキル・カスタムエージェント・MCPサーバー・スラッシュコマンド・プラグインといったエージェント関連のカスタマイズ活動まで対象を広げた。利用回数上位5件を示す『どれがよく使われているか』の指標と、利用された異なるアイテム数を示す『利用の広がり』の指標の両方を、個人単位・組織/エンタープライズ集計単位で提供する。

## 設計のポイント

- 『上位5件の利用回数』と『利用された異なるアイテム総数』という2種類の指標を分け、ホットスポットと利用の広がりを別々に把握できるようにする
- 顧客独自に定義したスキル名・エージェント名はプライバシー保護のため『other』『custom』にまとめて表示し、GitHub提供の既知アイテムのみ実名で表示する
- MCPサーバーのinteraction_countは接続（再接続）試行回数をカウントし、同一サーバー内の個々のツール呼び出し回数は加算しないという仕様上の注意点を明示する

## 使いどころ

- 社内で構築したスキル・MCPサーバーなどのエージェントカスタマイズが実際に使われているか監査したいプラットフォームチーム
- 組織内でのCopilot CLIカスタマイズの導入ギャップを見つけたい管理者
