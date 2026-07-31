---
type: guidance
title: NVIDIA Red Teamが指摘するAIエージェントの4つのセキュリティ対策
title_original: Four Ways to Deploy More Secure AI Agents
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- defense-in-depth
components:
- Docker
- NVIDIA OpenShell
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/four-ways-to-deploy-more-secure-ai-agents/
published_at: '2026-07-30'
---

## 概要

NVIDIA AI Red Teamが、企業向けAIエージェントの侵入テストで繰り返し発見した脆弱性のパターン(アクセス制御の欠如、任意コード実行、ネットワーク送信制御の欠如、平文シークレットの露出)と、その対策となる決定的なアーキテクチャ制御を解説。プロンプトベースやLLM-as-judgeによる防御は敵対的操作に弱いと指摘する。

## 設計のポイント

- エージェントへのアクセスは許可されたユーザーに限定し、呼び出し元ユーザーと同じ権限に絞る最小権限の原則を適用する
- コマンド実行ツールは可能な限り避け、必要な場合は許可コマンドの厳格なallowlistとサンドボックス化された実行環境を組み合わせる
- ネットワーク送信はデフォルト拒否とし、最小権限のallowlistのみを許可する
- 恒久的なシークレットをエージェントの実行環境に平文で置かない

## 使いどころ

- チャット接続型のAIエージェントを社内システムやライブツールに接続する前のセキュリティレビュー
- コード実行ツールやシェルアクセスを持つコーディングエージェントのサンドボックス設計
- LLM-as-judgeのみに依存したガードレールの限界を理解し、決定的な制御を追加したいセキュリティチーム
