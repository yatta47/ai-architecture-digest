---
type: guidance
title: OCR+RPAからエージェント型Document AIへの進化とパススルー率改善
title_original: 'Document AI: The Next Evolution of Intelligent Document Processing'
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
components: []
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/document-ai-the-next-evolution-of-intelligent-document-processing
published_at: '2026-07-19'
---

## 概要

従来のOCR・IDP・RPAの組み合わせが持つテンプレート依存の脆さを、意味構造を推論するエージェント型OCRとLLM推論による適応的なAgent Workflowsで克服する「Document AI」という概念を解説している。従来60〜70%で頭打ちだった自動処理のパススルー率が、エージェント型アプローチにより90%超まで改善しうるとしている。

## 設計のポイント

- エージェント型OCRはピクセルではなく意味構造を推論し、レイアウトが変化してもテンプレート再学習なしに読み取れる
- 不確実なフィールドをフラグ立てし、パラメータを変えて再試行するなど自己評価・自己修正のループを組み込む
- 固定的なif-thenルールのRPAではなくLLM推論による適応的なワークフローで、欠落項目の推論や動的なエラーリカバリを行う

## 使いどころ

- レイアウトの揺れが多い請求書・契約書などでOCR+RPAのパススルー率が頭打ちになっている業務を改善したい場合
- 例外処理から継続的に学習し自動化率を高めたい大量文書処理オペレーション
