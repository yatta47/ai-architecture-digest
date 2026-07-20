---
type: case
title: エージェント障害を検知するAIエージェント「Engine」を評価する内部ベンチマークIssueBench
title_original: IssueBench - How We Evaluate Engine
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- root-cause-analysis
- llmops
- ai-agent
components:
- LangSmith Engine
- Harbor
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/issuebench-how-we-evaluate-engine
published_at: '2026-07-20'
---

## 概要

LangChainは他のAIエージェントのトレースを監視し障害を検知・分類・グルーピングするLangSmith Engineを開発しており、その精度を測るために内部ベンチマークIssueBenchを構築した。IssueBenchはSREログ解析・ソフトウェア開発・カスタマーサポートの3ドメインにまたがる15タスクと15の失敗カテゴリを持ち、Harbor上でサンドボックス化された合成トレースとground truthラベルを用いてEngineの分類・カテゴリ付与・issue紐付け・新規issueグルーピングを採点する。ドメイン横断で同一の失敗カテゴリを評価することで、表面的なパターンの暗記ではなく抽象的な失敗モードの理解を検証している。

## 設計のポイント

- 15タスク×3ドメイン(SRE/ソフトウェア開発/カスタマーサポート)にわたり合成トレースとground truthラベルを用意し、Harbor上でサンドボックス化・再現可能な評価環境を構築する
- 分類(issue/no issue)・失敗カテゴリ付与・既存issueへの紐付け・新規issueグルーピングの4段階でエージェントの出力をスコアリングする
- クリーン(no-issue)なトレースの正しい識別も評価対象に含め、誤検出率が測定に混入しないようにする
- 同一の失敗カテゴリを異なるドメインのエージェントに対して繰り返しテストし、ドメイン固有の表面パターンではなく抽象的な失敗モードの理解を検証する

## 使いどころ

- 本番投入したエージェントのトレースを継続的に監視し、障害を自動検知・分類してチーム内の適切な担当者にルーティングしたいプラットフォームチーム
- プロンプトやモデルの変更が障害検知精度にどう影響するかを継続的に評価し、リグレッションを防ぎたいLLMOpsチーム
- 大量のエージェント実行ログから重複のないissueセットを生成し、デバッグ・テスト・修正の起点にしたい運用チーム
