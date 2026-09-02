---
type: case
title: MCPツール呼び出しの可観測性でAIエージェントの年間120万ドル浪費を1時間で解消
title_original: How we eliminated $1 million/year of wasted AI agent spend in one hour
company: Databricks
industry: other
cloud: []
patterns:
- ai-agent
- cost-optimization
- root-cause-analysis
- llm-gateway
components:
- Unity Gateway
- Genie One
- MCP
- OpenTelemetry
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-we-eliminated-1-million-year-wasted-ai-agent-spend-one-hour
published_at: '2026-09-01'
---

## 概要

Databricksは、社内のAIエージェント群が利用するMCPツールサーバーの不具合を、Unity GatewayのOpenTelemetryトレースとGenie One（自然言語でのデータ分析）を使って調査し、7件の小さなバグが年間約49.9万ドルのトークン浪費と1.2万エンジニア時間、合計で年間120万ドル相当の損失を生んでいたことを1時間で特定・修正した。原因の多くはツールの入力仕様が曖昧でLLMが妥当な値を推測して失敗し、不親切なエラーメッセージのために何度もリトライを繰り返していたことにあった。

## 設計のポイント

- Unity Gatewayが全MCPツール呼び出しに対し追加計装なしでOpenTelemetryトレース（ツール名・引数・エラー・トークン数・レイテンシ・セッションID）を自動記録する
- Genie Oneでトレーステーブルに自然言語で質問し、SQL作成やスキーマ調査の手間なく数分で『どのエラーが多発し、復旧に何ターン・いくらかかるか』を可視化
- ツールはLLMが自然に推測しがちな型（例: カンマ区切り文字列でなく配列）を許容し、失敗時は原因が一目でわかる自己説明的なエラーメッセージを返す設計にする
- 集計トークン支出だけでは使用量増加と誤解されるため、ツール・エラー・セッション単位で無駄なコストを特定できる粒度の可視化が必要

## 使いどころ

- 社内で多数のAIエージェントとMCPツールサーバーを運用し、静かなトークン浪費を疑っているプラットフォームチーム
- 集計コストダッシュボードだけでは原因が分からず、ツール障害起因のコストを切り分けたい組織
- MCPツールを設計する開発者が、エージェントのリトライループを減らし復旧時間を短縮したい場面
