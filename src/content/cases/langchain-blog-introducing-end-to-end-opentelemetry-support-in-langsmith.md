---
type: announcement
title: LangChain/LangGraphからLangSmithまで貫くEnd-to-EndのOpenTelemetryパイプライン
title_original: Introducing End-to-End OpenTelemetry Support in LangSmith
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- LangSmith
- LangChain
- LangGraph
- OpenTelemetry
- Datadog
- Grafana
- Jaeger
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/end-to-end-opentelemetry-langsmith
published_at: '2026-06-15'
---

## 概要

LangSmithはこれまでバックエンドでのOTel取り込みのみ対応していたが、SDK自体にネイティブなOpenTelemetry計装を組み込み、LangChain/LangGraphの計装からLangSmith SDK、LangSmithプラットフォームまで一気通貫のOTelパイプラインを提供するようになった。Datadog・Grafana・Jaegerなど既存の観測基盤との相互運用性も確保する一方、性能を優先する場合はLangSmithネイティブのトレース形式を推奨している。

## 設計のポイント

- LangChain/LangGraphの自動計装からLangSmith SDKでのOTel変換、LangSmithプラットフォームでの可視化まで三層のパイプラインとして設計する
- 分散トレーシングのcontext伝播により、マイクロサービスをまたいだ関連スパンを1つのトレースとして追跡できるようにする
- Datadog/Grafana/Jaegerなど既存の観測ツールとLangSmithを併用できる相互運用性を確保する
- 汎用フォーマットであるOTelはオーバーヘッドが高いため、LangSmith単体運用時は専用のネイティブ形式を推奨するという使い分けを明示する

## 使いどころ

- マイクロサービス構成の中でLLMアプリと既存インフラの監視を1つの観測基盤に統合したいプラットフォームチーム
- 複数の観測ツールを併用しつつLLM特有のトレースも一元管理したい組織
