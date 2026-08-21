---
type: guidance
title: AIエージェントスタックにおけるセキュリティ制御の置きどころ
title_original: Where Security Fits in an AI Agent Stack
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- guardrails
- defense-in-depth
- policy-as-code
components:
- NVIDIA OpenShell
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/where-security-fits-in-an-ai-agent-stack/
published_at: '2026-08-21'
---

## 概要

創造的な問題解決能力を持つエージェントが意図した制約を回避しうる事例が増える中、モデル・ハーネス・メタハーネス・セキュアランタイム・推論基盤という階層構造でエージェントスタックを整理し、セキュリティ制御は書き換え可能なハーネスロジックではなくランタイム／インフラ層で強制すべきだと提案する。

## 設計のポイント

- エージェントが自分自身に権限を付与したり制御を回避したりできないよう、制御はエージェント境界より下のレイヤーで一元的に強制する
- 最小権限・分離・ジャストインタイムアクセス・権威あるポリシー強制という原則をランタイム層に実装する
- 影響のある全アクションを一貫して評価・監査可能にすることで、ハーネスロジックの書き換えに依存しない安全性を担保する

## 使いどころ

- 長期タスクを自律実行するエージェントに権限管理・監査の仕組みを組み込みたい開発チーム
- エージェントのセキュリティ境界をどのレイヤーに実装すべきか設計判断を迫られているアーキテクト
- OSSやパートナーエコシステムを含む複数フレームワークで一貫したセキュリティモデルを適用したい組織
