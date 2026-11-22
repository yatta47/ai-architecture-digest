---
type: announcement
title: AWS QuickにMeta広告のMCPコネクタを追加し、自然言語で広告運用・分析を行う機能
title_original: Meta ads is now available in AWS Quick
company: AWS
industry: retail
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
- decision-execution
components:
- AWS Quick
- Model Context Protocol
- Meta Ads Manager
- Conversions API
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/meta-ads-is-now-available-in-aws-quick/
published_at: '2026-11-22'
---

## 概要

AWS QuickにMeta ads AIコネクタが追加され、Meta広告のMCPサーバー操作を通じて、自然言語でキャンペーンの作成・管理・分析ができるようになった。Meta広告データを在庫やCRMなど自社データと組み合わせ、ダッシュボードや資料、自動ワークフローを生成できる。

## 設計のポイント

- 広告プラットフォームの操作をMCPサーバー経由でエージェントに公開し、分析から実行までを一つの対話環境に集約する。
- キャンペーン作成や予算変更などの書き込み操作は、実行前に必ずユーザーの承認を求めるヒューマンインザループとする。
- 広告データを在庫・粗利・CRMなどの社内データと結合し、予算配分の判断材料にする。
- プロンプトに「変更しない」と明示するなど、分析・提案と実行を分離した運用ができる。

## 使いどころ

- 広告運用チームが週次レポートや次の施策案の作成を自動化したい場面。
- 在庫や利益率に連動して広告予算を調整したい小売・EC事業者。
- ピクセルやカタログ審査の問題切り分けを素早く行いたいマーケター。
