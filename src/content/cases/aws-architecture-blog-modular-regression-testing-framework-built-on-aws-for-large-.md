---
type: guidance
title: 本番トラフィックを再生する回帰テストフレームワーク
title_original: Modular regression testing framework built on AWS for large-scale systems
ai_relevant: false
company: AWS
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: quality
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/modular-regression-testing-framework-built-on-aws-for-large-scale-systems/
published_at: '2026-11-12'
---

## 概要

本番リクエストをストリームに記録し、事前環境で新コードに再生して結果を比較する、AWS上のモジュール型回帰テスト手法。ステートレスな計算系に向き、ステートフルな系は再生判定で副作用をスキップする。
