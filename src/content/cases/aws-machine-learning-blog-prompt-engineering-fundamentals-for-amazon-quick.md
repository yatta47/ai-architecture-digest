---
type: guidance
title: Amazon Quick向けプロンプト設計の基本原則とCRISPE
title_original: Prompt engineering fundamentals for Amazon Quick
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- context-engineering
- prompt-optimization
components:
- Amazon Quick
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/prompt-engineering-fundamentals-for-amazon-quick/
published_at: '2026-09-29'
---

## 概要

Amazon Quickの各AI機能で安定した出力を得るためのプロンプト設計の基本を整理したシリーズ第1回。具体性・文脈・few-shot例示の3原則と、複雑な依頼向けの構造化フレームワークCRISPEを紹介する。

## 設計のポイント

- 曖昧な依頼を避け、指標・期間・範囲・分析種別を明示してAIの暗黙の仮定を減らす。
- 利用者や意思決定の文脈を渡し、出力の深さや形式をAIに調整させる。
- 出力形式は説明よりfew-shotの実例で示し、初回精度を上げる。
- CRISPEでコンテキスト・役割・意図・手順・提示形式・評価基準を漏れなく構造化する。

## 使いどころ

- Quickのカスタムエージェントや会話型分析を業務で使い始めるチーム。
- チーム共通のプロンプト語彙・テンプレートを整備したい組織。
- 四半期レポートなど定型分析の再現性を高めたい担当者。
