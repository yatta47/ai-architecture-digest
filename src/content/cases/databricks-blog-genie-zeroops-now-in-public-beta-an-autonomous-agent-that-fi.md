---
type: announcement
title: Genie ZeroOpsがパブリックベータ：データパイプライン障害を自律解決
title_original: 'Genie ZeroOps now in public beta: an autonomous agent that fixes data pipelines'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- root-cause-analysis
- human-in-the-loop
components:
- Genie ZeroOps
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/genie-zeroops-now-public-beta-autonomous-agent-fixes-data-pipelines-lessons-80000-customer
published_at: '2026-11-19'
---

## 概要

Genie ZeroOpsは、データパイプラインの障害を検出・調査・解決するエージェントで、Unity Catalogとリネージを使って原因を特定しPR作成まで進める。共有、通知、ワンクリックPR、業務ルール追加が加わった。

## 設計のポイント

- Unity Catalogのメタデータとリネージを根拠に調査する。
- 修正はPRとして提示し、人が確認する。
- 業務固有の指示を追加できる。

## 使いどころ

- 多数のパイプラインを運用し、調査の人手負担を減らしたいデータエンジニアリングチームに向く。
