---
type: guidance
title: 1チーム1ドメインから始めるGenie（データエージェント）全社展開プレイブック
title_original: 'How to roll out Genie One: a step-by-step enterprise playbook'
industry: cross-industry
cloud:
- multi-cloud
patterns:
- text-to-sql
- ai-agent
- context-engineering
components:
- Genie One
- Genie Agents
- Genie Ontology
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-roll-out-genie-one-step-step-enterprise-playbook
published_at: '2026-09-28'
---

## 概要

Databricksは、業務ユーザー向けAIコワーカー『Genie One』の全社展開を、1チーム・1データドメインの小さなパイロットから段階的に広げる手順として提示する。Unity Catalogによるガバナンスを基盤に、ドメイン・メトリックビュー・Pagesという順序でセマンティックレイヤーを整備し、実際の質問セットでGenieの回答をスコアリングしてから次のチームへ拡大する。

## 設計のポイント

- ドメイン→メトリックビュー→Pagesの順でセマンティックレイヤーを整備し、Pagesがドメインに属する制約から着手順序を固定する。
- 展開前に25〜50件の実際の質問と正解を文書化し、セマンティック変更のたびにGenieの回答をこの基準でスコアリングして精度劣化を検知する。
- Unity Catalogで権限・マスキング・リネージ・監査をクエリ時に強制し、Genie Ontologyでサードパーティアプリへも権限を拡張する。

## 使いどころ

- パイプライン健全性確認など、特定業務チームの反復的な問い合わせ対応を自然言語AIコワーカーに任せたい場合。
- AI導入を一気に全社展開して信頼を失う前に、少人数パイロットで精度を検証してから拡大したい組織。
