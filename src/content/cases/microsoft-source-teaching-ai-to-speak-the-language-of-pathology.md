---
type: case
title: 病理画像と診断レポート言語を統合学習する基盤モデルPRISM2
title_original: Teaching AI to speak the language of pathology
company: Microsoft Research / Paige (Tempus)
industry: healthcare
cloud: []
patterns:
- unified-runtime
- fine-tuning
components:
- PRISM2
- Hugging Face
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/signal/articles/teaching-ai-to-speak-the-language-of-pathology/
published_at: '2026-08-04'
---

## 概要

Microsoft ResearchとPaige(現Tempus)は、病理組織画像と実際の病理レポートに基づく言語データの両方で学習させた基盤モデルPRISM2を開発した。タスクごとに専用モデルを作り直すことなく、前立腺がん・乳がん・乳がんリンパ節転移検出など複数のベンチマークで専用システムと同等以上の性能を達成した。モデル重みはHugging Face上で研究用に公開されている。

## 設計のポイント

- 病理画像と病理レポートから生成した数百万件の質問応答データをペアで学習させ、視覚的所見と診断言語を結びつける
- タスクごとに個別モデルを構築するのではなく、単一の基盤モデルがプロンプトに応じて複数の診断タスクに対応できるよう設計する
- 画像単体でも画像とテキストの組み合わせでも動作するよう入力形態を柔軟にする
- モデル重みを公開し、研究コミュニティが独自の病理AIツールをゼロから構築せず再利用・発展できるようにする

## 使いどころ

- 複数のがん種・検出タスクを個別モデルなしで単一モデルでカバーしたい病理研究者
- 既存の基盤モデルを土台に新しい病理診断支援ツールを効率的に開発したいヘルスケアAIベンダー
- 画像所見と診断レポートの言語を関連付けて解釈支援を行いたい医療機関
