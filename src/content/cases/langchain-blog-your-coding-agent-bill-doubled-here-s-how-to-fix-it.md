---
type: announcement
title: 複数コーディングエージェントのコスト可視化とガバナンス基盤
title_original: Your coding agent bill doubled. Here's how to fix it.
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
- llm-gateway
- eval
components:
- LangSmith
- Claude Code
- Cursor
- GitHub Copilot Chat
- LLM Gateway
- Engine
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/fix-your-coding-agent-bill
published_at: '2026-07-08'
---

## 概要

LangChainは、Claude Code・Cursor・GitHub Copilot Chat・OpenCode等の複数のコーディングエージェントを併用するチームで開発コストが急増している問題（Uberが2026年AI予算を4カ月で使い切った例等）を取り上げ、各ツールがバラバラの形式でログを出すため支出の全体像が見えないことを根本課題として指摘した。解決策として、LangSmithが全コーディングエージェントのセッションを共通トレースモデルに正規化して横断比較できるようにし、Engineが冗長なツール呼び出し等の無駄を検出して改善提案を行い、LLM Gatewayがユーザー・チーム・組織単位でコスト上限を設定してガバナンスする、という可視化→標準化→最適化→統制の4段階サイクルを提示した。

## 設計のポイント

- ツールごとに異なる形式のログを、root session・turn・tool call・metadataという共通トレースモデルに正規化し横断クエリを可能にする
- 可視化→コスト標準化→最適化提案→ガバナンスという段階的サイクルで設計し、各段階が次の段階を可能にする構造にする
- エージェントセッションの解析から重複したツール呼び出しなど具体的な無駄を自動検出し、ダッシュボードの数値だけでなく改善提案として提示する
- LLM Gatewayでユーザー・チーム・組織単位のコスト上限を設定し、フロンティアモデルが不要な作業はオープンソースモデルやサブエージェントへルーティングする

## 使いどころ

- 複数のコーディングエージェントを併用しておりツールごとに費用管理が分断されているエンジニアリングチーム
- コーディングエージェントの利用料が急増し予算超過に直面している開発組織
- AI投資対効果を可視化し無駄なトークン消費を削減したいエンジニアリングリーダー
