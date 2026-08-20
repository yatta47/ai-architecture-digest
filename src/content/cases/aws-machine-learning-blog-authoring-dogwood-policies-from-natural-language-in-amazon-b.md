---
type: guidance
title: 自然言語からDogwoodポリシーを自動生成するAgentCoreのPolicy Authoring
title_original: Authoring Dogwood policies from natural language in Amazon Bedrock AgentCore
industry: financial-services
cloud:
- aws
patterns:
- policy-as-code
- ai-agent
- guardrails
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- Amazon Bedrock Guardrails
- Dogwood
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/authoring-dogwood-policies-from-natural-language-in-amazon-bedrock-agentcore/
published_at: '2026-08-20'
---

## 概要

Amazon Bedrock AgentCoreのPolicy Authoringは、自然言語で書かれたポリシー文書をガバナンス言語Dogwoodの形式的仕様へ自動変換するAI機能。時間や過去のセッション履歴にまたがる制約（レート制限や事前ステップの要求など）もAgentCore Gatewayに組み込まれたDogwoodモニタでリアルタイムに強制できる。銀行のコールセンターエージェントを例に、MCPツールマニフェストから生成したスキーマを使って許可/禁止ルールを正確なポリシーへ落とし込む手順を示す。

## 設計のポイント

- ポリシーはエージェントのMCPツールマニフェストから生成したスキーマを参照するため、生成されたポリシーは実際にエージェントが呼び出す名前と一致する
- Dogwoodはデフォルト拒否でforbidがpermitを上書きする設計のため、『許可』はpermit+条件、『制限』はforbidとして翻訳される
- 過去のセッション内の出来事（直前の本人確認など）を参照するtemporal条件により、単発リクエストだけでは判定できないルールも表現できる
- ポリシー文書は要約でなく転記が前提のため、理由や背景を含む文書は事前にルールだけを抜き出しておくと変換精度が上がる

## 使いどころ

- コンプライアンス部門が人間向けに維持している規程文書を、そのままエージェントの実行制御に転用したい場合
- レート制限・順序制約・累積効果など、単一リクエストの検査だけでは表現できないガバナンス要件がある金融・規制業種のエージェント運用
- Guardrailsによる自由記述の意味内容チェックとツール引数の制限を組み合わせた多層防御を素早く構築したい場合
