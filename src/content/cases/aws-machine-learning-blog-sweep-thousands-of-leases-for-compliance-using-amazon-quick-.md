---
type: guidance
title: LLMは問い合わせの翻訳に徹し判定は決定論的ルールエンジンが行うAdjudicated Queryパターン
title_original: Sweep thousands of leases for compliance using Amazon Quick and the Adjudicated Query pattern
industry: other
cloud:
- aws
patterns:
- guardrails
- decision-execution
- human-in-the-loop
components:
- Amazon Quick
- Amazon Quick Sight
- Amazon Bedrock
- AWS Lambda
- Amazon API Gateway
- Amazon Cognito
- Amazon Aurora Serverless v2
- Model Context Protocol
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/sweep-thousands-of-leases-for-compliance-using-amazon-quick-and-the-adjudicated-query-pattern/
published_at: '2026-10-02'
---

## 概要

賃貸契約5万件規模のコンプライアンス確認で、チャットUIから質問しつつ合否判定は非AIのルールエンジンに任せるAdjudicated Queryパターンの紹介。RAGやtext-to-SQLでは担保できない網羅性の証明と判断の防御可能性を、完全性レシートで満たす。AWSリファレンスアーキテクチャとサンプルも提示している。

## 設計のポイント

- モデルの役割は自然言語を型付き操作の呼び出しに変換し結果を説明することに限定し、クエリ生成や母集団の決定、判定は行わせない。
- ルールはコードでなくバージョン管理されたデータとし、法改正はルール行の編集で対応する。
- compliant+in-breach+ambiguous+unreadable=scannedの完全性レシートを保存前に検証し、評価漏れを構造的に防ぐ。
- チャットは件数とレシートを返し、全件はQuick Sightダッシュボードで同一ストアから参照させる。

## 使いどころ

- 制裁スクリーニング、保険金請求査定、輸出管理など、見落としが法的責任になる領域。
- 監査や訴訟で適用ルール版や根拠を後から説明する必要があるコンプライアンス部門。
- 業務ユーザーに自然言語アクセスを与えつつ判定の正確性を維持したい場面。
