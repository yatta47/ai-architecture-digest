---
type: case
title: PHIに触れないチャネル設計でSlack常駐エージェントに運用業務を任せる医療系3社の事例
title_original: How healthcare organizations use Claude Tag
industry: healthcare
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- guardrails
components:
- Claude Tag
- Claude Agent SDK
- Claude API
- Slack
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-healthcare-organizations-use-claude-tag
published_at: '2026-09-14'
---

## 概要

医療系企業3社がSlack常駐のエージェントClaude Tag(ベータ)を使いPHIに触れないチャネル/コネクタ限定で人間とエージェントのチームを構築。紹介状処理AIを提供するInsight Healthは、PHIなしのエンジニアリングチャネルでClaude TagとBAA対象のエージェントZeus(Claude Agent SDK製、PHIをマスクして本番データにアクセス)を役割分担させ、インシデント対応で97%のアラートがエンジニア不要で解決するようになった。患者受け入れ支援プラットフォームTennrは社内ツールの主要メンテナーとしてClaude Tagを採用し、非エンジニアが自然言語でリクエストするだけでコード変更・デプロイまで完了する運用を実現した。

## 設計のポイント

- PHIを扱う権限をチャネル・コネクタ単位で厳密にスコープし、PHIに触れないエージェントとBAA対象の別エージェントに役割を分離するゼロトラスト的設計
- チャネルメモリにより長期継続する調査や標準指示を再説明なしに引き継がせる
- 非エンジニアが自然言語でチケットを書くだけでコード変更・デプロイ・ドキュメント化まで完了させ、内部ツールの保守コストを実質ゼロに近づける

## 使いどころ

- PHIなど機微情報の取り扱い制約下でもAIエージェントにインシデント対応や運用業務を任せたい医療系SaaS企業
- エンジニアの手を借りずに社内ツールを継続的にメンテナンスしたい急成長スタートアップ
