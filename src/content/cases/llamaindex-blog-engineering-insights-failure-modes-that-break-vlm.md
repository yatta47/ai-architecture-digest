---
type: case
title: LlamaParseの障害から学んだVLM搭載OCRの2つの故障モード(無限ループと引用ブロック)
title_original: 'Engineering Insights: Failure Modes That Break VLM-Powered OCR in Production'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- llmops
- document-processing
- guardrails
components:
- LlamaParse
- OpenAI API
- Anthropic API
- Gemini API
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/engineering-insights-failure-modes-that-break-vlm-powered-ocr-in-production
published_at: '2026-07-19'
---

## 概要

LlamaIndexはエージェント型文書パーサーLlamaParseで発生した複数の障害を分析し、原因を『繰り返しループ(空白や定型句をトークン上限まで生成し続ける)』と『引用ブロック(著作権フィルタが正当な抽出を誤検知して生成を停止する)』という性質の異なる2つの故障モードに切り分けた。両者はOpenAI/Anthropic/Geminiそれぞれで異なるfinish_reasonとして現れ、下流エージェントの連鎖的な停止やレイテンシ急増を引き起こしていた。

## 設計のポイント

- 繰り返しループには厳格なmax_tokens・タイムアウト・ストリーミング中の繰り返し検知による強制終了と、前後処理での空白正規化フィルタを実装した
- 引用ブロックは著作権フィルタの誤検知であり、モデルプロバイダはブロックされたリクエストにも課金するため、温度設定を変えたリトライだけでは根本解決にならないと認識した
- 一見似た2つの障害を『トークン確率崩壊』と『安全フィルタの誤検知』という別の根本原因として切り分けたことが、的確な対処につながった

## 使いどころ

- LLM/VLMをバッチの文書処理パイプラインに組み込み、大規模稼働させているチーム
- APIのfinish_reasonやエラーコードからLLM起因の障害を切り分けたいSRE/プラットフォームチーム
