---
type: opinion
title: 長時間稼働する『文書エージェント』はチャットではなく受信箱型UIで人間と協働すべき
title_original: Long-Horizon Document Agents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
- document-processing
components: []
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/long-horizon-document-agents
published_at: '2026-07-19'
---

## 概要

既存の文書AIは『制約されたバッチ処理(IDP/RPA)』か『短時間で終わるチャット型エージェント』のどちらかに偏っており、人間が実際に行う文書作業(調査・下書き・レビュー往復・継続更新)のような長時間・反復的・協働的な作業には対応できていないと指摘する。チャットに代わり、イベントで再起動し永続タスクバックログを持つ『エージェント受信箱』というUIを提案している。

## 設計のポイント

- エージェントの起点をユーザーのチャット送信だけでなく、レッドライン到着や文書編集、期限接近などのイベントに拡張する
- 今すぐ終わらない作業をため込む永続タスクバックログを持たせ、全てを即時に人間へエスカレーションしない設計にする
- 対話スレッドではなく『下書き完成、レビュー待ち』のような状態付きタスク一覧(受信箱UI)として人間とのインターフェースを再設計する

## 使いどころ

- 散在するSharePoint文書からFAQやナレッジベースを継続的に最新化したいチーム
- データルームの更新に応じて投資メモを自動で更新し続けたいデューデリジェンス業務
- 契約書のレッドライン往復など、複数ラウンドの協働編集を伴う法務レビュー
