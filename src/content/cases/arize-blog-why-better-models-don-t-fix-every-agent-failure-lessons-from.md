---
type: opinion
title: エージェント障害はモデルでなくコンテキスト・評価・可観測性で直す（OpenAI Stuart Sy氏の知見）
title_original: 'Why Better Models Don''t Fix Every Agent Failure: Lessons From OpenAI'
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- context-engineering
- eval
- root-cause-analysis
- llmops
components: []
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/why-better-models-dont-fix-every-agent-failure/
published_at: '2026-08-25'
---

## 概要

OpenAIのStuart Sy氏へのインタビュー記事は、モデルの知能そのものよりも、コンテキスト（何を見せるか）とハーネス（どのツール・権限を与えるか）が本番エージェント障害のボトルネックになっていると指摘する。モデルを固定した上でコンテキスト・プロンプト・ツールを1つずつ変えて評価セットで検証する反復ループと、フィードバックやトレース失敗を1つのイベントモデルに集約してタクソノミー化し、クラスタから確定したものを評価ケースに昇格させる仕組みを紹介している。

## 設計のポイント

- モデルを差し替える前に『必要なドキュメント/状態/ツール結果が渡っていたか』『ツール呼び出しが失敗・タイムアウト・空応答をそのまま事実として扱っていないか』を確認する
- モデルを固定して変数を1つずつ変え、狭いラベル付き評価セットで改善したかどうかだけを基準に変更を採否する
- 最終出力のスコアだけでなく、ツール呼び出し回数・エラー率・レイテンシ・思考量などプロセス指標も評価対象にする
- 評価/レーティング/チケット/トレース失敗を単一のイベントモデルに集約し、既知の失敗から作った暫定タクソノミーでクラスタリングして新しい失敗モードを評価ケースに昇格させる

## 使いどころ

- 本番エージェントが低頻度（数十回に1回など）で静かに失敗し、集計指標には現れないバグを追跡したいチーム
- モデルのアップグレードだけでは解決しない障害を切り分けたいAIプラットフォーム/信頼性担当
- 大量のユーザーフィードバックやトレースから評価データセットを継続的に育てたい組織
