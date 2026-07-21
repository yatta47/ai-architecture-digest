---
type: guidance
title: LangGraphのフォールトトレランス機構：リトライ・タイムアウト・エラーハンドラ
title_original: 'Fault Tolerance in LangGraph: Retries, Timeouts, and Error Handlers'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- fault-tolerance
components:
- LangGraph
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/fault-tolerance-in-langgraph
published_at: '2026-06-04'
---

## 概要

LangGraphはエージェントをノードのグラフとしてモデル化し、実行を制御する立場を活かして各ノードにRetryPolicy（バックオフ・ジッター付き自動リトライ）、TimeoutPolicy（wall-clockタイムアウトと進捗ベースのidle timeout）、error_handler（リトライ枯渇後に失敗コンテキスト付きで走る後処理ノード）という3つのフォールトトレランス機構を直接アタッチできる。これにより、ネットワーク障害やレート制限など本番エージェントが直面する一時的エラーへの対処コードをビジネスロジックから分離しつつ、ノード定義のすぐそばで宣言的に管理できる。

## 設計のポイント

- RetryPolicyのretry_onで再試行対象の例外を明示的に絞り込み、ValueErrorなど恒久的なバグ由来の例外は再試行しない
- TimeoutPolicyをハードなrun_timeoutと進捗ベースのidle_timeoutに分離し、正常にストリーミング中の長時間処理は誤って打ち切らない
- error_handlerはリトライが尽きた後にのみ、失敗したノードと同じ実行ステップ内でアトミックにスケジュールし、途中でクラッシュしても再開時にハンドラ自体が再実行される
- フォールトトレランス設定をadd_node呼び出し時にノードへ直接アタッチし、保護対象のロジックのすぐそばに置く

## 使いどころ

- 数時間〜数日単位で動く長時間実行エージェントが途中で失敗しても最初からやり直さずに済むようにしたい場合
- LLMプロバイダのレート制限や外部APIの一時的な障害に耐える本番グレードのエージェントを構築する場合
- リトライ枯渇後に注文失敗のマーキングや補償処理・dead-letter書き込み・フォールバックモデルへの切り替えなど後処理が必要な業務フロー
- エラーハンドリングの定型コードをノードごとに書き分散させず、宣言的かつ一元的に管理したいチーム
