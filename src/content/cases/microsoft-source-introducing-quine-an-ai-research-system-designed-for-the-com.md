---
type: case
title: 生物学の世界モデルと研究ハーネスをつなぐ研究システムQuine
title_original: 'Introducing Quine: an AI research system designed for the complexity of biology'
company: Microsoft
industry: healthcare
cloud:
- azure
patterns:
- ai-agent
- reasoning-computation-separation
- human-in-the-loop
components:
- Quine
- Microsoft Discovery
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/research/blog/introducing-quine-an-ai-research-system-designed-for-the-complexity-of-biology/
published_at: '2026-09-29'
---

## 概要

Microsoft Researchは、配列・構造・細胞状態・画像を横断して学習する生物学の世界モデルと、科学ツール・文献・研究者を結ぶハーネスから成るQuineを発表した。Broad Instituteとの共同研究で膵がん向けの化合物候補を優先順位付けし、複数のウェットラボ実験で上位候補を検証している。

## 設計のポイント

- 複数モダリティを個別の専門モデルで束ねず、共通表現として同時学習して相互に予測へ活用する。
- モデルを完全とはせず、実験設計の優先順位付けに役立てる位置づけにして高コストな実験を絞る。
- 質問から提案、設計、実験、測定と、研究者を起点にしたループでモデルを継続的に改善する。
- 研究専用で、出力には専門家の検証が必要と明示して運用する。

## 使いどころ

- 創薬・がん研究で候補化合物の絞り込みを効率化したい研究チーム。
- 科学分野で世界モデルとエージェントハーネスの組み合わせを検討する開発者。
- 実験コストが高い領域でAI予測と検証を回す仕組みを設計する人。
