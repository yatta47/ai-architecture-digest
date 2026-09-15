---
type: announcement
title: 既存のSalesforce権限内でClaudeが商談準備とCRM更新を代行するプラグイン
title_original: Bringing Salesforce into Claude
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- context-engineering
components:
- Claude
- Salesforce
- Slack
- Salesforce MCP
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/salesforce-in-claude
published_at: '2026-09-15'
---

## 概要

AnthropicがSalesforceと共同開発したプラグイン「Salesforce in Claude」をベータ公開。37のスキルでアカウント調査・架電準備・パイプラインレビュー・CRM更新を担い、既存のSalesforce権限内で読み書きする。GitLabやSiemens、Legoraなど7,000人の営業が利用中。

## 設計のポイント

- SalesforceとSlackの2つのコネクタでCRM・メール・通話記録・チャットに散らばる情報を横断的に集約する
- 更新はセラーの承認を経てから書き込むhuman-in-the-loop設計で信頼性を担保する
- 既存のSalesforce権限をそのまま適用しアクセス制御を二重管理しない

## 使いどころ

- 商談前の情報収集に多くの時間を取られている営業担当
- トップ営業のノウハウやパイプライン管理を組織全体で標準化したい営業リーダー
