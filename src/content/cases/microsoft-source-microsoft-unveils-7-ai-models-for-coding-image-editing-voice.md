---
type: announcement
title: 'Microsoft MAI: コーディング/画像/音声/ルーティング向け低価格モデル7種の発表'
title_original: Microsoft unveils 7 AI models for coding, image editing, voice and more
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- inference-optimization
- fine-tuning
components:
- MAI Code 2
- MAI Code 2 Flash
- MAI Cyber 2 Flash
- MAI Image 2.7
- MAI Realtime 1
- Dragon Copilot Transcribe
- Decision 1.1
- Maia 200
- Microsoft Foundry
- GitHub Copilot
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://microsoft.ai/news/microsoft-ignite-2026/
published_at: '2026-11-18'
---

## 概要

MicrosoftがMAIモデルファミリー7種を発表した。コーディング・サイバー防御・画像編集・リアルタイム音声・文字起こし・ルーティング用Decisionモデルを、競合比で大幅に低い価格で提供するとしている。自社環境で動かせるMAI Licensed Weightsも発表された。

## 設計のポイント

- Decision 1.1のようなルーティングモデルをアプリに組み込み、高価な大型モデルは必要時のみ使う。
- 用途別に軽量(Flash)と高性能モデルを使い分け、日常的な大量タスクのコストを下げる。
- 独自データでカスタマイズしたモデルを自社Azure環境で動かし、重みとデータの管理権を保つ。

## 使いどころ

- エージェントを常時稼働させ、トークンコストが課題になっている開発組織。
- 通信など特定ドメインの分析で、カスタムモデルによりコストを下げたい企業。
- 重みを自社管理下に置きたい規制業種の企業。
