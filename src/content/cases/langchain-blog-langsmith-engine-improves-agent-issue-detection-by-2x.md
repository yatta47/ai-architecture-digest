---
type: case
title: 本番エージェントのトレースを自動診断し修正案まで出すLangSmith Engine
title_original: 'New in LangSmith Engine: >2x better issue detection'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- root-cause-analysis
- eval
components:
- LangSmith
- LangSmith Engine
- Slack
- Linear
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/new-in-langsmith-engine-2x-better-issue-detection
published_at: '2026-08-25'
---

## 概要

LangSmith Engineは本番エージェントのトレースを自動解析し、問題の診断・根本原因・修正案（レビュー可能なPR）・検証用データセット・継続的な回帰監視までを自動生成するin-platformのDeep Agent。5月の提供開始から6000万件超のトレースを走査し2万件超の問題を検出、最新リリースで内部ベンチマークの問題検出精度が2倍、業界標準ベンチマークでの修正精度が25%向上した。

## 設計のポイント

- トレース解析から診断・修正提案・検証データセット生成・継続監視までをエージェント改善ライフサイクル全体を担う単一のDeep Agentに集約する
- セルフホスト環境ではオーケストレーションを顧客のVPC内で実行し、推論のみゼロデータ保持のマネージドサービスに委ねてセキュリティ要件と性能を両立させる
- コスト重視のチーム向けに走査トレース数を絞るReduced Analysisモードを用意し、精度とコストのトレードオフを選べるようにする

## 使いどころ

- 数千万件規模の本番トレースから手作業では追いきれない不具合を継続的に検出したいエージェント運用チーム
- SlackやLinearなど既存のインシデント対応フローにエージェントの不具合検知・トリアージを統合したいチーム
