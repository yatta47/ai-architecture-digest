---
type: announcement
title: MicrosoftとMistralが欧州向けにソブリンAI基盤を拡張
title_original: Microsoft and Mistral expand strategic partnership to give enterprises and regulated industries frontier AI
  they can control
company: Microsoft, Mistral
industry: cross-industry
cloud:
- azure
patterns:
- sovereign-ai-deployment
- multi-model-routing
components:
- Microsoft Foundry
- Foundry Local
- Copilot Studio
- Azure Local
- Mistral Medium 3.5
- Mistral OCR 4
- NVIDIA Vera Rubin GPU
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/2026/07/21/microsoft-and-mistral-expand-strategic-partnership-to-give-enterprises-and-regulated-industries-frontier-ai-they-can-control/
published_at: '2026-07-21'
---

## 概要

MicrosoftとMistralは、欧州の規制産業向けにMistralのフロンティアモデルをMicrosoft FoundryやCopilot Studioへ統合し、クラウド・クラウド接続・完全切断の3形態でAzure/Azure Local上に展開できる体制を発表した。あわせてMistralの欧州GPU基盤(NVIDIA Vera Rubin)拡張に数十億ドル規模を投資し、データ主権を保ちながらフロンティアAIを利用可能にする。

## 設計のポイント

- Microsoft FoundryとFoundry Localで同一のモデル・ツール・APIをクラウドからエッジ(Azure Local)まで一貫して使えるようにし、環境ごとの作り直しを減らす。
- クラウド/クラウド接続/完全切断の3段階の運用モデルを用意し、機密性や規制要件に応じてデータの越境有無を選べるようにする。
- モデル提供元(Mistral)とインフラ(Azure)を分離しつつGPU供給を拡張することで、需要増に対応する。

## 使いどころ

- 欧州の金融・公共など、データ主権や規制順守が必須でデータを域外に出せない業種。
- オンプレやエッジでの完全切断運用が必要なミッションクリティカルな環境。
