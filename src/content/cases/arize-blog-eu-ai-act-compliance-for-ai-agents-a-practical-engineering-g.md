---
type: guidance
title: EU AI法対応をAgentのトレースと評価で実装する手引き
title_original: 'EU AI Act compliance for AI agents: a practical engineering guide'
company: Arize
industry: financial-services
cloud: []
patterns:
- eval
- human-in-the-loop
- policy-as-code
components:
- Arize AX
- Arize Phoenix
- evroc
outcome:
  type: risk-compliance
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/eu-ai-act-compliance-ai-agents/
published_at: '2026-10-13'
---

## 概要

EU AI法の高リスク要件(自動ログ、保存、人による監督、市販後監視)をエンジニアリング作業として整理し、evrocのEU内インフラとPhoenix/AXによるトレース・評価で証跡を作る方法を説明する。

## 設計のポイント

- ログの完全性・保持・プライバシーを最初のトレースから設計する。
- データの所在と管理主体を明確にする。
- オンライン評価と人間レビュー記録を証跡にする。

## 使いどころ

- 与信やCV審査等の高リスク用途にエージェントを使う組織。
