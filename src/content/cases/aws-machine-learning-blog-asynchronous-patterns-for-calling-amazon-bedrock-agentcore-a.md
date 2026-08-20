---
type: guidance
title: サーバーレスパイプラインでAmazon Bedrock AgentCoreエージェントを呼ぶ非同期パターン
title_original: Asynchronous patterns for calling Amazon Bedrock AgentCore agents in serverless pipelines
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- event-driven
- cost-optimization
- out-of-band-inference
components:
- Amazon Bedrock AgentCore
- AWS Step Functions
- AWS Lambda
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/asynchronous-patterns-for-calling-amazon-bedrock-agentcore-agents-in-serverless-pipelines/
published_at: '2026-08-19'
---

## 概要

AgentCoreのエージェントは応答までに時間がかかるため、呼び出し側のLambda関数が同期的にブロックして待つと、その待機時間ぶんの計算コストを丸ごと支払うことになる。本記事は、タスクトークンによるコールバック、Step Functionsとの直接サービス統合、Durable Functionという3つの非同期呼び出しパターンをブロッキングのアンチパターンと比較し、呼び出し側の計算リソースを待機中に解放してコストを抑える設計を示す。

## 設計のポイント

- エージェント側は推論待ちのCPUに課金されないが、呼び出し側のLambda/コンテナは同期呼び出しでブロックしている間フルの計算リソース分課金され続けるため、無駄は呼び出し側に生じる
- エージェントにタスクトークンやDurable Functionのコールバック ID を渡し、完了時にエージェント自身が該当の実行を再開させることで、呼び出し側は起動して即座に制御を返せる
- エージェントは受け取った信号（タスクトークンの有無など）に応じて同期/非同期を自動判別するため、オーケストレーションパターンを変えてもエージェント自体の再デプロイは不要
- 同一のパイプライン・同一のエージェントのまま検証対象のブランチ（Validateステージ）だけを差し替えて4パターンを同条件で比較できるようにする

## 使いどころ

- ドキュメント検証など推論に時間がかかるエージェント呼び出しをステートマシン/サーバーレスパイプラインに組み込みたい場合
- 同期呼び出しでLambdaやEC2がブロックされたまま課金され続けており、コストを最適化したいチーム
- オーケストレーション方式（Step Functions/Durable Functionなど）を切り替えてもエージェント自体は変更したくない場合
