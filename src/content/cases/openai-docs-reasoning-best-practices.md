---
type: guidance
title: 推論モデル(プランナー)とGPTモデル(ワークホース)の使い分けベストプラクティス
title_original: Reasoning best practices
industry: cross-industry
cloud: []
patterns:
- reasoning-computation-separation
components:
- o3
- o4-mini
- GPT-4.1
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/reasoning-best-practices
published_at: '2025-08-03'
---

## 概要

複雑な問題を長く深く考えるo系推論モデル(プランナー)と、低レイテンシ・低コストで実行するGPTモデル(ワークホース)は得意分野が異なるという前提のもと、両者をどう組み合わせて使うべきかのベストプラクティスを解説する。

## 設計のポイント

- 推論モデルで戦略・計画を立て、GPTモデルで個々のタスクを実行するという2段構成のパイプラインを基本形とする
- 速度・コストを優先するか、数学・科学・法務のような高精度な意思決定を優先するかで、モデル系統を明確に切り分ける

## 使いどころ

- コスト効率と精度のバランスを取りたいエンドユーザー向けアプリケーション
- 金融・法務・エンジニアリングなど専門家的判断が必要な複雑タスクを自動化したいチーム
