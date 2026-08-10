---
type: opinion
title: EU AI Act対応をトレース・評価・監査ログのエンジニアリング実装に落とし込む
title_original: Demystifying the EU AI Act for AI product and engineering teams
industry: cross-industry
cloud:
- multi-cloud
patterns:
- eval
- guardrails
- llmops
- human-in-the-loop
components:
- Arize AX
- OpenTelemetry
- OpenInference
- Presidio
outcome:
  type: risk-compliance
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/demystifying-eu-ai-act-for-ai-product-and-engineering-teams/
published_at: '2026-08-10'
---

## 概要

EU AI Act対応をエンジニアリング視点で解説する記事。トレース・評価・アノテーション・CI連携・監査ログといった通常のAI運用基盤を、Art.12記録保持やArt.14人間の監督などの各条項に対応するエビデンスとして機能させる方法を、Arize AXを例にしたリファレンスアーキテクチャで示す。LLM judgeのスコアを鵜呑みにせず人間との合意率を検証することの重要性や、Digital Omnibusの猶予期間（16か月）を待つのではなく計装を今から始めるべきという主張が中心。

## 設計のポイント

- エージェント実行→リダクション用スパンプロセッサ→OTelコレクタ→ストレージ（EUリージョン/自社クラスタ）→オンライン/オフライン評価→レビューキュー→CIゲート→監視という順でパイプラインを構成し、記録が発生した時点でPIIを最小化する
- LLM judgeのスコアをそのまま信頼せず、代表的なキャリブレーションセットで人間との合意率を計測し、不一致ケースを継続的に検証する
- OpenInference/OpenTelemetryでエージェントの全トラジェクトリ（モデル呼び出し・ツール引数・検索結果・ハンドオフ）をトレースし、保持期間を意図的に設計する
- システムプロンプト変更・検索インデックス再構築・モデル更新・ツール追加などの変更履歴を記録し、『重大な変更』の判定根拠を後から追跡できるようにする

## 使いどころ

- EU域内でAIエージェント・製品を展開し、EU AI Actの記録保持・人間の監督義務に備える必要があるプロダクト/エンジニアリングチーム
- Responsible AIポリシーはあるが評価プログラムと接続されておらず、原則を数値化されたエビデンスに変換したい組織
- LLM judgeによる公平性・安全性スコアを意思決定に使う前に、その信頼性を検証したいチーム
