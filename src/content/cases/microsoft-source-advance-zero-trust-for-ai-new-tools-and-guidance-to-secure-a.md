---
type: announcement
title: Zero Trust for AI戦略を実装レベルへ、AI向け評価チェックとDevSecOpsピラーを追加
title_original: 'Advance Zero Trust for AI: New tools and guidance to secure AI agents and DevSecOps'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- guardrails
- defense-in-depth
components:
- Zero Trust Assessment
- Zero Trust Workshop
- Microsoft AI Memory
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/security/blog/2026/08/04/advance-zero-trust-for-ai-new-tools-and-guidance-to-secure-ai-agents-and-devsecops/
published_at: '2026-08-05'
---

## 概要

MicrosoftはZero Trust for AI戦略の実装フェーズとして、AI・SecOps・インフラ向けの評価チェックを追加したZero Trust Assessmentと、ソースコードからデプロイまでを対象とする15コントロールグループ・91タスクのDevSecOpsピラーをZero Trust Workshopに新設した。あわせてAIメモリをガバナンス対象の境界として扱うためのMicrosoft AI Memoryフレームワークに基づくガイダンスと、自律・エージェント型システム向けの実践ガイドブックを公開している。

## 設計のポイント

- 『検証してから信頼する・最小権限・侵害を前提にする』というZero Trustの3原則を、AI開発パイプライン（ソース・CI/CD・依存関係・IaC）に対する具体的なコントロールへ翻訳する
- アセスメントで現状のリスクを測定し、ワークショップのFirst/Then/Nextフェーズでロードマップ化するという、測定から実行計画への一連の型を用意する
- AIエージェントのメモリを『ただのキャッシュ』ではなく、意図・来歴・ライフサイクル可視性・ユーザー制御を伴うガバナンス対象の境界として扱う
- コード生成・パッケージ推薦・IaC自動生成などAIアシスト開発が広げる攻撃面に対し、コードガバナンス・ツール許可リスト・サプライチェーン保護を専用タスクとして切り出す

## 使いどころ

- AIエージェントやコーディングアシスタントの全社導入に伴うリスクを、既存のZero Trust運用の枠組みで測定・優先順位付けしたいセキュリティ部門として
- AI支援開発によって広がった攻撃面（依存関係・サプライチェーン・IaC）を、DevSecOpsとして体系的に統制したいプラットフォームチームとして
- エージェントのメモリを新たなガバナンス境界として位置づけ、来歴やライフサイクルを管理したい場合として
