---
type: guidance
title: GPT-4Vの図表読み取りは具体的な質問で改善するかの実験
title_original: GPT4-V Experiments with General, Specific questions and Chain Of Thought prompting (COT) Techniques
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- eval
components:
- GPT-4V
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/gpt4-v-experiments-with-general-specific-questions-and-chain-of-thought-prompting-cot-techniques-49d82e6ddcc9
published_at: '2023-11-17'
---

## 概要

棒グラフ、散布図、表の画像に対し、一般的な質問・具体的な質問・Chain of Thoughtの3方式でGPT-4Vの回答を比較した実験。具体的に尋ねるほど回答は良くなる一方、軸ラベルの捏造や凡例の取り違えも観察された。

## 設計のポイント

- 画像解析では対象カテゴリや色の対応など、読み取りの前提をプロンプトで与える。
- 図表読み取りの結果は誤り得る前提で、自社データで検証してから使う。

## 使いどころ

- マルチモーダルLLMに図表を読ませる機能を設計する開発者。
