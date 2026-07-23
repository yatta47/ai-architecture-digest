---
type: guidance
title: 推論モデルとGPTモデルを『プランナー』と『ワークホース』として使い分ける設計
title_original: How to keep costs low and accuracy high
industry: cross-industry
cloud: []
patterns:
- reasoning-computation-separation
- cost-optimization
components:
- o3
- o4-mini
- GPT-4.1
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/reasoning-best-practices#how-to-keep-costs-low-and-accuracy-high
published_at: '2025-07-21'
---

## 概要

OpenAIの推論モデル（o3、o4-miniなど）は複雑な戦略立案や曖昧な情報からの意思決定に強い『プランナー』、GPTモデル（GPT-4.1など）は低遅延・低コストで実行に徹する『ワークホース』と位置づけ、アプリケーションでは推論モデルに戦略立案を任せ、実行はGPTモデルに委ねることで精度とコストを両立できるという設計指針を示す。

## 設計のポイント

- 複雑な計画・意思決定は推論モデル、定型的な実行タスクは低コストなGPTモデルという役割分担でモデルを組み合わせる。
- 速度とコストが最優先ならGPTモデル、実行精度と自律性が最優先なら推論モデルという選択基準を明示している。

## 使いどころ

- コストを抑えつつ複雑なタスクの精度も担保したいプロダクション用途のエージェント設計。
- モデル選定で迷うチームが用途別にモデルを使い分ける指針を必要とする場合。
