---
type: announcement
title: Arize AXがOpenTelemetry GenAIセマンティック規約をネイティブサポートしトレース変換処理を不要に
title_original: Arize AX adds native support for OpenTelemetry GenAI semantic conventions
company: Arize
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
components:
- Arize AX
- OpenTelemetry
- OpenInference
- Microsoft Agent Framework
- CrewAI Studio
outcome:
  type: productivity
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/arize-ax-opentelemetry-genai-semantic-conventions/
published_at: '2026-08-11'
---

## 概要

Microsoft Agent FrameworkやCrewAI Studioなど、OpenTelemetryのGenAIセマンティック規約(gen_ai.*属性)を標準で発するフレームワークが増えているが、これまでArize AXで評価やコスト分析を行うには独自の変換プロセッサが必要だった。Arize AXは取り込み時にgen_ai.*属性をOpenInferenceの構造化フィールドに自動マッピングするようになり、モデル・プロバイダ情報、メッセージ、トークン使用量、ツール呼び出し、検索結果などをクライアント側の変換なしにそのまま評価・デバッグ・コスト分析に使えるようになった。

## 設計のポイント

- アプリ側でランタイムを制御できないマネージド/ローコードのエージェントプラットフォームでも、OTLPエンドポイントさえ向ければ観測可能にする
- 取り込み時に標準規約(gen_ai.*)を独自のOpenInferenceスキーマへ正規化し、下流の評価・分析ワークフローを変更せずに済ませる
- 分類に自信が持てないスパンはspan kindを未設定のままにし、誤った推測でデータを歪めない
- 既存のOpenInference属性が明示的に存在する場合はそちらを優先し、両規約が混在する環境でも矛盾なく扱う

## 使いどころ

- 自社が計装コードを制御できないマネージドエージェント基盤のトレースを観測したいプラットフォームチーム
- 複数フレームワークが異なるテレメトリ規約を吐く混在環境で一貫した評価・コスト分析をしたい場合
- OpenTelemetry標準への準拠を進めつつAI特有のトレース情報(トークン数、ツール呼び出し)も扱いたい場合
