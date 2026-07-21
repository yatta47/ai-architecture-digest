---
type: guidance
title: 'AIエージェント開発を体系化する「ADLC」: Build→Test→Deploy→Monitorの反復サイクル'
title_original: The Agent Development Lifecycle (ADLC)
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- context-engineering
components:
- LangChain
- LangGraph
- Deep Agents
- CrewAI
- Claude Agent SDK
- LangSmith Fleet
- Claude Cowork
- n8n
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/the-agent-development-lifecycle
published_at: '2026-06-25'
---

## 概要

LangChainのHarrison Chase氏が、エージェント開発を「Build→Test→Deploy→Monitor」の4段階からなる反復的なライフサイクル(ADLC)として整理した記事。Build段階ではフレームワーク・ランタイム・ハーネスというツール層の違いとno-code/low-codeツールの役割を、Test段階ではデータセット・メトリクス・実験・シミュレーションを用いた評価手法を解説している。単発のデモとしてではなく、多数のエージェントを組織的・継続的に開発するための共通基盤とガバナンスの必要性を強調する内容になっている。

## 設計のポイント

- エージェント開発を「Build→Test→Deploy→Monitor」の反復ループとして設計し、本番運用の学びを次のBuild/評価サイクルへ明示的にフィードバックする。
- ツール選定はフレームワーク(抽象化に特化)・ランタイム(状態管理や制御フローの実行に特化)・ハーネス(プロンプト/スキル/MCP/ミドルウェアなど実行環境に特化)の3層で役割を切り分ける。
- no-code/low-codeツールでドメイン専門家の参加を広げつつ、hooksとmiddlewareでツール呼び出し・認可・業務ルールをコードから制御できる余地を残す。
- 完璧な評価スイートを最初から目指さず、少数の代表的タスクから始めて本番トレースで継続的にデータセットを強化し、正解が一意なタスクは正解ベース、そうでないタスクは基準(criteria)ベースで評価する。

## 使いどころ

- 単発のデモではなく、複数のエージェントを組織横断で安全かつ反復的に開発・出荷したいプラットフォーム/プラットフォームエンジニアリングチーム。
- サポート対応やコーディング支援、社内オペレーションなど、マルチターンで状態を持ち会話・ツール呼び出しを繰り返すエージェントを構築し、単一ターン評価では品質を保証しきれないチーム。
- 業務理解者(ドメイン専門家)がプロンプトやスキルを直接編集しつつ、エンジニアが信頼性・テスト容易性・ガバナンスを担保したい組織。
- モデル更新やプロンプト変更のたびに同じ失敗が再発するのを防ぎたい、eval・実験基盤を整備中のAI開発チーム。
