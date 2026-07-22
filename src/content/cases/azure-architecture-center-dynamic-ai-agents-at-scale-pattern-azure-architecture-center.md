---
type: guidance
title: 数百規模のAIエージェントを動的選択するマルチエージェント基盤パターン
title_original: Dynamic AI agents at scale pattern
industry: cross-industry
cloud:
- azure
patterns:
- multi-agent-orchestration
- ai-agent
- rag
components:
- Microsoft Foundry
- Azure AI Search
- Azure OpenAI
- Azure Managed Redis
- Azure Monitor
- Application Insights
- Azure NAT Gateway
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/ai-agents-at-scale
published_at: '2026-05-28'
---

## 概要

Azure上で数百規模のAIエージェントを動的に選択・起動するマルチエージェント基盤のソリューションパターン。ユーザークエリに対してAI Searchのセマンティックキャッシュでベクトル類似度から候補エージェントを絞り込み、信頼度が閾値未満ならLLMが候補から選択し、エージェントファクトリが実装をインスタンス化する。Redisで会話コンテキストを保持し、Application InsightsとAzure Monitorで全体を可観測にする。

## 設計のポイント

- エージェント選択をベクトル類似度による候補絞り込みと信頼度スコアでのフィルタリングの2段階にし、閾値を超えたら直接呼び出し、超えなければLLMに選ばせることでレイテンシとコストを両立する
- エージェント実装をコードモジュールやYAMLテンプレートなど複数形式で登録し、エージェントファクトリが動的にインスタンス化することでエージェント追加を疎結合にする
- 会話コンテキストと履歴をRedisに保存してマルチターンのやり取りを低レイテンシで維持する
- OpenTelemetry経由の全コンポーネント計装とログ分析でエージェント単位・会話単位の異常を検知できるようにする

## 使いどころ

- 会話ドメインを事前に予測できないオープンエンドな問い合わせに、多数のエージェントから適切なものを都度選ぶ必要がある場面
- デバイスやワークフローの自動化が進み、エージェント数が増え続ける仮想アシスタントのエコシステムを構築・運用する場面
