---
type: guidance
title: エージェントループの高速な意思決定を担う『System One』モデルJevの使い方
title_original: What is Jev? A guide to TypeSafe AI's System One model
company: TypeSafe AI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- inference-optimization
- reasoning-computation-separation
components:
- Jev
- LangChain
- TypeSafe AI
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/building-a-harness-with-jev
published_at: '2026-09-18'
---

## 概要

エージェントループの各判断ごとにフルのLLM呼び出しを行うのは遅く高コストであるという課題に対し、TypeSafe AIはテキスト生成を行わず状態と型付き質問を受け取り確率付きの型付き回答を返す『System One』モデルJevを提供する。RLCD（calibrated decisionのための強化学習）で学習されており、比較対象のLLMに対し最大200倍高速・400倍低コストとされる分類的な判断をエージェントループ内に組み込める。

## 設計のポイント

- エージェントループ内の分類・優先度判定などの軽い意思決定は、毎回フルのチャットLLMを呼ぶ代わりに状態＋型付き質問を渡すSystem Oneモデルに任せて計算量を分離する
- 選択・スコア・数値などの質問タイプごとに確率付きの型付き回答を返す設計にし、アプリ側のコードがそのままロジックとして使える形にする
- ツール呼び出し・構造化出力というエージェント統合の既存プリミティブの上に、判断の高速化レイヤーとして追加する

## 使いどころ

- サポートチケットの緊急度判定のような高頻度・低複雑度の分類判断を大量に行うエージェントシステム
- エージェントループの各ステップでフルLLM呼び出しを行うことでレイテンシ・コストが課題になっている高トラフィックなサービス
