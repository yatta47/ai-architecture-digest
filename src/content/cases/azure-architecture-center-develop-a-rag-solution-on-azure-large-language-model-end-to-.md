---
type: guidance
title: RAGソリューションのLLMエンドツーエンド評価：グラウンド性・完全性・利用率で応答品質を測る
title_original: Large language model end-to-end evaluation
industry: cross-industry
cloud:
- azure
patterns:
- rag
- eval
- llmops
components:
- Azure AI Content Safety
- Ragas
- MLflow
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-llm-evaluation-phase
published_at: '2025-11-21'
---

## 概要

RAGパイプラインのチャンク化・埋め込み・検索を評価し終えた後、最終段階として言語モデルの応答そのものを評価するフェーズを解説する。グラウンド性・完全性・利用率・関連性・正確性という指標を用い、検索されたコンテキストと生成された応答の関係を多角的に測定する方法を示す。単一の正解を求めるのではなく、LLMの非決定性を踏まえて目標レンジで評価する考え方を提示している。

## 設計のポイント

- グラウンド性・完全性・利用率・関連性・正確性を組み合わせて評価し、どれか一つに偏らずワークロードに応じて優先順位を決める。
- LLM応答は非決定的であるため、単一の目標値ではなく目標レンジを設定して評価する。
- 完全性と利用率をクロス集計するマトリクスで、top-kパラメータ調整・チャンク戦略見直し・埋め込みモデル変更のどれが必要かを切り分ける。
- Azure AI Content SafetyやRagas・MLflowなど既存の評価ライブラリ/モデルを使い分けてグラウンド性や忠実性を算出する。

## 使いどころ

- RAGの検索・チャンク化フェーズの評価が完了し、最終的なLLM応答の品質を検証したいチームに有効。
- 低い完全性や利用率スコアから、チャンクサイズや埋め込みモデル選定など具体的な改善アクションに落とし込みたい場合に使える。
- エージェント型RAGを含む、より高度な評価指標(ツール選択精度・レイテンシなど)への拡張を検討する際の前提知識として参照できる。
