---
type: guidance
title: 形式ポリシーの意味的差分を反ユニフィケーションで計算する手法
title_original: Semantic diffing of formal policies with anti-unification
ai_relevant: false
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/semantic-diffing-of-formal-policies-with-anti-unification/
published_at: '2026-11-11'
---

## 概要

形式ポリシーのテキスト差分は意味に関係ない並べ替えに埋もれるため、反ユニフィケーションとe-graphで共通パターンと差異を抽出するOSSエンジンを紹介する。差異が無ければ与えた法則の下でポリシーが等価と判断できる。
