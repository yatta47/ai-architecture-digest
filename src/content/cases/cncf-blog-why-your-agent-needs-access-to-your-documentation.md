---
type: case
title: 1,192件の会話が示した、エージェントにドキュメント検索が不可欠な理由
title_original: Why your agent needs access to your documentation
company: kapa.ai
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- context-engineering
components: []
outcome:
  type: quality
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/21/why-your-agent-needs-access-to-your-documentation/
published_at: '2026-07-21'
---

## 概要

自社製品に組み込んだ分析エージェントの1,192件の会話ログを分析したところ、30種類のネイティブツールよりもドキュメント検索ツール(search_knowledge_base)が最も多く使われていた。ドキュメント検索は、ネイティブツールで答えられない質問へのフォールバック、回答への文脈付与に加え、エージェント自身がどのネイティブツールを使うべきかを学ぶための「計画補助」としても機能していた。

## 設計のポイント

- ネイティブツールが「今何が真か」を答えるのに対し、ドキュメント検索は「それが何を意味するか」を答える役割分担になる。
- ドキュメント検索を、ユーザーへの回答だけでなく、エージェントが正しいネイティブツールを選ぶための事前調査ステップとしても使わせる。
- 存在しない機能(例:感情フィルタ)を尋ねられた際、ドキュメントから代替の実現方法(ダウンボート等)を発見し、正しいツール呼び出しにつなげられる。

## 使いどころ

- 多数のネイティブツールを持つ製品組み込みエージェントで、スキーマに一致しない自然言語の質問を減らしたい場合。
- ドキュメントが大規模かつ更新頻度が高いOSS/プラットフォームプロジェクトのサポート自動化。
