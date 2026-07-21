---
type: case
title: Agentforceにおける決定論的な多言語ローカライゼーション制御基盤
title_original: How Agentforce Prevents Language Drift in 600K Daily Multilingual AI Workflows
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- multilingual-localization
- ai-agent
- context-engineering
- guardrails
components:
- Agentforce
- Lingua
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-agentforce-prevents-language-drift-in-600k-daily-multilingual-ai-workflows/
published_at: '2026-06-23'
---

## 概要

Salesforceは34言語(+ベータ26言語)を展開するAgentforceで、承認済み言語リストを与えてもLLMが誤った言語で応答する「言語ドリフト」問題に直面した。そこでLLMに言語選択を委ねず、Rustベースの高速言語検出ライブラリLinguaでp95約3〜4msの決定論的な言語検出を行い、その結果を「Localization Context」としてプランナー・検索・アクション・下流サービス全体で共有する単一の真実源とすることで、1日60万件超の言語検出を一貫した挙動で処理している。

## 設計のポイント

- 言語選択をLLMの確率的推論に委ねず、推論開始前にRustベースの検出ライブラリLinguaで言語を決定論的に確定させ、モデルはその言語制約の中で生成させる
- 検出した言語を『Localization Context』として一度確立し、プランナー・検索・アクション実行・下流サービスが個別に言語を推測せず同じ言語状態を参照する単一の真実源とする
- 各アクション/サービスが独自に言語ローカライズやフォールバック戦略を実装する分散モデルは断片化と応答内の言語混在を招くため、中央集権的な言語ポリシー適用に統一する
- 会話途中での言語切り替えに追従できるよう、Localization Contextを静的設定ではなくワークフロー実行中に進化するライブな共有状態として設計する

## 使いどころ

- 多数の言語に対応するマルチリンガルAIエージェントで、承認済み言語を指定してもLLMが意図せず別言語で応答してしまうドリフトを防ぎたい場合
- プランナー・検索・並列実行される複数アクションが動的に応答を組み立てる分散エージェントアーキテクチャで、応答全体の言語一貫性を保証したい場合
- エンタープライズ顧客に対し、AIエージェントの言語選択の挙動を監査可能・説明可能にし、カスタマー側の言語ポリシーを確実に強制したい場合
- 会話の途中でユーザーが使用言語を切り替えるようなリアルタイム性の高い対話システムで、低遅延(数ミリ秒オーダー)の言語検出と状態伝播が求められる場合
