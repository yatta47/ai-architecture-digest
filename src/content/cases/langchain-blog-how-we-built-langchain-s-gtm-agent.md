---
type: case
title: Deep Agentsで作るLangChain社内のGTM(営業支援)エージェント
title_original: How we built LangChain's GTM Agent
company: LangChain
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- human-in-the-loop
- decision-execution
components:
- Deep Agents
- LangSmith
- Salesforce
- BigQuery
outcome:
  type: revenue
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-we-built-langchains-gtm-agent
published_at: '2026-06-15'
---

## 概要

LangChainは、Salesforceの新規リードをトリガーに接触要否を判断し、複数ソースから文脈を集めてSlackに下書きメールを提示するGTMエージェントをDeep Agents上に構築した。過去のやり取り確認や関係性に応じた文面調整、担当者の承認を必須とするhuman-in-the-loopを組み込み、リードから商談化までの転換率を250%向上、月間40時間の営業担当の工数削減を実現した。

## 設計のポイント

- エージェントに送信可否を自己判断させ、既に連絡済みのリードやサポート対応中の顧客には自動送信しない安全側の判断を優先させる
- 人間の承認なしにメールを送信しない human-in-the-loop を非交渉の要件とし、承認・編集・却下をSlack上で完結させる
- 顧客の状態（既存顧客/温かい見込み客/コールド）ごとに異なるプレイブック(スキル)を切り替えて文面を生成する
- 全ての担当者アクション(送信/編集/取消)をLangSmithのトレースに紐づけて記録し、品質評価とリグレッション検知に使う

## 使いどころ

- アウトバウンド調査や下書き作成にかかる営業担当の工数を削減したいSDR/営業チーム
- 商談化率や案件の優先度付けをデータドリブンに改善したいGTMチーム
