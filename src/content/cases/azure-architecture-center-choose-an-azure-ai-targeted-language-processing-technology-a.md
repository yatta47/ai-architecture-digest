---
type: guidance
title: 用途別に選ぶAzure AI言語処理サービスの使い分けガイド
title_original: Choose an Azure AI targeted language processing technology
industry: cross-industry
cloud:
- azure
patterns:
- document-processing
- realtime-translation
- multilingual-localization
- rag
components:
- Azure Language
- Azure Translator
- Azure Document Intelligence
- Azure Content Understanding
- Foundry Models
- Azure AI Search
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/data-guide/ai-services/targeted-language-processing
published_at: '2026-03-24'
---

## 概要

Azure Foundry Toolsが提供する自然言語処理・翻訳・文書データ抽出などの言語処理系サービス群について、用途に応じてどれを選ぶべきかを整理したガイダンス記事。NER・感情分析・要約・質問応答を担うAzure Language、翻訳専用のAzure Translator、フォーム抽出のAzure Document Intelligence、プレビルトモデルが無い文書向けの生成AIベースのAzure Content Understandingなど、目的別の使い分け基準とMCP経由でのエージェント連携方法を示す。

## 設計のポイント

- プレビルトの文書抽出モデルがある場合はAzure Document Intelligence、無くRAG向けMarkdown出力や信頼度スコアが必要な場合はAzure Content Understandingを使い分ける。
- 翻訳タスクはAzure Language ではなく専用のAzure Translatorに任せ、Language側は文書検索やコンテンツ安全性チェックの用途には使わない。
- エージェントとAzure Language機能の連携はMCPサーバー（リモート/ローカル選択可）を介して行い、エンタープライズ向けのコンプライアンスとデータ保護を確保する。
- 医療データなどレジデンシー制約がある場合はText Analytics for HealthをDockerコンテナとして自環境やオンプレミスにホストし、PaaS利用に伴うコンプライアンス懸念を回避する。

## 使いどころ

- 意図理解に基づく応答制御が必要な会話型AIアプリを構築するチームが、Intent RoutingエージェントやExact Question Answeringエージェントの採用を検討する場面。
- プレビルトモデルが存在しない独自フォーマットの文書からスキーマ定義済みフィールドを抽出したいチームがContent Understandingを検討する場面。
- リアルタイム翻訳やカスタム用語辞書を用いたバッチ/単一ファイル翻訳が必要な多言語対応アプリケーションの開発。
- 医療機関など、データレジデンシーやコンプライアンス要件を満たしつつ電子カルテ等から医療情報を抽出したい場合。
