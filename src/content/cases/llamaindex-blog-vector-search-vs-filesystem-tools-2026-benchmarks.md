---
type: case
title: ファイルシステム探索エージェントと従来型RAGの精度・速度比較実験
title_original: Did Filesystem Tools Kill Vector Search?
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- eval
components:
- LlamaParse
- Chonkie
- Qdrant
- OpenAI
- FastEmbed
- Gemini 3 Flash
- AgentFS
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/did-filesystem-tools-kill-vector-search
published_at: '2026-07-19'
---

## 概要

LlamaIndexが、ハイブリッド検索RAG(LlamaParse+Chonkie+Qdrantによる疎密統合検索)と、grep/read/globなどファイルシステムツールを使う自律エージェント(fs-explorer、Gemini 3 Flash)を、arXiv論文5本に対するQAタスクで比較した。RAGの方が平均3.8秒速い一方、正確性・関連性のスコアではファイルシステム探索エージェントがRAGを上回る結果となった。

## 設計のポイント

- パース済みテキストをディスクキャッシュして再利用し、取り込みパイプラインの耐障害性と速度を両立する
- 疎(キーワード)・密(埋め込み)検索をRRFで統合するハイブリッドRAG構成をベースラインとして採用する
- ファイルシステム探索エージェントにはread/grep/glob/parseの少数ツールのみを与え、ループの中で自律的にツール呼び出しを選択させる
- LLM-as-a-Judgeで正確性・関連性を0-10で採点し、速度とあわせて定量比較する

## 使いどころ

- 小〜中規模の文書集合に対しRAGと素朴でないエージェント探索のどちらを選ぶか検討するチーム
- チャンク分割による文脈欠落がボトルネックになっているRAGパイプラインを改善したい開発者
- 応答速度よりも正確性・網羅性を優先したいQA用途
