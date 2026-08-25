---
type: case
title: OpenWikiにおける根拠付きクレームで実現する自己修正型エージェントメモリ
title_original: Building Self-Correcting Memory in OpenWiki
company: LangChain
industry: cross-industry
cloud: []
patterns:
- memory-consolidation
- eval
- context-engineering
- ai-agent
components:
- OpenWiki
- Open Knowledge Format (OKF) v0.2
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/self-correcting-memory-openwiki
published_at: '2026-08-25'
---

## 概要

LangChainのOpenWikiは、Wikiページの各事実主張(claim)にコード上の根拠(evidence)とそのバージョンを紐付けて永続化し、根拠側のコードが変更されるとそのclaimを自動的に「stale」と判定する自己修正型メモリ機構を実装した。stale判定はモデル呼び出し無しの決定的なチェックで、エージェントが該当ページを更新する際にstaleなclaimを提示され再検証・修正する。commit列を再生する評価では、stale率が3.5%→0.5%、幻覚(hallucinated)claimが0.7%→0%に低減した。

## 設計のポイント

- 各claimに『主張文』と『コード上の根拠(evidence)への参照』をセットで記録し、テキストの塊ではなく個々の事実として真偽を追跡する
- 根拠側のバージョンを比較するだけの決定的(モデル呼び出し無し)なstaleness検知にすることで、claim数が増えても更新コストはコード変更量にしか比例しない
- stale判定は明示的なステータスフラグではなく『保存済みの根拠バージョンとの差分』で表現し、再検証されるまで不確実性を保持し続ける
- 詳細なclaim/evidenceは内部サイドカーに、ポータブルなMarkdown側にはOKFの信頼サマリ(生成者・検証履歴)だけを露出させ、責務を分離する

## 使いどころ

- コードの変更に追従してドキュメント（Wiki/仕様書）を書くAIエージェントの、ハルシネーションや陳腐化した記述を抑えたい場合
- エージェントの長期記憶が『何を信じているか』と『なぜそれを信じているか』を区別して管理したいメモリシステム設計
- 自動生成ドキュメントの信頼性を定量評価（stale率・hallucination率）したいAIプラットフォームチーム
