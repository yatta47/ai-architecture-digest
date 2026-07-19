---
type: case
title: 神経多様性を持つソリューションアーキテクトが構築した個人用AIワークフロー
title_original: When your brain works differently, AI isn't a luxury—it's accessibility
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
- memory-consolidation
components:
- Amazon Quick
- Amazon Bedrock
- Model Context Protocol
- Kiro
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/when-your-brain-works-differently-ai-isnt-a-luxury-its-accessibility/
published_at: '2026-07-13'
---

## 概要

AuDHD(自閉症とADHDの併発)を持つソリューションアーキテクトが、Amazon Quick on your desktopとAmazon Bedrockを基盤にメールトリアージやタスク優先度判断を自動化する個人用AIワークフローを構築し、実行機能(executive function)の不足を補った体験記。

## 設計のポイント

- トリアージ・優先度判断のルールをMarkdownファイルとして外出しし、AIが毎セッション読み込むことで、ルール変更時に再デプロイなしで即座に挙動が変わるようにする。
- 「今すぐ着手すべき」条件などを明示的なルールとしてハードコードし、優先順位付けという実行機能の欠如をシステム側で補う。
- 決定的に動く反復自動化(メール整形・終業サマリなど)をskillsとして分離し、認知的な判断コストをほぼゼロに近づける。

## 使いどころ

- 実行機能(優先順位付け・時間管理・タスク切り替え)に困難を抱える神経多様な働き手。
- 毎朝のメールトリアージや優先度判断にかかる認知負荷を下げたいあらゆる知識労働者。
