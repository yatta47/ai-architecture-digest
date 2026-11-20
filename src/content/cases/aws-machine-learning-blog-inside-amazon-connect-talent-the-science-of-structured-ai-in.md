---
type: guidance
title: Amazon Connect Talentの構造化AI面接の設計原則
title_original: 'Inside Amazon Connect Talent: The science of structured AI interviews'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- eval
components:
- Amazon Connect Talent
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/inside-amazon-connect-talent-the-science-of-structured-ai-interviews/
published_at: '2026-11-19'
---

## 概要

Amazon Connect Talentは、職務に紐づく証拠、適応的な追質問、証拠に基づく採点という3原則で、構造化面接をAIで大規模に実施する。内部研究と外部専門家レビューで評価した結果を紹介する。

## 設計のポイント

- コンピテンシーごとに行動基準付きのスコアカードを作り、質問を対応づける。
- 回答ごとに証拠が足りるかを判定し、不足なら追質問する。

## 使いどころ

- 大量採用で面接の一貫性を保ちたい人事部門に向く。
