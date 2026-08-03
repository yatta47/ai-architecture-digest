---
type: announcement
title: Bedrock Guardrailsのポリシーを自動修正するAutomated Reasoning Refinement
title_original: Automated Reasoning policy refinement in Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- policy-as-code
components:
- Amazon Bedrock Guardrails
- Amazon Bedrock
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automated-reasoning-policy-refinement-in-amazon-bedrock/
published_at: '2026-08-03'
---

## 概要

Amazon Bedrock Guardrailsの自動推論チェックは自然言語を形式論理に変換してLLM出力の正しさを検証するが、失敗したテストの原因診断とポリシー修正は手作業だった。新機能のAutomated Policy Refinementはルールの誤りとあいまいな変数定義という2種類の失敗モードをそれぞれ専用モードで自動修正案として提示し、人はレビュー・承認するだけで済むようにする。

## 設計のポイント

- 自然言語→変数割当の翻訳ステップと、形式ルールによる検証ステップを分離し、失敗の原因をどちらのステップかで切り分ける
- ルールの誤り（Rule issue）にはIterative Refinement、変数定義のあいまいさ（Translation ambiguous）にはAmbiguous Variable Refinementと、失敗モードごとに異なる自動修正エンジンを割り当てる
- 修正案は既存のテストケースに対してシミュレーションし収束するまで内部反復するが、最終適用は人間のレビュー・承認を必須のゲートとする

## 使いどころ

- 10〜30ルール規模のポリシーを手作業のSMT-LIB編集なしに継続的にチューニングしたいプラットフォームチーム
- LLMの出力に対する正しさ保証をコンプライアンス要件として持つ規制業種のガードレール運用
