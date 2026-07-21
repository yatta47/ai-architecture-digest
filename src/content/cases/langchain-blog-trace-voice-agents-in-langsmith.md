---
type: announcement
title: コストセンター単位でAIクレジットを管理できるGitHub Copilot課金機能
title_original: AI credit pools for cost centers in the billing UI
company: GitHub
industry: cross-industry
cloud: []
patterns:
- cost-optimization
components:
- GitHub Copilot
- GitHub billing UI
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/trace-voice-agents-in-langsmith
published_at: '2026-07-21'
---

## 概要

GitHubは、コストセンターごとのAIクレジットプールをREST APIだけでなく課金画面上から直接設定できるようにした。プールの上限はそのコストセンターに割り当てられたCopilotライセンス数から自動計算され、上限到達時に利用をブロックするか追加課金として継続するかを選択できる。

## 設計のポイント

- プール上限はライセンス数から自動算出され手動設定が不要なため、ライセンス増減に追従して上限がずれる心配がない。
- コストセンター予算(メータード課金の上限)とAIクレジットプール(組み込みクレジットの上限)を別軸で併用できる。

## 使いどころ

- 部門・チームごとにAI利用コストを配分し、予算超過を防ぎたいEnterprise/Business管理者。
