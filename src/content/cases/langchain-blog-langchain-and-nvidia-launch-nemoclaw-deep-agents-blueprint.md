---
type: announcement
title: 'NemoClaw: LangChain×NVIDIAのオープンなガバナンス型エージェントスタック'
title_original: LangChain and NVIDIA launch the NemoClaw Deep Agents Blueprint
company: LangChain
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- llmops
- eval
- inference-optimization
components:
- NVIDIA Nemotron 3 Ultra
- LangChain Deep Agents Code
- NVIDIA OpenShell
- LangSmith
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langchain-and-nvidia-launch-the-nemoclaw-deep-agents-blueprint
published_at: '2026-07-08'
---

## 概要

LangChainはNVIDIAと共同で、オープンモデルNemotron 3 Ultra・LangChain Deep Agents Code・NVIDIA OpenShellランタイムを組み合わせた「NemoClaw for LangChain Deep Agents」ブループリントを発表した。モデル・ハーネス・eval・ランタイムを一体でチューニングすることで、Deep Agentsベンチマークにおいて0.86のスコアを他社モデルの約10分の1のコスト（4.48ドル対43.48ドル）で達成し、企業が自社データとガバナンス要件に沿ってエージェントを所有・運用できるオープンなスタックを提供する。EY・Baseten・Fireworks等のパートナーが本番展開を支援する。

## 設計のポイント

- モデル・ハーネス・eval・ランタイムの4層を個別にではなく一体でチューニングすることでエージェント性能を最大化する
- オープンモデル(Nemotron)を採用し、重みのホスティングやファインチューニングを企業自身が制御できるようにする
- サンドボックス化されたガバナンス可能なランタイム(OpenShell)でツール・システム・データへのアクセスをポリシーとして制御する
- 複数の推論プロバイダー(Baseten, Fireworks等)から選べる構成にしロックインを避けつつ本番提供の柔軟性を確保する

## 使いどころ

- 規制業界などでガバナンス・監査性を重視しつつ本番エージェントを展開したい企業
- 自社データ・業務知識を活かしたカスタムエージェントを構築したい企業
- コストを抑えつつフロンティア級のエージェント品質を得たいチーム
