---
type: guidance
title: AIエージェント専用の実行サンドボックス設計指針
title_original: Agents need their own computer. Here's how to give them one safely.
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- guardrails
components: []
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agents-need-their-own-computer
published_at: '2026-07-15'
---

## 概要

コード実行を伴うAIエージェントには、ラップトップやDockerコンテナではなく専用の隔離された実行環境が必要だと説く記事。安全な実行・制御・可観測性・高速な起動という4要件を提示し、本番運用ではサンドボックスプラットフォームの構築・利用が避けられないとする。

## 設計のポイント

- モデルが生成したコードは出所を問わず未検証・信頼できないものとして扱い、ハードウェア仮想化でカーネルごと分離する。
- 資格情報はネットワーク層のプロキシで注入し、エージェント自身にはトークンを渡さない設計にする。
- CPU/メモリ/ネットワークのリソース上限を課しタスクごとのコスト上限を設ける。
- 実行したコマンド・変更ファイル・ネットワーク呼び出しを監査ログとして残し、既知の状態から再実行・比較できるようにする。

## 使いどころ

- モデル生成コードやパッケージインストールを伴うエージェントを本番運用するプラットフォームチーム。
- 数千のエージェント環境を並列に起動しそれぞれ隔離が必要なマルチテナントAIプロダクト。
