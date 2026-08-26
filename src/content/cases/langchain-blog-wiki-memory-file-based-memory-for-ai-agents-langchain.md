---
type: opinion
title: エージェント記憶を圧縮ファイルで永続化する「wikiメモリ」パターン
title_original: Wiki Memory
industry: cross-industry
cloud: []
patterns:
- context-engineering
- memory-consolidation
- rag
- document-processing
components:
- DeepWiki
- AutoWiki
- LangMem
- Letta
- Mem0
- Zep
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/wiki-memory
published_at: '2026-08-26'
---

## 概要

LangChainのHarrison Chaseが、ログやドキュメントなどの生データをエージェントが圧縮し、ファイルとして永続化する「wikiメモリ」という共通パターンについて論じている。クエリ時に生チャンクを検索するRAGとは異なり、wikiは事前にドメイン知識を高レベルに統合・構造化しておく点が異なる。DeepWikiやAutoWikiなどの実例を挙げつつ、あらゆるドメインでこの永続的な知識層が有用になり得ると主張している。

## 設計のポイント

- 生データ（ログ・ノート・コード・Slackスレッドなど）を直接エージェントに渡すのではなく、専用のエージェントが密なagent-readableな表現に圧縮してから利用する
- RAGのようにクエリ時に生チャンクを検索するのではなく、事前に高レベルな統合結果を作成・維持しておくことで、エージェントが毎回ドメイン構造を再発見する手間を省く
- 圧縮後の表現形式としてファイルを採用することで、検査可能性・編集可能性・バージョン管理のしやすさを確保する
- wikiの維持自体もエージェントに担わせ、ソースの更新に追従して継続的に最新化する

## 使いどころ

- コードベースの理解を助けるDeepWikiやAutoWikiのような、人間とコーディングエージェント双方向けのドキュメント生成
- 退職などで失われがちな専門家（研究者など）の暗黙知を、実験ノートや行動記録から組織知として保存したい場合
- 会話の短期状態やユーザー嗜好、高頻度イベントログではなく、長期的に安定したドメイン知識を扱いたい場面
