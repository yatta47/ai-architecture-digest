---
type: announcement
title: Arize Phoenixがモデル価格カタログをリリース間で自動更新
title_original: Arize Phoenix now updates model prices automatically
company: Arize
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
components:
- Arize Phoenix
- LiteLLM
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/phoenix-automatic-model-pricing-updates/
published_at: '2026-11-02'
---

## 概要

Phoenixは、トレース内のLLM呼び出しコストを計算する価格カタログを、バックグラウンドで約1日ごとにGitHubから取得して更新するようになった。カタログはLiteLLMの価格表から生成され、再起動やアップグレードなしで新しいモデルの料金が反映される。

## 設計のポイント

- 起動直後と以後約1日ごとに新しいカタログを確認し、生成日を比較して新しい場合のみ適用する。
- 更新後の料金は、価格キャッシュの更新後に記録される新しいスパンから反映される。

## 使いどころ

- LLMのコストをトレース単位で追跡している運用チーム。
- 新モデルの登場に合わせて料金設定を手動更新する手間を省きたい場合。
