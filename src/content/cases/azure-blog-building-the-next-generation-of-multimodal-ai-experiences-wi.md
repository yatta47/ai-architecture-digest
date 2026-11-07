---
type: announcement
title: Microsoft FoundryにfalのKling・LTX・MiniMax動画生成モデルを追加
title_original: Building the next generation of multimodal AI experiences with fal in Microsoft Foundry
company: Microsoft
industry: media
cloud:
- azure
patterns:
- multi-model-routing
- cost-optimization
components:
- Microsoft Foundry
- fal
- Kling v3 Pro
- LTX-2.5
- MiniMax H3 Max
outcome:
  type: quality
source_id: azure-blog
source_name: Azure Blog
source_url: https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/building-the-next-generation-of-multimodal-ai-experiences-with-fal-in-microsoft-/4570032
published_at: '2026-11-06'
---

## 概要

MicrosoftとfalがFoundryで動画生成モデルをパブリックプレビュー提供する。用途に応じてドラフト用の高速モデルと最終出力用の高品質モデルを選べ、米国ホスティングやモデル別従量課金で企業利用を想定している。

## 設計のポイント

- 高速ドラフト用と高品質最終用のモデルを使い分けて速度とコストと品質を両立する。
- テキスト→動画と画像→動画を1つのプラットフォームで組み合わせ、複数モデルのワークフローにする。
- データ所在地と課金体系をモデルごとに確認して選定する。

## 使いどころ

- 広告やマーケティングで動画コンセプトを素早く試作する制作チーム。
- 生成動画を企業アプリに組み込む開発者。
