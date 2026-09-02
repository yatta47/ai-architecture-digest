---
type: announcement
title: Amazon BedrockとClaude Platform on AWSにおけるClaude Fable 5.1の提供開始
title_original: Introducing Claude Fable 5.1 on AWS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- guardrails
- confidential-computing
components:
- Amazon Bedrock
- Claude Platform on AWS
- AWS GovCloud
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-claude-fable-5-1-on-aws/
published_at: '2026-09-01'
---

## 概要

AWSはAmazon BedrockおよびClaude Platform on AWSでClaude Fable 5.1の提供を発表した。数学・科学分野の高難度推論や長時間のエージェント作業、エンドツーエンドの分析業務での能力向上に加え、AnthropicとAWSが共同提供するEnterprise Frontier Safeguardsにより対象顧客は自社管理下のクラウド環境にデータを置いたままモデルを利用できる。

## 設計のポイント

- Fable 5.1はCovered Modelに指定され、利用には最大30日のデータ保持とAWS内での人的安全性レビューを伴うaws_reviewモードの設定が前提となる
- Enterprise Frontier Safeguardsにより対象顧客はゼロデータ保持(ZDR)でFable 5/5.1を利用でき、2026年内は内部利用に限定した先行提供として位置づけられている
- Anthropic Messages APIに加えInvoke/Converse APIやAWS CLI・SDK経由でも呼び出せるようにし、既存のBedrockワークフローとの互換性を保っている
- 推論モデルであるためレスポンスにthinkingブロックが含まれる場合があり、固定インデックスではなくブロック種別でテキストを選択する実装が必要になる

## 使いどころ

- コードベース横断の機能追加やレビュー・パフォーマンス改善を数時間にわたり自律的に進めたいエージェント型コーディングワークフロー
- 金融・会計・ヘルスケア領域でリサーチから資料作成・数値検証までを一気通貫で行いたいナレッジワーク
- 文献調査から仮説構築・実験・形式検証までを支援したい科学研究キャンペーン
- データを自社管理下のクラウド環境に置いたまま最先端モデルを安全に利用したい規制業種の企業
