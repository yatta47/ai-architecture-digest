---
type: case
title: Claude Opus 4.6のプレリリーステストで顧客4社が体験した性能の飛躍
title_original: 'Behind the model launch: What customers discovered testing Claude Opus 4.6 early'
company: Harvey / bolt.new / Shopify / Lovable
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
- llmops
components:
- Claude Opus 4.6
- BigLaw Bench
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early
published_at: '2026-02-09'
---

## 概要

Anthropicの新モデルOpus 4.6は正式リリース前の数日間、Harvey・bolt.new・Shopify・Lovableといった顧客企業に先行アクセスを提供し、各社が自社ベンチマークと実務タスクの両面で検証した。Harveyの法務ベンチマークBigLaw Benchでは初めて90%を突破し、bolt.newは過去5回失敗していたバグを一発診断、ShopifyはTypeScriptからRubyへの大規模移植を単発で完遂するなど、各社は推論の深さと指示追従性の顕著な向上を報告した。

## 設計のポイント

- 定量ベンチマーク（BigLaw Benchや自動evalプラットフォーム）と、実務担当者による定性的な「vibe check」を併用し、両者が一致する場合を強いシグナルとして扱う
- 他社の印象に引きずられないよう専用Slackチャンネルを立てつつ初期の所感を意図的に共有しないなど、バイアスを排除する運用を取る
- 早期アクセスでの率直なフィードバックが実際に最終モデルへ反映される仕組みにすることで、顧客が本音の課題報告をする動機を維持する
- 既存の自動評価基盤（ビルド品質・バグ修正・コードベース理解等）と手動ストレステストを組み合わせ、モデル更新のリスクを本番投入前に洗い出す

## 使いどころ

- 新モデルのリリース前に、法務・コーディング・ファイナンスなど専門領域の顧客に先行検証させ品質を保証したいAIベンダー
- 過去のモデルで解決できなかった実際の失敗事例をリグレッションテストとして使い、モデル更新の実質的な進歩を確認したい開発チーム
- 自動ベンチマークだけでなく、現場の専門家による主観的な使用感を品質判断に組み込みたい場合
