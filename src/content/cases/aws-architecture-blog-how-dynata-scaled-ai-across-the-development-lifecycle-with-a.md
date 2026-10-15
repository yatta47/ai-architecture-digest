---
type: case
title: AI-DLCとKiroで開発ライフサイクル全体をAI化したDynataの事例
title_original: How Dynata scaled AI across the development lifecycle with AI-DLC and Kiro IDE
company: Dynata
industry: other
cloud:
- aws
patterns:
- spec-driven-development
- ai-agent
- context-engineering
components:
- Kiro IDE
- AI-DLC
- Confluence
- Jira
- GitHub
- Figma
- Lucidchart
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/
published_at: '2026-10-15'
---

## 概要

データ企業Dynataは、AI支援コーディングから始め、Confluence/Jira/Figma等の知識基盤をAIにつなぎ、AWSのAI-DLC手法とKiro IDEを採用した。通常3〜4スプリントかかる機能開発を約1スプリント分に短縮した。

## 設計のポイント

- コーディングだけでなく要件・設計・QA・デプロイ計画まで含む全工程にAIを組み込む
- 分散した要件情報をAIに接続して着手前に共通の全体像を作る
- 職能間の逐次調整を前倒しして並行化する

## 使いどころ

- 複数チームで開発する企業が機能提供のリードタイムを縮めたい場面
- 要件文脈が複数ツールに散らばっている組織
