---
type: guidance
title: Nemotronを地域ルール向けにペルソナ合成データでLoRA微調整
title_original: Fine-Tuning NVIDIA Nemotron to Know Local Rules, Not Just Local Languages
company: NVIDIA / Pleias
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- eval
components:
- NVIDIA Nemotron
- NVIDIA NeMo
- LoRA
- Nemotron-Personas
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/fine-tuning-nvidia-nemotron-to-know-local-rules-not-just-local-languages/
published_at: '2026-10-26'
---

## 概要

フランス・ベルギーのペルソナデータと行動規約、公式手続き文書から合成会話を作り、Nemotron 3.5 LightningをNeMoでLoRA微調整し、固定テストセットで評価する手順を示す。Pleiasは脊椎ケア相談に応用した。

## 設計のポイント

- 地域に根ざした合成ペルソナで実データ不足を補う。
- 微調整後はアダプターをマージし、固定テストセットで評価する。
- データ生成から評価までの手順をリポジトリとエージェントスキルで再利用できる。

## 使いどころ

- 地域固有の制度や言語に合わせてオープンモデルを調整したいとき。
- 実データが少ない領域のテスト多様化。
