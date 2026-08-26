---
type: guidance
title: 金融サービスにおけるエージェントAIのROI可視化：LangSmithとPay-iによるコスト・KPI管理
title_original: Proving the ROI of agentic AI in financial services
industry: financial-services
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- llmops
- document-processing
components:
- LangChain
- LangSmith
- LangGraph
- Pay-i
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/proving-the-roi-of-agentic-ai-in-financial-services
published_at: '2026-08-26'
---

## 概要

金融機関の取締役会が求める「AI投資の費用対効果」に答えるため、LangChain/LangSmith/LangGraphによるエンジニアリング観測性とPay-iによるビジネスKPI測定を組み合わせる手法を解説する。RFP自動応答とAMLコンプライアンス監視という2つの実例を用い、要件抽出精度やSMEレビュー承認率などの業務KPIをどう定義・追跡し経営層にROIを説明するかを示す。

## 設計のポイント

- LangSmithが全エージェント実行をトレースとして記録し、モデル・プロバイダー別のトークン使用量とコストを自動計算する
- Pay-iがユースケースごとに業務成功の定義を調査し、業界水準に基づくKPIとゴール値（例: 要件抽出精度95%）を動的に設定してスコアリングする
- エンジニアリング観測性（『何をしているか』）とビジネス価値観測性（『その価値は何か』）の2層を接続してROIを定量化する設計
- RFP自動応答では人間のSMEが最終承認を担い、AIはドラフト生成と引用付けおよびレビュー要ギャップの検出に専念する人間参加型フロー

## 使いどころ

- RFP対応で数百時間かかる調査・ドラフト作成・SME間調整を自動化しつつ、レビュー品質を担保したい金融機関の提案チーム
- マルチエージェントシステムの動的なLLM呼び出しやツール呼び出しのコストを従来のFinOpsツールで追跡できず、可視化基盤を必要とするエンジニアリング組織
- AIエージェントへの投資対効果を取締役会や経営層に数値で説明する責任を負うCIOやトランスフォーメーション責任者
