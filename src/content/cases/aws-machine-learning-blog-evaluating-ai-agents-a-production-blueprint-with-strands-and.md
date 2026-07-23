---
type: case
title: 中古車ダイーラー向け在庫検索エージェントの3層評価・監視パイプライン
title_original: 'Evaluating AI Agents: A production blueprint with Strands and AgentCore'
company: Motorway
industry: retail
cloud:
- aws
patterns:
- eval
- ai-agent
- llmops
components:
- Strands Agents SDK
- Amazon Bedrock AgentCore
- Amazon Bedrock
- LanceDB
- Amazon Titan Text Embeddings V2
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-a-production-blueprint-with-strands-and-agentcore/
published_at: '2026-07-23'
---

## 概要

Motorwayは英国の中古車オークションマーケットプレイスで、AWS PACEと共同でStrands AgentsとAmazon Bedrock AgentCoreを用いたディーラー向け在庫検索エージェントの評価パイプラインを構築した。ビルド時のstrands-agents-evalsとプロダクション監視のAgentCore Evaluationsを組み合わせた3層(ツール利用・推論・出力品質)評価フレームワークにより、誤った検索結果を8件に1件から50件に1件に削減し、問題検知時間を数時間から数分に短縮した。

## 設計のポイント

- ツール利用(>95%)・推論(>85%)・出力品質(>90%)の3層に閾値を設け、全層合格をデプロイのゲートにする
- ビルド時評価(strands-agents-evals)と本番監視(AgentCore Evaluations)の二段構えでGenAIOpsライフサイクル全体をカバーする
- 非決定的な出力に対してpass^kメトリクスで一貫性を評価する
- 5段階デプロイパイプラインに品質ゲートを組み込み、閾値未達ならリリースをブロックする

## 使いどころ

- 数千件規模の同時利用者を抱える会話型検索・レコメンドエージェントの信頼性担保
- 複数ツール・ベクトル検索を組み合わせたエージェントでツール選択ミスや意味検索の誤りを検出したいチーム
- CI/CDにエージェント品質ゲートを組み込みたいプロダクションAI運用チーム
