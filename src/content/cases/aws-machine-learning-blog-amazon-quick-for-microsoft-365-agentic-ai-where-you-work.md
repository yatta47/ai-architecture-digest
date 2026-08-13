---
type: announcement
title: Amazon QuickがMicrosoft 365内でエージェント型AIとして動作するようになった
title_original: 'Amazon Quick for Microsoft 365: Agentic AI where you work'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
components:
- Amazon Quick
- Microsoft Word
- Microsoft Excel
- Microsoft PowerPoint
- Microsoft Outlook
- Amazon QuickSight
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-quick-for-microsoft-365-agentic-ai-where-you-work/
published_at: '2026-08-13'
---

## 概要

Amazon QuickがMicrosoft Word/Excel/PowerPoint/Outlookに直接組み込まれるエージェント拡張機能を発表。既存のQuickSightダッシュボードやSalesforce、Jira、SharePointなどの接続データを、アプリを切り替えずに文書内で直接編集・参照できるようにする。

## 設計のポイント

- サイドパネルとして常駐し、変更箇所を監査証跡付きのビジュアル差分で提示することでエージェントによる編集の透明性を確保する
- クライアント側インストール不要で、Microsoft 365管理センターからマニフェスト配布することで全社展開を簡素化する
- Quickネイティブ認証を使い、Entraアプリ登録なしでも既存のセキュリティ枠組みを維持する

## 使いどころ

- 複数の社内データソースを横断してレポートや提案書を作成する必要があるナレッジワーカー
- 普段のOfficeアプリを離れずにAIエージェントを使いたい企業のエンドユーザー
