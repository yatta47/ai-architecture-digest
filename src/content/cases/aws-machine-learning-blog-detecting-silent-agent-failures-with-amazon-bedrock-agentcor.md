---
type: guidance
title: Bedrock AgentCoreによるサイレントなエージェント失敗の検知と根本原因分析
title_original: Detecting silent agent failures with Amazon Bedrock AgentCore optimization
industry: cross-industry
cloud:
- aws
patterns:
- eval
- root-cause-analysis
- ai-agent
- llmops
components:
- Amazon Bedrock AgentCore
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/detecting-silent-agent-failures-with-amazon-bedrock-agentcore-optimization/
published_at: '2026-07-23'
---

## 概要

Amazon Bedrock AgentCore optimizationの「insights」機能は、成功したように見えて実際は誤動作しているAIエージェントの「サイレント障害」を、既存のトレースデータから検出する。失敗パターンのクラスタリングと根本原因分析、ユーザー意図分析、実行分析の3つの観点で、数百セッションにまたがる挙動パターンをランク付けして提示し、優先順位付けした改善を可能にする。

## 設計のポイント

- トレースをスパングラフとして表現し、失敗に無関係な分岐を刈り込むことでRCAを長いセッションでも実用的にする
- 失敗を11カテゴリの振る舞い分類に対してクラスタリングし、影響セッション数で優先度をランク付けする
- 2階層クラスタ構造(大分類→サブパターン)で、最も効果の大きい単一の修正を特定できるようにする
- エラーシグナルに依存せず、ポリシー適合性や振る舞いの妥当性を推論して失敗を検知する

## 使いどころ

- ダッシュボードは正常なのに顧客からの不具合報告が続くAIエージェント運用チーム
- 数百〜数千セッション規模のトレースを手作業でレビューしきれない大規模エージェント運用
- 本番エージェントの実際の利用意図と設計意図のギャップを把握したいプロダクトチーム
