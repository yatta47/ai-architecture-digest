---
type: case
title: 人間ラベルでエージェント評価を整合させるCustom Viewのループ
title_original: 'Alignment is a human-AI workflow: how Custom Views make agent review possible'
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- human-in-the-loop
- llmops
- ai-agent
components:
- Arize AX
- Alyx
- Arize Phoenix
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/alignment-is-a-human-ai-workflow-custom-views/
published_at: '2026-10-09'
---

## 概要

ArizeはAIアシスタントAlyxの自動評価を人間の判断と揃えるため、本番セッションをラベリングキューへサンプリングし、専用Custom Viewで文脈とルーブリックを一画面に集約してレビューする。ラベルと評価器の不一致を修正し、セッション単位の監視ビューで本番を追う循環を回している。

## 設計のポイント

- 成功・失敗・判断が割れるケースを混ぜてキューに入れ、人間ラベルを評価器検証の正解にする。
- トランスクリプト、ツール列、エラー、成果物、ルーブリックを一画面にまとめ、証拠を落とさず要約せずにレビューを速く一貫させる。
- 不一致は評価基準・ルーブリック・表示情報不足のいずれが原因かを切り分けて修正する。
- 監視で矛盾や回帰を見つけたセッションをラベリングへ戻すループにする。

## 使いどころ

- エージェントの自動評価の信頼性を高めたいLLMOpsチーム。
- ドメイン専門家に観測基盤の知識なしでセッションをレビューさせたい場面。
- 本番エージェントの品質を継続監視したい運用者。
