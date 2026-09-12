---
type: guidance
title: トークン単価ではなく『正解1件のコスト』でLLMを選ぶベンチマーク手法
title_original: 'Beyond the price per token: Choosing the right OpenAI model on Amazon Bedrock for your workload'
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- multi-model-routing
- eval
- cost-optimization
components:
- Amazon Bedrock
- OpenAI GPT-5.6
- OpenAI API
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/beyond-the-price-per-token-choosing-the-right-openai-model-on-amazon-bedrock-for-your-workload/
published_at: '2026-09-11'
---

## 概要

AWSはトークン単価ではなく『正解1件あたりのコスト』『エージェントのターン数』『実務成果物の品質』という3軸でOpenAIモデル群（Bedrock上のgpt-5.6系とOpenAI API上のmini/nano）を比較するオープンソースのベンチマークハーネスを公開した。推論を無効化したBedrock版luna/terraは、トークン単価が高くても正答あたりコストや必要ターン数の少なさで、mini/nanoより実質的に安く高品質な結果を示した。

## 設計のポイント

- モデル選定は$/1Mトークンではなく『正解1件あたりの総コスト（誤答分も含む）』で評価する
- マルチターンのエージェントワークフローでは会話履歴の再送によって入力トークンがほぼ2次関数的に増えるため、ターン数の削減がコストに直結する
- 採点は決定的チェックとLLM-as-a-Judge（固定プロンプト・ハッシュ記録）を組み合わせ再現性を担保する

## 使いどころ

- 既存でコスト最適モデル（mini/nano等）を使っており、上位モデルへの切り替えが実質コスト増になるか判断したいチーム
- Web検索・ツール呼び出しを伴うエージェント型ワークロードのコスト試算をしたい設計者
