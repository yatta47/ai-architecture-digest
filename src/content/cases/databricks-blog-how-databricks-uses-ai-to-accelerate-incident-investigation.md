---
type: case
title: 1500超のKubernetesクラスタを横断してAIが障害調査を主導するDatabricksのAI SRE
title_original: How Databricks uses AI to accelerate incident investigation
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- root-cause-analysis
- human-in-the-loop
components: []
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-databricks-uses-ai-accelerate-incident-investigation
published_at: '2026-08-24'
---

## 概要

Databricksは、インシデント発生と同時に自動着手する障害調査エージェント「AI SRE」を構築し、150以上のチーム・2000件以上/日の調査に展開している。プラットフォームヘルスチェック・サービスレベル分析・チーム固有のエージェント化されたランブック実行という3つの調査トラックを並列に走らせ、診断結果を必ず検証可能な生データに紐づけることでブラックボックス推論を避け信頼性を確保している。

## 設計のポイント

- 自動トリアージ(プラットフォームヘルス・サービス分析・ランブック実行を並列実行)と、対話的な深掘り調査という2つの体験を組み合わせる
- 各チームが自分たちのランブックを「スキル」としてエージェント化できる共通プラットフォームを提供し、個別チームがドメイン知識を持ち込めるようにする
- 診断結果を常に検証可能な生の証拠(ログ・メトリクス・トレース)に直接リンクさせる「context-first」開発でブラックボックス推論を避ける
- まずインフラ層の異常(クラウド障害・ネットワーク・上流依存)を先に確認することで、アプリケーション層での見当違いな調査時間を削減する

## 使いどころ

- 多数のマイクロサービス・多数のチームで構成される大規模プラットフォームでオンコール対応の速度と一貫性を上げたい場合
- 経験豊富なエンジニアの暗黙知をランブックとして形式化し、組織全体にスケールさせたい場合
