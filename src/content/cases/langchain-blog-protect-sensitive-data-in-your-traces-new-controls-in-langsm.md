---
type: announcement
title: LangSmithのトレース内機微データのアクセス制御
title_original: 'Protect sensitive data in your traces: new controls in LangSmith'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- guardrails
- policy-as-code
components:
- LangSmith
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/protect-sensitive-data-in-your-traces-new-controls-in-langsmith
published_at: '2026-11-17'
---

## 概要

LangSmithにトレースの入出力の閲覧制限、ユーザーグループ単位の権限管理、メタデータによるトレース単位のアクセスポリシーが追加された。エンジニアは機微な入出力を見ずにレイテンシやコストを調査できる。GDPRやHIPAAなどの要件への対応を狙う。

## 設計のポイント

- 入出力と実行ツリー・性能指標を分離し、デバッグ可視性と最小権限を両立する。
- ユーザーグループ単位でデータ権限とワークスペース所属を管理する。
- ルートrunのメタデータでトレースごとの閲覧可否を決める。

## 使いどころ

- 顧客の個人情報や医療情報を扱うエージェントを本番運用する組織。
- 開発とセキュリティ部門でトレース閲覧権限を分けたい場面。
