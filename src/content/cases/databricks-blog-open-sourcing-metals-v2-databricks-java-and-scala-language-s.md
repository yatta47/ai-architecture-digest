---
type: case
title: エージェント時代のコード把握を高速化するJava/Scala言語サーバー刷新(Metals v2)
title_original: 'Open Sourcing Metals v2: Databricks'' Java and Scala Language Server for Multi-Million-Line Codebases'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Metals
- Cursor
- VS Code
- Neovim
- IntelliJ
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/open-sourcing-metals-v2-databricks-java-and-scala-language-server-multi-million-line-codebases
published_at: '2026-08-11'
---

## 概要

Databricksは、コードの大半がエージェントによって書かれる時代には網羅的な補完よりも起動の速さとコードベース把握が重要だと考え、Scala言語サーバーMetalsをフォークしてJavaへの本格対応と2600万行モノレポ規模への再設計を行った。ContentのCursor週次利用率は12%だったIntelliJに対し92%まで伸び、成果はMetals v2としてOSS化されStripeなど社外にも波及している。

## 設計のポイント

- エージェントがコードの大半を書く前提で、網羅的な補完・リファクタリングよりも起動の速さと信頼できるコードベース把握を優先し、TTII(初回インテリジェンスまでの時間)を主要指標に据えた。
- モノレポ規模(2600万行)向けにMetals v1をフォーク・再設計し、ソースパス提供の仕組みからJava/Scalaのナビゲーションを再構築した。
- 社内標準化にとどめず上流のMetalsメンテナや協力エディタベンダーと協業してOSS化し、他社でも同じパターンを再現できるようにした。

## 使いどころ

- AIコーディングエージェントの利用が増え、エンジニアが手動編集する場面で軽量エディタでの高速なコードベース把握を重視したいチーム。
- 数百万〜数千万行規模のJava/Scalaモノレポで、既存のJVM言語サーバーがスケールせず困っているプラットフォームチーム。
- IntelliJ中心のツール投資を、Cursor/VS Code/Neovimなど軽量エディタとエージェントの組み合わせへ移行したい組織。
