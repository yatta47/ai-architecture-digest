---
type: guidance
title: ビルド・テスト・レビューを通過してもAI生成コードを信頼できるとは限らない理由
title_original: Why AI-generated code is easy but engineering trust is hard
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- eval
components: []
outcome:
  type: quality
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/why-ai-generated-code-is-easy-but-engineering-trust-is-hard/
published_at: '2026-08-20'
---

## 概要

ビルド成功・全テストgreen・レビュー通過という従来の合格基準をすべて満たしても、エージェントが曖昧な要件を誤解釈したまま一貫した実装を積み上げてしまう場合がある。AIを使ったモバイルアプリデザイナー開発で直面したこの問題から、SalesforceはAI生成コードの信頼性をどこで検証すべきかを論じる。

## 設計のポイント

- テスト・ビルド・レビューがいずれも『実装が要件の意図通りである』ことまでは検証していない点をリスクとして認識する
- エージェントが下した暗黙の設計判断（既存ユーティリティを使わない、リポジトリ固有の規約を破る等）を可視化する仕組みが必要になる
- 要件からコードへの経路が複数存在しうる前提に立ち、経路の途中にある解釈の分岐点を検証対象に含める

## 使いどころ

- AIコーディングエージェントの出力を大規模に本番投入する前にレビュー体制を見直したい開発組織
- テストとレビューが通っているにもかかわらず後工程で要件誤解が発覚した経験がある場合
- エージェントの意思決定プロセスに対する説明可能性・検証可能性を高めたいプラットフォームチーム
