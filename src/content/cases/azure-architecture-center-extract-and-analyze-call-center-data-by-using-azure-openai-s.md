---
type: guidance
title: 通話録音をAzure OpenAIでバッチ分析するコールセンター後処理アーキテクチャ
title_original: Extract and analyze call center data
industry: cross-industry
cloud:
- azure
patterns:
- document-processing
- guardrails
- event-driven
components:
- Azure Blob Storage
- Azure Speech
- Azure OpenAI
- Azure Language
- Power BI
- Foundry Tools
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/openai/architecture/call-center-openai-analytics
published_at: '2026-04-30'
---

## 概要

コールセンターの通話録音をAzure Blob Storageに保存し、Azure Speechでバッチ書き起こし、Azure Languageで個人情報を検出・匿名化したうえでAzure OpenAI(GPT-5系モデル)に渡して意図・感情分析やエンティティ抽出、要約を行うバッチ処理アーキテクチャ。処理結果はPower BIやCRMに連携し、オペレーターの対応品質向上や顧客満足度改善に活用する。

## 設計のポイント

- リアルタイムではなく通話終了後のバッチ処理として設計し、コストと処理負荷を抑えつつ意図・感情・要約などの分析を行う
- LLMに渡す前にAzure Languageで個人情報を検出・削除(redaction)し、プライバシーを保護してから分析に回す
- Timer triggerとBlob triggerを使い分け、蓄積バッチ処理とアップロード即時処理の両方に対応できるようにする

## 使いどころ

- コールセンターの通話履歴から傾向分析やオペレーター支援情報を自動生成したい場合
- 個人情報を含む音声データを安全にLLM分析へ回したい場合
