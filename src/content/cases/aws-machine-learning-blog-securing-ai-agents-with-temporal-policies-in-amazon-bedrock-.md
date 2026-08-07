---
type: guidance
title: エージェントのセッション履歴を踏まえて認可判断するAgentCoreの時系列ポリシー
title_original: Securing AI agents with temporal policies in Amazon Bedrock AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- guardrails
- human-in-the-loop
- llm-gateway
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- AgentCore Policy
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/securing-ai-agents-with-temporal-policies-in-amazon-bedrock-agentcore/
published_at: '2026-08-06'
---

## 概要

Amazon Bedrock AgentCoreの新機能「temporal policies」は、単発のツール呼び出しだけでなくエージェントのセッション内の履歴(トラジェクトリ)全体を踏まえて認可判断を行うステートフルなポリシーエンジンである。Gateway側、つまりエージェントのコード外で強制されるため、ハルシネーションによる値のすり替えや、リスク上限を超えた累積取引、承認なしの高リスク操作といった、個々の呼び出しは正常に見えても文脈的に危険なケースを防げる。

## 設計のポイント

- 認可ロジックをエージェントのコード内ではなくGatewayの外側に置き、プロンプトやコードのバグに関わらずバイパスできないようにする
- セッションIDと呼び出し元アイデンティティの組で軌跡(トラジェクトリ)を一意に区別し、同じセッションIDでも別アイデンティティなら別軌跡として扱う
- 前段ツールの出力と今回の引数が一致するか、承認イベントが記録されているかなど時系列の整合性をルール化し、ハルシネーションや二重操作を防ぐ
- 軌跡の参照範囲を24時間のルックバックウィンドウに限定し、状態肥大化と古い文脈での誤判定を避ける

## 使いどころ

- 資金移動や取引実行など、文脈依存で危険度が変わる操作をエージェントに任せる金融・決済系ワークロード
- 承認済みの標準作業手順(SOP)の順序遵守をエージェントに強制したい業務システム
- エージェントが同一リクエストを短時間に何度も実行してしまう暴走を、累積エクスポージャーで止めたい場合
