---
type: guidance
title: タスク成功あたりコストで測るAIモデルベンチマーク:Kimi K3・GPT-5.5他10モデル比較
title_original: 'Cost per successful task: Benchmarking Kimi K3, GPT-5.5, and 8 more AI models'
company: Arize
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- eval
- cost-optimization
components:
- Kimi K3
- GPT-5.5
- gpt-oss-120b
- Gemini 3.1 Flash Lite
- Claude Sonnet 5
- Terminal-Bench
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/cost-per-successful-task-ai-model-benchmark
published_at: '2026-07-23'
---

## 概要

ArizeとFireworksが4プロバイダ10モデルをTerminal-Bench由来の実タスク2,400回分で検証し、トークン単価ではなく「タスク成功あたりコスト」で比較した。簡単なタスクではフロンティアモデルの追加コストに見合う価値はなく、難しいタスクではオープン/クローズド問わず最上位モデルしか通用しないという知見を示す。

## 設計のポイント

- コスト評価指標をトークン単価ではなく「全試行の総コスト÷成功回数」とし、リトライ・失敗・タイムアウトを含めた実質コストで比較する
- タスク難易度別に成功率を分解すると、易しいタスクではフロンティアモデルの追加コストに見合う価値がなく、難しいタスクでは低コストモデルが急激に脱落する
- モデル差し替えをOpenAI互換API経由の1コード経路で行い、エージェント側のスキャフォールディングを最小限にしてコストをモデル起因に限定する
- 採点はエージェント終了後にタスク付属のテストスイートをコンテナ内で実行する決定的な自動判定とする

## 使いどころ

- タスク難易度に応じて安価モデルとフロンティアモデルにルーティングする仕組みを設計したいチーム
- モデル選定をベンチマークのラベル(オープン/クローズド)ではなく自社ワークロードの実測コストで判断したい場合
