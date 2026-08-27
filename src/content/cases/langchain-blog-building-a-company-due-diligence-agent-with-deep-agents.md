---
type: case
title: 5系統の調査を並列サブエージェントで束ねる企業デューデリジェンス自動化
title_original: Building a company due diligence agent with Deep Agents, LangSmith and Parallel
company: LangChain
industry: financial-services
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- parallel-execution
components:
- Deep Agents
- LangSmith
- Parallel Task API
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel
published_at: '2026-08-26'
---

## 概要

PEアナリストの案件審査や与信審査、コンプライアンス、保険引受など金融サービス各所で発生する企業デューデリジェンスを自動化するため、LangChainのDeep AgentsによるプランニングとサブエージェントA委譲、Parallelの構造化Web調査API（引用・確信度付き）を組み合わせたエージェントを構築した。企業プロファイル・財務・訴訟規制・報道・競合の5系統を並列サブエージェントで調査し、競合分析はさらに競合ごとに動的にファンアウトし、Rivian社の事例では9回のAPI呼び出しで約23分で完了した。

## 設計のポイント

- 企業プロファイル・財務・訴訟規制・報道・競合という5つの調査観点をそれぞれ専用サブエージェントに割り当て、独立したコンテキストで並列実行した
- 競合分析は競合リストが判明してから競合数だけ動的にサブエージェントをファンアウトする、実行時に並列度が決まる設計にした
- 各調査結果にフィールド単位の引用と確信度スコアを付与し、確信度が低いフィールドは前回の調査を引き継いだフォローアップ質問で再調査できるようにした
- 序盤の調査結果（対象が子会社と判明した場合など）が後続の調査範囲を変えるため、オーケストレーターが調査計画を都度立て直せるプランニング機構を持たせた

## 使いどころ

- PEのディール審査や銀行の与信審査など、根拠付きの企業調査レポートを大量に作る金融サービス業務
- 新規取引先や委託先のコンプライアンス確認を自動化したいコンプライアンス/オンボーディングチーム
- 保険引受のように多角的な企業情報を短時間で構造化してまとめたい業務
