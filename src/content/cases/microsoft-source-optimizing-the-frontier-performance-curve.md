---
type: case
title: 製品特化の小型モデル群でコスト対性能のフロンティア曲線を押し上げるMAIファミリー
title_original: Optimizing the frontier performance curve
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- inference-optimization
- multi-model-routing
- cost-optimization
components:
- MAI-Cyber-1-Flash
- MDASH
- MAI-Code-1-Flash
- GitHub Copilot
- MAI-Image-2.5-Flash
- Bing Image Creator
- PowerPoint
- OneDrive
- MAI-Voice-2-Flash
- Dynamics 365 Contact Center
- MAI-Transcribe-1.5
- Dragon Copilot
- Maia 200
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://microsoft.ai/news/optimizing-the-frontier-performance-curve/
published_at: '2026-07-30'
---

## 概要

Microsoft AIは、汎用フロンティアモデルではなく製品ごとにチューニングした小型モデル群(MAIファミリー)をハーネスと共同最適化することで、性能を維持しながらトークンコストを大幅に削減。MAI-Cyber-1-FlashはCyberGymベンチマークで1位を獲得しつつコストは半分、MAI-Voice-2-FlashはGPUコストを最大89%削減するなど、コスト対性能の「フロンティア曲線」を押し上げる取り組みを紹介する。

## 設計のポイント

- 汎用フロンティアモデルは全タスクの一部(例: 90%)のみに使い、残りの困難なタスクだけ最大級モデルに回すハーネス設計(MDASH)を採用する
- モデル・ハーネス・強化学習環境(RLE)を共同最適化し、コスト対性能曲線上の狙った位置を選べるようにする
- 自社シリコン(Maia 200)とモデルを共同設計することで性能/ワットを改善する
- 単一モデルファミリーへの依存を避け、モデルを代替可能な部品として扱うことで障害・方針変更・地政学リスクへの耐性を高める

## 使いどころ

- コーディング支援(GitHub Copilot)や画像生成、音声、文字起こしなど高頻度に呼び出される製品機能のGPUコスト削減
- コールセンターエージェント(T-Mobile、EasyJetなど)向けの音声処理コスト最適化
- 医療分野など大量の文字起こしを処理する用途でのエラー率とコストの両立
