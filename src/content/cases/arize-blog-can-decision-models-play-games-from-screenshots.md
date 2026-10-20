---
type: opinion
title: 画像対応の意思決定モデルはスクショからゲームを遊べるか
title_original: Can decision models play games from screenshots?
company: Arize
industry: other
cloud: []
patterns:
- eval
- multi-model-routing
components:
- Arize AX
- Clef Flash
- Liquid d1
- OpenAI Decisions
- Jev 1.14
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/can-decision-models-play-games-from-screenshots/
published_at: '2026-10-20'
---

## 概要

固定の選択肢に確率を返す意思決定モデルのうち画像対応のものを、三目並べ・マインスイーパ・Flappy Birdで8モデル比較した。結果は「まずまずだが優秀ではない」で、筆者自身が多くのAIを上回った。

## 設計のポイント

- 勝敗やスコアという決定的な判定でモデルを評価し、画像入力とテキスト入力の差も比較する。
- 意思決定モデルはツール選択やルーティング、停止判断などエージェント内の一手に向く。

## 使いどころ

- エージェント内の分岐判断に軽量モデルを採るかの検討。
- 画像入力の判断精度を自社で簡易評価したいチーム。
