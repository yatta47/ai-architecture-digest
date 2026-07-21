---
type: guidance
title: エージェントにコードを書かせて実行させるためのサンドボックス選定ガイド
title_original: How to Choose the Right Sandbox for Your Agent
company: LangChain
industry: cross-industry
cloud: []
patterns:
- guardrails
- defense-in-depth
components:
- LangSmith Sandboxes
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-choose-the-right-sandbox-for-your-agent
published_at: '2026-06-15'
---

## 概要

機密データへのアクセス・信頼できない外部コンテンツへの露出・外部通信能力が揃う『Lethal Trifecta』が成立するとプロンプトインジェクションでデータ漏洩が起きうるため、AIエージェントにコード実行を許す際はサンドボックスでリスクを縮小すべきだと解説する。分離ファイルシステム・限定ネットワークアクセス・リソース制限・再利用制御・カーネルレベル分離（microVM）という5要件を満たすサンドボックスとして、LangSmith Sandboxesの設計思想を紹介している。

## 設計のポイント

- 機密データアクセス・信頼できない入力・外部通信能力の3条件が揃う『Lethal Trifecta』が成立するかを起点にリスクを評価する
- サンドボックスにはエージェントが必要とするデータだけを置く分離ファイルシステムと、送信先を絞る限定ネットワークアクセスを組み合わせる
- コンテナレベルの分離では不十分な場合があるため、microVMなどによるカーネルレベルの分離で侵害の影響範囲を機械単位に留める
- サンドボックスの再利用は状態を持ち越せる利便性と、侵害が持続するリスクのトレードオフとして明示的に選択できるようにする

## 使いどころ

- エージェントに任意のコードを書かせて実行させたいが、プロンプトインジェクションのリスクを抑えたいチーム
- 外部MCPサーバーやサードパーティ製スキルなど信頼できないコンテンツをエージェントに読ませる可能性があるプロダクト
