---
type: case
title: トレースを読んで自らPRを出すLLMコスト削減エージェント
title_original: Agent cost management is about more than the model
industry: cross-industry
cloud: []
patterns:
- cost-optimization
- llmops
- context-engineering
- multi-agent-orchestration
components:
- Arize AX
- LangGraph
- GitHub
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/using-managed-agents-to-optimize-llm-costs/
published_at: '2026-09-01'
---

## 概要

Arize AXが提供するCost Agentは、トレースを読んでスパンごとの支出をランク付けし、無駄なコストの原因を関数レベルまで特定してPRを起票する。LangGraph製のマルチエージェント金融アシスタントへの適用例では、巨大なWebページ取得結果が会話履歴に残り続けて後続呼び出しを膨張させている問題などを発見し、6件の修正で月額コストの35〜40%を削減した。

## 設計のポイント

- コスト診断はスパン単位の支出ランキングと品質スコアの相関から『割に合わない処理』を機械的に特定する
- リポジトリ接続を持たせることで、テレメトリ診断に加えて実装コードを読み、直接PRとして修正案を出す
- ツール呼び出しの戻り値が会話状態に蓄積され後続ステップ全てに再送されるコンテキスト膨張を優先的に洗い出す
- モデルダウングレードを最初の手段にせず、キャッシュ未活用やプロンプト設計の粗さなど根本原因を先に潰す

## 使いどころ

- 本番稼働中のマルチエージェントシステムでLLMコストが非線形に増大しているチーム
- コスト最適化の担当が定まらず後回しになっているエージェント運用チーム
- トレースからコード修正まで自動化してレビューコストを抑えたいプラットフォームチーム
