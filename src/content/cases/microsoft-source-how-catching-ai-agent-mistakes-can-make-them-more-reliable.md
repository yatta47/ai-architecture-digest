---
type: case
title: 最終状態を検証するエージェント評価基盤ThinkingBoxと、その検証を報酬にした強化学習
title_original: The check that catches agent failures can also train them
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- eval
- reinforcement-learning
- ai-agent
- human-in-the-loop
components:
- ThinkingBox
- ThinkingBox-Bench
- Qwen3.8-27B
outcome:
  type: reliability
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://commandline.microsoft.com/thinkingbox-part-two-expanded-model-evals-reinforcement-learning-rewards/
published_at: '2026-11-07'
---

## 概要

MicrosoftのThinkingBoxは、隔離した環境でエージェントを動かし、発話ではなく最終的なデータベース状態を検査して成否を判定する評価基盤である。18モデルの評価で平均成功率と繰り返し成功率が別の順位になることを示し、同じ検証を報酬にした強化学習で27Bモデルの全回成功タスクを38から107へ増やした。

## 設計のポイント

- エージェントの報告ではなく、操作後のレコードを実行可能な検査で判定し、完了したように見える失敗を検出している。
- pass@1とpass^20を併用し、人がレビューする用途と無人で本番を更新する用途で指標を使い分けている。
- 失敗の多くはツール利用の失敗であるため、エラー分類による再試行の選別、ツール面の絞り込み、高コストな変更への人手承認を対策として挙げている。
- 評価に使う検証を終端状態の報酬として強化学習に流用し、ベンチマーク外のタスクでの訓練で方針違反を減らしている。

## 使いどころ

- エージェントが本番レコードを無審査で更新する運用で、信頼性の指標を選ぶ場面。
- モデル選定時に、平均精度ではなく再現性とコストを併せて比較したいチーム。
- 社内ポリシーを守らせるため、環境ベースの検証を評価と訓練の両方に使いたい場面。
