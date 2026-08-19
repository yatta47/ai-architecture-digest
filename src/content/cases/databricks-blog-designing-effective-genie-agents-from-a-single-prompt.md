---
type: guidance
title: 単一プロンプトからUnity Catalogに基づくドメイン特化エージェントを作る
title_original: Designing effective Genie Agents from a single prompt
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- rag
- eval
components:
- Databricks Genie Agents
- Unity Catalog
- Genie One
- Genie Code
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/designing-effective-genie-agents-single-prompt
published_at: '2026-08-19'
---

## 概要

Databricks Genie Agentsは、Unity Catalogでガバナンスされた構造化データや文書・ファイルを根拠に、単一プロンプトからドメイン特化エージェントを生成できる機能。回答の弱さの多くはプロンプトではなく業務コンテキスト不足に起因するとして、まず狭いユースケースで組成しベンチマークで検証してから知識やツールを拡張していくアプローチを推奨している。

## 設計のポイント

- 曖昧なプロンプト調整ではなく、Unity Catalogで統治された信頼できるデータ・ドキュメントの整備に投資することで回答精度を上げる
- 最初は範囲を絞った1つの業務課題から始め、根拠となるソースの妥当性を検証しやすくしてから段階的に拡張する
- 組み込みベンチマーク機能で期待回答付きテスト問題を定義し、変更のたびに精度スコアで効果を定量比較する

## 使いどころ

- 営業パイプラインリスクの把握や物流遅延の検知など、繰り返し発生する定型分析業務を持つ部門
- 既にUnity Catalogでデータやドキュメントをガバナンスしている組織がセルフサービスAI活用を広げたい場面
- IT・データ部門がドメインエージェントの品質を継続的にベンチマークし改善したい場合
