---
type: guidance
title: サーバーレスGitメトリクスダッシュボード
title_original: A serverless, data-driven Git metrics dashboard using Amazon Quick Sight
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/a-serverless-data-driven-git-metrics-dashboard-using-amazon-quick-sight/
published_at: '2026-09-17'
---

## 概要

GitHub/GitLabのイベントを検知してメトリクスを自動収集し、S3に保存してQuick Sightで可視化するサーバーレスなGit分析基盤を紹介する。EventBridge SchedulerとStep Functionsで差分検知・全量/差分ロード・大規模リポジトリの並列処理を自動化し、AIコーディングツール導入前後の開発生産性を継続的に計測できるようにする。
