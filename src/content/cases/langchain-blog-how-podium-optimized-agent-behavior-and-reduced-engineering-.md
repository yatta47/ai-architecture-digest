---
type: case
title: LangSmithでAIエージェントの会話終了判定を改善し、サポート対応の90%を非エンジニアに委譲
title_original: How Podium optimized agent behavior and reduced engineering intervention by 90% with LangSmith
company: Podium
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- fine-tuning
components:
- LangChain
- LangSmith
- LangSmith Playground
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/customers-podium
published_at: '2026-08-26'
---

## 概要

Podiumは中小企業向け顧客対応AIエージェント「AI Employee」の開発にLangSmithを導入し、20〜30回に及ぶLLM呼び出しのトレースを可視化した。会話の自然な終了を認識できず挨拶を繰り返す問題に対し、データセット作成とモデル蒸留・ファインチューニングでF1スコアを91.7%から98.6%に改善した。さらに問題の原因（バグ・文脈不足・指示の不整合・LLM由来）を切り分ける運用フローを整備し、エンジニアの介入を90%削減した。

## 設計のポイント

- 会話ログにメタデータ（顧客属性・業種など）を付与しトレースをグルーピングすることで、バランスの取れた高品質なデータセットをキュレーションできるようにした
- 大きいモデルの出力を蒸留して小さいモデルに転写する手法で、トレースに自動記録された入出力を使いモデル入れ替えを容易にした
- ペアワイズ評価とオフライン評価を組み合わせ、ファインチューニング後のモデル改善を定量的に検証してから本番反映した
- 問題原因を『アプリのバグ』『文脈不足』『指示の不整合』『LLM起因』の4種に分類し、非エンジニアのサポートチームでも対応可能な範囲を明確にした

## 使いどころ

- エージェントの応答品質に関するカスタマー問い合わせが多く、原因切り分けにエンジニアが都度対応しているチーム
- 会話の終了判定など特定の振る舞いの精度を継続的なデータ収集とファインチューニングで改善したいプロダクト
- サポート担当者にPlayground等でプロンプトや出力を直接確認・修正させ、エンジニアリソースを節約したい組織
