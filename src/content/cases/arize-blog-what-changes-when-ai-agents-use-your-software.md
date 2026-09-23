---
type: opinion
title: エージェントが使うソフトウェアを作る際の権限委譲とツール設計の論点
title_original: What changes when AI agents use your software
company: Daytona
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- defense-in-depth
components:
- Daytona
- OAuth Token Exchange
- Arize AX
outcome:
  type: risk-compliance
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/building-tools-for-ai-agents/
published_at: '2026-09-23'
---

## 概要

Daytona共同創業者へのインタビューを基に、エージェントが利用者と別のアイデンティティで動くべきことと、ツールにアクセスできず失敗する問題を論じる。委譲アクセスの表現にはOAuthトークン交換などがあり、認可はエージェントではなくサービス側で強制すべきだとする。

## 設計のポイント

- 利用者の権限を代理する主体と操作対象を区別し、モデルが広い範囲を要求しても境界を維持している。
- 認証情報はモデルのコンテキストの外の信頼済み統合コードに持たせ、許可された操作だけを公開する。
- エージェントが実際の顧客タスクを与えられた権限と時間で完了できるかを製品チームが検証する。

## 使いどころ

- エージェント向けAPIや連携を整備するプロダクトチーム。
- エージェントの認可モデルを設計するセキュリティ担当者。
- サンドボックスとハーネスを組むエンジニア。
