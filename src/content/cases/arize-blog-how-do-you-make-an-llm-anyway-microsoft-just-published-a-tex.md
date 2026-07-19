---
type: case
title: Microsoftの技術レポートに見るフロンティアLLM「MAI-Thinking-1」の学習パイプライン全貌
title_original: How do you make an LLM, anyway? Microsoft just published a textbook.
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- llmops
- llm-pretraining
components:
- MAI-Thinking-1
- Common Crawl
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-do-you-make-an-llm-anyway-microsoft-textbook/
published_at: '2026-07-13'
---

## 概要

Microsoftが公開した109ページの技術レポートは、推論モデルMAI-Thinking-1を学習させるまでのデータ収集・フィルタリングから事前学習・mid-training・post-trainingまでの全工程を詳細に開示した。約1.2兆ページのWebクロールを厳しくフィルタ・重複排除し、コード比率54.6%のデータミックスで30兆トークンを8,192基のGPUで学習、設計判断は小型モデルの『ladder』実験とEfficiency Gain指標で積み上げ的に検証している。

## 設計のポイント

- 収集したWebデータをスパム・重複・AI生成コンテンツまで含めて徹底的にフィルタリングし、学習データの質を担保する。
- 狙う能力（推論力など）に応じてコードやmath等のデータ比率を意図的に偏らせ、希少で高品質なデータは複数エポック繰り返して学習させる。
- 本番規模の学習前に小型モデルの『ladder』で設計変更を検証し、Efficiency Gainという単一指標で比較しながら小さな改善を積み重ねる。
- mid-training段階で高品質データに絞り込み直し、コンテキスト長を16K→64K→262Kと段階的に延伸してロングコンテキスト性能を作り込む。

## 使いどころ

- フロンティア級LLMを自前で学習したい研究機関やAIラボが、データ選定からアーキテクチャ検証までのプロセス設計を参考にする場合。
- 小規模実験の結果を大規模学習に外挿する際の落とし穴（小規模では良く見えたデータ配分が大規模で悪化するケース）を把握したいエンジニアリングチーム。
