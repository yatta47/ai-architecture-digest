---
type: case
title: 読み取り自律・書き込みHITLゲート型のKubernetes SREエージェント
title_original: How we build an autonomous SRE Agent for Kubernetes Deployments
company: LangChain
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
- root-cause-analysis
components:
- LangGraph
- Deep Agents
- LangSmith
- Claude Sonnet
- Claude Haiku
- Slack
- Kubernetes
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-we-build-an-autonomous-sre-agent-for-kubernetes-deployments
published_at: '2026-08-05'
---

## 概要

LangChainが自社のKubernetesクラスタ運用向けに、健全性のトリアージから修復提案までを行う自律SREエージェントを構築した。読み取りは完全自律、書き込みは人間承認（HITL）を必須とする構造的な安全設計と、定期監視には安価なモデルのみを使うコスト設計を組み合わせている。

## 設計のポイント

- 定期ヘルスチェックはPythonでクラスタ状態を収集しHaikuを1回呼ぶだけにし、フルエージェント実行(~20コール)に比べコストを95〜99%削減する
- pod-inspectorなど専門サブエージェントを並列実行させ、コンテキストを絞ってハルシネーションを減らしつつ安価なモデルに処理を任せる
- 書き込みツールはchange-executorサブエージェントに隔離し、Human-in-the-Loop承認ゲートで必ず人間の承認を通す構造にし、in-cluster RBACでも同じ読み書き分離を二重化する
- 変更提案は一目で影響範囲が分かる粒度に絞り、helm upgradeのような高インパクトで見えにくいツールは意図的に持たせない

## 使いどころ

- Kubernetesクラスタの障害トリアージや復旧対応でオンコール負荷を減らしたいSREチーム
- 本番環境への自動変更は許容できないが、読み取り・診断は自動化したい組織
- LLM呼び出しコストを抑えながら数分おきの定期監視を回したい基盤運用チーム
