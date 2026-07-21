---
type: case
title: monday ServiceのAIサービスエージェント、評価をDay0からコード化する
title_original: 'monday Service + LangSmith: Building a Code-First Evaluation Strategy from Day 1'
company: monday.com
industry: cross-industry
cloud: []
patterns:
- eval
- ci-cd
- guardrails
components:
- LangSmith
- LangGraph
- Vitest
- OpenEvals
- AgentEvals
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/customers-monday
published_at: '2026-06-15'
---

## 概要

monday Serviceは、企業向けサービス管理を自動化するLangGraphベースのReActエージェント群に対し、評価をリリース後の後付けではなく開発初日から組み込んだ。ゴールデンデータセットによるオフライン評価（安全網）と本番トレースを監視するオンライン評価（モニター）の2層構成を、Vitest/LangSmith統合でCI上のコードとして管理し、評価フィードバックループを162秒から18秒へと8.7倍高速化した。

## 設計のポイント

- オフライン評価（安全網）とオンライン評価（継続監視）の2層構成にし、コード変更の副作用検知と本番品質モニタリングを分担させる
- 決定的なスモークチェック→LLM-as-Judgeによる正確性評価→KB根拠付け・矛盾解決・ガードレールなど用途別チェックへと段階的に評価粒度を上げる
- 評価ロジックをバージョン管理されたコードとして扱い、GitOpsスタイルのCI/CDで本番に評価ケースをデプロイする
- Vitestのプロセス並列化とLLM評価のI/O並列化を組み合わせ、評価フィードバックループの遅さが開発速度を犠牲にしないようにする

## 使いどころ

- 本番投入前にAIエージェントの品質劣化を検知したいエンタープライズSaaSチーム
- 評価をアルファテスト任せにせず開発サイクルの一部として継続運用したいチーム
