---
type: guidance
title: LLM評価者そのものを測るデータセットとGemini対GPTの比較
title_original: Two New Llama Datasets and A Gemini vs. GPT Showdown
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- eval
components:
- LlamaIndex
- LabelledEvaluatorDataset
- LabelledPairwiseEvaluatorDataset
- Gemini
- GPT
- MT-Bench
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/two-new-llama-datasets-and-a-gemini-vs-gpt-showdown-9770302c91a5
published_at: '2023-12-20'
---

## 概要

LLMを評価者に使う場合も評価者自体の検証が必要として、単体評価用と2回答比較用のデータセット型を追加した。MT-Benchを変換したデータでGeminiとGPTの評価者性能を比較している。

## 設計のポイント

- LLMジャッジは盲信せず、人手の参照評価付きデータで定期的にベンチマークする。
- 絶対評価と2回答の比較評価は別のデータセットとして測る。

## 使いどころ

- LLM-as-a-judgeで品質管理するチームの評価者選定。
- 評価モデルを差し替える前の妥当性確認。
