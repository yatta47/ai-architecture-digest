---
type: guidance
title: LangSmithとLangChain OSSで実現するEU AI Act高リスクAIシステム対応
title_original: How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- human-in-the-loop
components:
- LangSmith
- LangGraph
- LangSmith Studio
- LangSmith Insights Agent
- LangSmith Deployment
- LangSmith EU
- PagerDuty
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act
published_at: '2026-06-25'
---

## 概要

LangChainが、EU AI Actの高リスクAIシステム要件(リスク管理・自動ロギング・透明性・人間による監督・市販後監視)を、自社製品のLangSmithとLangChain OSS(LangGraph)の機能でどう満たせるかを解説する記事。トレーシング、継続的評価、Human-in-the-Loopの3本柱で、Article 9/10/12/13/14/15といった各条文に対応する具体的な機能をマッピングしている。2026年8月2日の適用開始を控え、金融・医療・HR・製造・重要インフラなど高リスク分野のチームに向けた実務ガイドとなっている。

## 設計のポイント

- エージェントの全実行(LLM呼び出し・ツール呼び出し・推論過程)を入力/出力/タイムスタンプ付きでトレースし、Article 12が求める自動イベントロギングを満たす。
- 本番トラフィックの一部を対象にオンライン評価者(バイアス・毒性・PII漏洩・プロンプトインジェクションなど)を継続実行し、閾値超過時にPagerDutyやWebhookでアラートする仕組みを組み込む。
- LangGraphのinterruptプリミティブでエージェントグラフに人間介入ポイントを組み込み、実行の一時停止・状態確認/修正・再開(exactly-once実行の耐久ランタイム)を可能にする。
- セルフホスト/BYOC/マネージドクラウド(EUリージョン限定のLangSmith EUを含む)の複数デプロイ形態を用意し、ログの保存場所とトレース保持期間(base 14日/extended 400日)を選べるようにしてデータレジデンシー要件に対応する。

## 使いどころ

- 与信スコアリング・医療機器・採用・重要インフラなど高リスクAIシステムを構築し、2026年8月2日のEU AI Act適用期限までにコンプライアンス基盤を整備する必要があるチーム。
- マルチステップで推論・ツール呼び出しを行うエージェントの意思決定過程を可視化し、規制当局や導入先(deployer)への説明責任(Article 13)を果たしたい場合。
- エージェントの誤りが連鎖する前に人間が介入・是正できる仕組み(Article 14)を実行グラフ自体に組み込みたい開発チーム。
- 本番運用中のAIシステムに対して継続的な精度・バイアス・敵対的耐性の監視(Article 10/15)と市販後モニタリングの証跡を残したい場合。
