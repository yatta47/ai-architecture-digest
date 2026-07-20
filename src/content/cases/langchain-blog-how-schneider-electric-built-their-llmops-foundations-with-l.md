---
type: case
title: Schneider ElectricのLLMOps基盤構築（LangSmith活用）
title_original: How Schneider Electric Built Their LLMOps Foundations At Enterprise Scale With LangSmith
company: Schneider Electric
industry: manufacturing
cloud:
- aws
- azure
- multi-cloud
patterns:
- llmops
- eval
- human-in-the-loop
- ai-agent
components:
- LangSmith
- AWS EKS
- LangSmith SDK
- One Jo
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-schneider-electric-built-their-llmops-foundations-at-enterprise-scale-with-langsmith
published_at: '2026-07-08'
---

## 概要

Schneider Electricは160,000人の従業員と40億ユーロ超の売上を持つエネルギー技術企業で、社内AI Hubの350人の専門家が60以上のエージェントを本番展開している。同社はLangSmithをAWS EKS上にセルフホストし、AI製品単位でワークスペースを構成して本番トレースを開発用データセットへ還元するループを構築、オフライン評価テンプレートとLLMOps成熟度フレームワークにより、160,000人が利用する社内AIアシスタント「One Jo」をはじめとする60以上のAI製品の品質と精度を継続的に検証・改善している。

## 設計のポイント

- ワークスペースを環境単位ではなくAI製品単位（dev〜prodを横断）で構成し、本番トレースを開発データセットへ還元するループを成立させる
- LangSmithを自社セキュリティ境界内のAWS EKS上にセルフホストし、サードパーティへのデータ越境を防いでコンプライアンス要件を満たす
- GitHubテンプレートと評価CLIによるオフライン評価アクセラレータで、全AIスクワッドの実験手法（データセット規約・評価インターフェース）を標準化する
- LLMOps成熟度モデルを策定し、トレーシング・オフライン評価・オンライン評価・フィードバック活用の状況をプロダクトライフサイクルのゲートレビューに組み込む

## 使いどころ

- 数十万人規模の従業員向け社内AIアシスタントの継続的な品質改善
- 60以上のAIプロダクトを横断してLLMOps導入状況を可視化・統制したい大企業
- 重要インフラなどデータ主権とセキュリティ要件が厳しい領域でAIエージェントを展開したい企業
