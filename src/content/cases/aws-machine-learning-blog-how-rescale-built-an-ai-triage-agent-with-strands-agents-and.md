---
type: case
title: E2Eテスト失敗を自動分類・振り分けするAIトリアージエージェント
title_original: How Rescale built an AI triage agent with Strands Agents and AI-DLC
company: Rescale
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- root-cause-analysis
- human-in-the-loop
components:
- Strands Agents
- AI-DLC
- Amazon EKS
- Argo Workflows
- Playwright
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-rescale-built-an-ai-triage-agent-with-strands-agents-and-ai-dlc/
published_at: '2026-10-22'
---

## 概要

Rescaleは夜間E2Eテストの失敗分類とチーム振り分けを自動化するトリアージエージェントを、AWSのAI-DLCで構築した。問題定義からステージング展開まで5日、本番まで数週間で到達し、既存のArgo Workflows CI/CDの1ステップとして動く。

## 設計のポイント

- AI-DLCの『AIが実行し人が決める』方針で、AIが質問と計画提示を行い人間が各段階で承認する。
- Mob Elaboration／Mob Constructionのグループセッションで要件定義と構築を同時進行させ、非同期の引き継ぎを減らす。
- 既存のCI/CDパイプライン内のステップとして組み込み、ログ・履歴・ソースを根拠に分類と担当チーム推定を行う。

## 使いどころ

- 週次リリースを統合テストが止めており、失敗調査がボトルネックになっているチーム。
- AI主導の開発手法を短期間で小さな業務に適用し、組織へ展開したい開発組織。
