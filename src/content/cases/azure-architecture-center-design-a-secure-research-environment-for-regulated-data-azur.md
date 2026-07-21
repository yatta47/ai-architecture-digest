---
type: guidance
title: 規制データを扱う研究者向けに、Azure Virtual Desktopをジャンプボックスとした安全な機械学習研究環境を設計する
title_original: Design a secure research environment for regulated data
industry: cross-industry
cloud:
- azure
patterns:
- human-in-the-loop
- guardrails
- policy-as-code
components:
- Azure Machine Learning
- Microsoft Fabric Data Science
- Azure Blob Storage
- Azure Virtual Desktop
- Microsoft Purview
- Azure Key Vault
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/secure-compute-for-research
published_at: '2026-06-19'
---

## 概要

規制コンプライアンスが求められる機微データを扱う研究環境として、Azure Machine LearningのマネージドコンピュートとMicrosoft Fabric Data Science、プライベートBlob Storage、特権ジャンプボックスとしてのAzure Virtual Desktopを組み合わせた構成を解説する。マネージド仮想ネットワークとプライベートエンドポイントによりコンピュートとストレージへの通信を完全に内部化し、パブリックIPを一切使わずにデータの持ち出しを承認ワークフロー経由で統制する。

## 設計のポイント

- 取り込み用ストレージから非公開ストレージへコピー後に元データを削除することで、データセットをイミュータブルにし不用意な再アクセスを防ぐ。
- Azure Virtual Desktopで条件付きアクセス・多要素認証・特権ID管理・コピー&ペースト禁止などのDLP制御を課し、研究者のアクセスを監査可能なセッション単位に閉じ込める。
- 非識別化されたモデル・データのエクスポートには人間による承認ワークフローを挟み、Responsible AIダッシュボードで公平性・解釈性を評価してから外部へ出す。

## 使いどころ

- 医療・金融など機微データを扱う研究プロジェクトで、コンプライアンス要件を満たしたAI/ML研究基盤を構築したい組織。
- 研究者の端末に機微データを一切残さず、特権アクセス管理下でモデル開発を行いたいセキュリティ担当チーム。
- モデルやデータのエクスポート前に人手によるレビューを必須にしたい、監査要件の厳しい業界。
