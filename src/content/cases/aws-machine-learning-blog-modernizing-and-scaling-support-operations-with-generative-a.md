---
type: case
title: 研修動画からSOPを自動生成しRAGでチケット対応を導くサポート運用基盤
title_original: Modernizing and scaling support operations with generative AI on AWS
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
- document-processing
components:
- Amazon Bedrock
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/modernizing-and-scaling-support-operations-with-generative-ai-on-aws/
published_at: '2026-09-02'
---

## 概要

サポート業務のナレッジがSOP・録画・属人知識に分散している課題に対し、研修動画からSOPを自動生成し、RAGでチケット対応の手順をガイドし、機械学習で作業量配分とSLAリスクを予測する生成AIソリューションを解説する記事。タグ付けやステータス更新などの定型作業はエージェントに任せつつ人間の関与も維持する。

## 設計のポイント

- 個々のチケットや文書を最適化するのではなく、部門をまたぐ業務フロー全体を可視化・改善する設計方針をとる
- 研修動画やウォークスルーの録画から知識を抽出し構造化・検索可能な形でSOPとして永続化する
- RAGでチケット内容から関連SOPを自動的に特定し、担当者が手作業で探す時間を削減する
- SLA違反の兆候を事前に検知するML予測を組み込み、事後対応ではなく先回りの優先順位付けを可能にする

## 使いどころ

- SOPや属人知識が分散し新人が対応に苦労するサポートチーム
- 金融・医療・物流・製造・エネルギーなど他業界へ応用可能な運用ナレッジ管理
- チケット急増時にSLA違反を未然に防ぎたいオペレーションリーダー
