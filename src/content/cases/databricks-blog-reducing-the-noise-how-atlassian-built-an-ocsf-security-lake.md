---
type: case
title: AtlassianのOCSFセキュリティレイクハウス
title_original: 'Reducing the Noise: How Atlassian Built an OCSF Security Lakehouse on Databricks'
company: Atlassian
industry: other
cloud: []
patterns:
- data-federation
- ai-agent
- unified-runtime
components:
- Databricks
- OCSF
- Delta Lake
- Photon
- Go
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/reducing-noise-how-atlassian-built-ocsf-security-lakehouse-databricks
published_at: '2026-10-15'
---

## 概要

Atlassianは1日440億件のセキュリティログをOCSFに統一してレイクハウスに集め、取り込みコストを80%削減した。スキーマをGoの型に埋め込み、変換を自動化するエージェントの幻覚とトークン使用量も減らした。

## 設計のポイント

- スキーマを型として埋め込み、コンパイル時に正しさを保証する。
- ELTでなくETLで転送中に変換し、リアルタイム検知とベンダー非依存を保つ。
- 手作業の変換工程を自動化し、アナリストが使えるセルフサービスにする。

## 使いどころ

- ログ形式がばらばらなセキュリティ運用チーム。
- 変換エージェントの出力を型で制約したい場面。
