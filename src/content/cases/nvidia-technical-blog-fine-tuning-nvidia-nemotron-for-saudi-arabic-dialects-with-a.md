---
type: guidance
title: NeMoでNemotron ASRをサウジ方言にファインチューニングする手順
title_original: Fine-Tuning NVIDIA Nemotron for Saudi Arabic Dialects, with a Path to Other Languages
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- fine-tuning
- multilingual-localization
- eval
components:
- NVIDIA Nemotron 3.5 ASR
- NVIDIA NeMo
- NeMo Curator
- Nemotron 3 Diarization
- FLEURS
- SADA 2022
- PyTorch
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/fine-tuning-nvidia-nemotron-for-saudi-arabic-dialects-with-a-path-to-other-languages/
published_at: '2026-09-30'
---

## 概要

NVIDIA Nemotron 3.5 ASRをNeMoで、サウジのNajdi・Hijazi方言に適応させるファインチューニングの手順を示す記事。最小限のデータ整備、FLEURSとのリプレイ混合、長さ別バケット化、エンコーダの部分解凍を組み合わせる。133.7時間の学習でWERが55.05%から29.96%に下がり、英語も11.04%から10.42%に改善した。

## 設計のポイント

- 破壊的忘却を抑えるため、既習データを少量混ぜるリプレイ混合を使う。
- 構造的に不良なラベルや不整合クリップのみを除き、難しい音声は捨てない最小限のキュレーションにする。
- エンコーダの層を部分的に凍結すると計算量を減らせるが、精度とのトレードオフがある。
- 注意コンテキスト拡大とビームサーチは再学習なしでWERを下げられるが、遅延が増える。

## 使いどころ

- 多言語ASRを方言や特定ドメインに適応させたいチーム。
- 既存言語の性能を保ったまま専用化したい音声認識の導入。
- 話者分離付きの文字起こしを多人数環境で使いたい場面。
