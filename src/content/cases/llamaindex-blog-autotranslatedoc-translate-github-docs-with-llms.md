---
type: announcement
title: GitHubの技術文書を検証付きで多言語翻訳するAutoTranslateDoc
title_original: 'Bridging the Language Gap in Programming: Introducing AutoTranslateDoc'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- multilingual-localization
- document-processing
components:
- AutoTranslateDoc
- GPT-3.5
- GPT-4
- GitHub
- LlamaIndex.TS
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/bridging-the-language-gap-in-programming-introducing-autotranslatedoc-ccc93fbcd3a8
published_at: '2023-12-08'
---

## 概要

GitHubリポジトリのMarkdown文書を取得・分割してLLMで翻訳し、検証に失敗した箇所は再翻訳するCLIツールを公開した。翻訳履歴を保持して変更分だけを再翻訳できる。

## 設計のポイント

- 各チャンクに見出し階層を付けて翻訳し、文脈と構造を保つ。
- 長さ・見出し・リンク数・コードブロックの決定的チェックで脱落や捏造を検出する。
- 翻訳履歴をJSONで管理し、差分のみを再翻訳する。

## 使いどころ

- OSSや製品の文書を多言語展開したいメンテナー。
- 原文更新への追従コストを下げたい場面。
