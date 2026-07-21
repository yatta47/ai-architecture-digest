---
type: guidance
title: エージェントの『推論』をトレースで可視化し評価につなげる観測性の設計
title_original: Agent observability powers agent evaluation
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- llmops
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agent-observability-powers-agent-evaluation
published_at: '2026-06-30'
---

## 概要

従来のソフトウェアはコードとログで原因を追跡できるが、数百ステップにわたり自律的にツールを呼び出すAIエージェントでは『失敗したのはコードではなく推論』であるため同じデバッグ手法が通用しない。この記事はRun（1回のLLM呼び出し）・Trace（一連の実行全体）・Thread（複数ターンの会話）という3つの観測性プリミティブを定義し、これらが単一ステップ・全ターン・複数ターンというエージェント評価の粒度にそのまま対応することを解説する。

## 設計のポイント

- デバッグの単位をコードの行ではなく、LLM呼び出し単位の『Run』とその連なりである『Trace』に置き換える
- 本番トレースを単なる不具合発見の場ではなく、オフライン評価データセットを継続的に育てる情報源として扱う
- 評価の粒度をRun（単一ステップ）・Trace（1ターン全体）・Thread（複数ターン）の3段階で使い分ける
- Runには入力プロンプト・利用可能ツール・実際の選択理由まで記録し、デバッグと評価の両方に使えるようにする

## 使いどころ

- 数十〜数百ステップに及ぶエージェントの挙動が不安定で、原因箇所を特定できずに困っているチーム
- 本番運用から得られる実際のユーザーとのやり取りをテストケースとして評価スイートに反映したい場合
- エージェント評価の粒度設計（単一ステップ/1ターン/複数ターン）をこれから決めようとしているチーム
