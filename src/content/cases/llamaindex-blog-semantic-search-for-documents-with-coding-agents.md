---
type: case
title: コーディングエージェント＋セマンティック検索ツールのドキュメント探索ベンチマーク
title_original: 'SemTools: Are Coding Agents (Plus Unix Tools) All You Need?'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- full-text-search
- ai-agent
- document-processing
- context-engineering
components:
- SemTools
- LlamaParse
- Claude Code
- Gemini CLI
- model2vec
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/semtools-are-coding-agents-all-you-need
published_at: '2026-07-19'
---

## 概要

LlamaIndexは、Claude CodeやGemini CLIなどのコーディングエージェントにSemTools（LlamaParseベースのparseと軽量埋め込みによるsearch）を与えることで、grep/findだけの場合よりドキュメント探索の質が上がるかを1,000本のArXiv論文と25問のベンチマークで検証した。検索ツールを与えたエージェントはより詳細で精度の高い回答を、より少ないツール呼び出しで生成できた一方、大規模コーパスでの検索速度には課題が残った。

## 設計のポイント

- model2vecの軽量な静的埋め込みで『あいまいなセマンティックキーワード検索』を実現し、grep/findを補完するCLIツールとして提供する
- コーパスをby_author/by_category/by_dateなど複数のシンボリックリンク構成で整理し、エージェントが慣れたファイルシステム操作で探索できるようにする
- 厳密な正解データが用意しづらい大規模データセットでは、エージェント自身に根拠文書を再確認させる『vibesベース』評価で妥当性を検証する

## 使いどころ

- 大量のテキストコーパスに対してgrepだけで十分か、セマンティック検索ツールへの投資が必要か判断したいチーム
- 数千件の文書間の関係性や時系列変化を横断分析させたいリサーチ/ナレッジワーカー向けエージェント
