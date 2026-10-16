---
type: case
title: npmマルウェアのLLM判定にバイナリ解析の知識を注入
title_original: 'Closing the Binary Blind Spot: Domain Knowledge Injection for LLM Malware Triage of npm Packages'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- context-engineering
- eval
- guardrails
components:
- YARA
- Semgrep
- npm
- OSV
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/closing-binary-blind-spot-domain-knowledge-injection-llm-malware-triage-npm-packages
published_at: '2026-10-16'
---

## 概要

npmレジストリを監視するスキャナで、バイナリを含むパッケージはLLMが決定的な判定に至らない率が高い（14.4%対6.2%）。静的解析の証拠を推論前にプロンプトへ入れることで、安価なモデルから最先端モデルまで検出品質を改善した。

## 設計のポイント

- 再学習が要らず閉じたホスト型モデルにも使えるよう、専門知識を推論時の事前計算済み証拠として渡す。
- YARAやSemgrepなどの静的解析を先に走らせ、LLMには構造化プロンプトで判定させる。
- 難読化度の異なる攻撃ペイロードで失敗の傾向を測り、系統的な弱点を特定する。

## 使いどころ

- サプライチェーン攻撃の検知にLLMを使うセキュリティチーム。
- ドメイン知識の注入でモデル精度を上げたい場面。
