---
type: case
title: 行動データ基盤とガバナンス統制で実現するハイパーパーソナライズ銀行体験
title_original: How Discovery Bank Delivers Hyper-Personalized Banking at Scale
company: Discovery Bank
industry: financial-services
cloud: []
patterns:
- decision-execution
- guardrails
- ai-agent
components:
- Databricks Data and AI Platform
- Delta Lake
- MLflow
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-discovery-bank-delivers-hyper-personalized-banking-scale-behavioral-ai-governed-data-and
published_at: '2026-09-01'
---

## 概要

Discovery Bankは決済・支出・デジタル行動などのシグナルをDatabricks上で統合し、再利用可能な行動データプロダクトとして次善アクション(NBA)モデルや不正検知TRUST™アラートを構築した。単一モデルではなく共有・統治された意思決定レイヤーを各チャネルから使い回す設計により、顧客エンゲージメント施策の効果が40%向上し、データパイプライン開発が20倍、データプロダクト作成が5倍高速化した。

## 設計のポイント

- チャネル横断で使う意思決定ロジックを一つの共有レイヤーに集約し、活性化するチャネルとは分離する
- 行動データを特徴量・スコア・予測などの再利用可能なデータプロダクトとして一度作り、複数ユースケースに権限制御付きで供給する
- 次善アクションは送客量の最大化ではなく、その時点でその顧客に本当に有用な提案かどうかを基準に選ぶ
- 不正検知は既知パターン照合に加え、個人の行動基準からの逸脱度を評価するモデルで補強する

## 使いどころ

- 顧客ごとの行動データから次善アクションを導きたい金融機関のパーソナライゼーションチーム
- 複数チャネル・複数ユースケースでモデルやスコアを重複開発せず再利用したいデータ基盤チーム
- パーソナライズ施策と不正防止・ガバナンスを同一データ基盤上で両立させたい金融サービス企業
