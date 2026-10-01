---
type: case
title: uniopenがAmazon Novaを小売モデレーション方針に合わせてファインチューニングし本番運用
title_original: How uniopen customized Amazon Nova to their retail moderation policies for production deployment
company: uniopen (Uni-President Enterprises Group)
industry: retail
cloud:
- aws
patterns:
- fine-tuning
- human-in-the-loop
- eval
- prompt-optimization
- guardrails
components:
- Amazon Nova 2 Lite
- Amazon Nova 2 Pro
- Amazon SageMaker AI
- Amazon S3
- Amazon DynamoDB
- Argo Workflows
- Argo CD
- Amazon EKS
- Amazon SNS
- Amazon CloudWatch
- Amazon Bedrock Guardrails
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-uniopen-customized-amazon-nova-to-their-retail-moderation-policies-for-production-deployment/
published_at: '2026-10-01'
---

## 概要

台湾のUni-President Enterprises Group傘下のuniopenは、行動9分類と対象3分類で判定する独自のモデレーション方針に合わせ、Amazon Nova 2 LiteをSageMaker AIで教師ありファインチューニング(LoRA)し、最後にプロンプトレベルの出力最適化を加えた。ベースラインのPer Behavior Macro F1 0.5852がファインチューニングで0.8364に向上した。誤り報告から人手検証済みの修正データを作り、評価ゲートを通過した候補だけ本番に昇格させる継続改善ループも構築した。

## 設計のポイント

- 本番のモデレーション経路と、修正生成・学習・評価・デプロイの経路を分離した。
- Nova 2 Proが修正候補を生成しても、人間が検証したものだけを学習データに入れ、生成ラベルを正解扱いしない。
- 必須の回帰テストであるハードゲートと、警告のソフトゲートで昇格を制御し、ソフトゲート警告時は管理者承認を求める。
- Argo Workflows、DynamoDB、Argo CDで評価からデプロイまでを再現可能なワークフローにした。

## 使いどころ

- 汎用モデルでは学べない自社固有の分類方針を持つコンテンツモデレーション。
- 誤り報告を継続的に学習データへ反映したいLLM運用チーム。
- 品質低下時の自動昇格を防ぐ評価ゲートが必要なモデル更新運用。
