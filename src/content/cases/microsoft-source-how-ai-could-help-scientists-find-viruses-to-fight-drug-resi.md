---
type: case
title: 検査可能なエージェントで構築するファージ療法のバイオインフォマティクスパイプライン
title_original: Developing Bioinformatics Workflows for Phage Therapy with Inspectable Agents
company: Microsoft
industry: healthcare
cloud:
- azure
patterns:
- ai-agent
- human-in-the-loop
- context-engineering
components:
- Microsoft Discovery
- Discovery Bookshelf
- MCP
- PubMed
- Europe PMC
- NCBI BLAST
- Semantic Scholar
- ClinicalTrials.gov
- AlphaFold
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://techcommunity.microsoft.com/blog/microsoft-discovery-blog/developing-bioinformatics-workflows-for-phage-therapy-with-inspectable-agents/4560876
published_at: '2026-09-30'
---

## 概要

Microsoft Discoveryアプリを使い、薬剤耐性菌に有効なファージを環境データから探索するバイオインフォマティクスパイプラインを、人間とエージェントの協働で設計・検証した事例。研究要件がタスクツリーに分解され、各段階の出力が次段階の入力へ追跡可能につながる。タスクツリー生成からドラフトレポートまで4時間未満で進んだ。

## 設計のポイント

- 科学者の目的を「purpose」と検査可能な「task」ツリーに変換し、各ステップを人が確認・修正できるようにしている。
- 信頼できる論文群をBookshelfとして汎用インターネット検索から分離し、エージェントの根拠を管理している。
- MCPベースのアダプタでPubMedやAlphaFoldなど外部データ源を段階的に追加し、ツール統合の工数を抑えている。
- エージェントの改訂計画は人間が承認してから該当タスクを進める。

## 使いどころ

- 研究者が再現可能な計算パイプラインを短期間で立ち上げたい場面。
- エビデンスの連鎖を確認しながらエージェントに調査・解析を任せたい科学研究。
- 外部の文献・データベースをMCPで束ねる研究支援エージェントを設計する際の参考。
