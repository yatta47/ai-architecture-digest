---
type: announcement
title: Amazon BedrockでのGPT-6.1 Sol一般提供とエージェント業務への適用
title_original: Bring near-Astra intelligence to everyday work with GPT-6.1 Sol on Amazon Bedrock
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
- confidential-computing
components:
- Amazon Bedrock
- GPT-6.1 Sol
- Codex
- Agent Toolkit for AWS
- ChatGPT Work
- AWS IAM
- AWS CloudTrail
- AWS PrivateLink
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/bring-near-astra-intelligence-to-everyday-work-with-gpt-6-1-sol-on-amazon-bedrock/
published_at: '2026-09-29'
---

## 概要

OpenAIのGPT-6.1 SolがAmazon Bedrockで一般提供となり、エージェント型コーディング、コンピューター操作、専門業務向けの推論性能を提供する。OpenAIによれば、DeepSWE v1.1でGPT-6 Astraと同等の結果をタスクあたり約5分の1のコストで達成する。Bedrock上ではIAMによるアクセス制御、CloudTrailでの監査、PrivateLinkによるVPCエンドポイント、オペレーターもアクセスできないハードウェア分離環境での推論が利用できる。

## 設計のポイント

- エージェントのコストはトークン単価だけでなく、推論品質で決まる試行回数とタスク成功率を含めたタスク単位で評価する。
- モデルが使えるツールをアプリケーション側で定義し、承認が必要な操作や完了できない操作への応答をアプリ側で制御して人を介在させる。
- IAMでモデルアクセスを管理し、CloudTrailで呼び出しを監査し、PrivateLinkのVPCエンドポイントで通信をネットワーク境界内にとどめる。

## 使いどころ

- CodexからBedrock上のGPT-6.1 Solを使い、リポジトリ調査・実装・テストまでを行う開発チーム。
- 複雑な文書の分析や業務ツールをまたぐ多段ワークフローをエージェントで自動化したい企業。
- プロンプトや推論データの保護・監査が求められる環境でフロンティアモデルを使いたい組織。
