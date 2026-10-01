---
type: announcement
title: Alyxが長期メモリでセッションを跨いで作業を記憶
title_original: Alyx now remembers your work across sessions with long-term memory
company: Arize
industry: cross-industry
cloud: []
patterns:
- memory-consolidation
- context-engineering
- ai-agent
components:
- Alyx
- Arize AX
outcome:
  type: productivity
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/alyx-arize-ax-long-term-memory/
published_at: '2026-10-01'
---

## 概要

ArizeのAIエンジニアリングエージェントAlyxに、プロジェクト目標・規約・好み・過去の判断をセッション間で保持する長期メモリが追加され、Arize AXの全ユーザーで既定で有効になった。メモリはユーザーとArizeスペース単位で分離され、チームメイトや他スペースとは共有されず、チャットで確認・修正・削除できる。

## 設計のポイント

- 現在の設定やIDなど取得可能な情報はメモリに入れず、取得困難な意図や判断理由に絞る。
- メモリをユーザーとスペースの単位でスコープし、無関係な文脈の混入を防ぐ。
- チャットから確認・修正・削除できる操作を提供して利用者の制御を保つ。

## 使いどころ

- トレース調査後に別セッションで評価器を作る際、前提を再説明したくない場面。
- 評価・実験・プロンプト改善を複数セッションで継続するAIエンジニア。
