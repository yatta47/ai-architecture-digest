---
type: case
title: Microsoft Discoveryで仕様書から物理レイアウトまでチップ設計を体験する
title_original: 'From Ad Astra to Semper Disco: Learning Chip Design with Microsoft Discovery'
company: Microsoft
industry: manufacturing
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- decision-execution
components:
- Microsoft Discovery
- OpenROAD
- SKY130
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://techcommunity.microsoft.com/blog/microsoft-discovery-blog/from-ad-astra-to-semper-disco-learning-chip-design-with-microsoft-discovery/4554904
published_at: '2026-09-17'
---

## 概要

半導体設計の専門知識を持たないMicrosoftのエンジニアが、AIエージェント基盤「Microsoft Discovery」を使って、RISC-Vコアと行列演算アクセラレータの仕様書から論理C、HLS（高位合成）C、RTL（Verilog）、そしてOpenROADとSKY130プロセスによる物理レイアウトまでを一気通貫で歩んだ実践記録。DAC 2026のワークショップとして実施され、AI支援によって専門知識がなくても設計フロー全体を短時間で体験できる一方、EDAツールのフィードバック解釈や最適化には引き続き専門家の知見が必要であることを示した。

## 設計のポイント

- 仕様からC、HLS、RTL、物理レイアウトへと段階的に詳細化していく古典的な設計プロセスにAIエージェントを組み込む
- コーディングエージェントをEDAツールと連携させ、合成・実装レポートから次の最適化イテレーションを導く
- クロック速度などのパラメータスイープや設計反復を自律的に行わせ、最適化の手間を削減する
- EDAフィードバックの解釈や用途別最適化の判断は専門家に委ね、AIには探索の迅速化を担わせる

## 使いどころ

- チップ設計の深い専門知識を持たないエンジニアがハンズオンで設計フローを学びたい場面
- オープンソースのEDAツールチェーンで低コストに設計プロトタイピングを試したいチーム
- AI支援設計と専門家によるチューニングを組み合わせたワークショップ・教育プログラム
