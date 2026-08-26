---
type: announcement
title: LangSmith LLM Gateway、本番エージェント向けに支出上限・レート制限・モデルフォールバック・PII redactionを一元制御
title_original: 'LangSmith LLM Gateway: runtime controls for production agents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- multi-model-routing
- cost-optimization
- guardrails
components:
- LangSmith
- LangSmith LLM Gateway
- OpenAI
- Anthropic
- Fireworks
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-llm-gateway-runtime-controls-for-production-agents
published_at: '2026-08-26'
---

## 概要

LangChainはエージェントとモデルの間に立つ中央ガバナンス層「LangSmith LLM Gateway」をパブリックベータで公開した。組織・ワークスペース・APIキー・ユーザーの4階層で支出上限とレート制限を設定でき、上限到達時は402エラーを返す。プロバイダ障害時のモデルフォールバックやPII・シークレットのリダクション、テナント単位の課金分離もサポートし、OpenAI・Anthropic・Fireworksなど複数プロバイダをBYOKで一元的にルーティングできる。

## 設計のポイント

- 組織・ワークスペース・APIキー・ユーザーの4階層で時間区切りの支出上限を設定し、超過時にエージェント側へ402エラーを明示的に返す
- カスタムリクエストヘッダーでエンドカスタマーを識別し、単一APIキーを共有しながらテナントごとに支出・レート制限を分離するマルチテナント設計
- プロバイダ障害やレート制限時のモデル/ホストへのフォールバックルールをアプリごとの実装から切り離し、ゲートウェイ側で一元定義
- ゲートウェイのブロック・制御イベントをLangSmithのトレースにメタデータとして記録し、本番トラフィックでの制御挙動を後から追跡できるようにする

## 使いどころ

- 公開エージェントなど、コスト暴走やレート超過が直接ビジネスリスクになる本番エージェントを運用するチーム
- マルチテナントSaaSやリセラーが、顧客ごとの利用状況・支出を単一APIキー経由で一元管理したい場合
- 複数のモデルプロバイダやオープンウェイトモデルを併用しつつ、ガバナンスとフォールバックを統一管理したいAIプラットフォームチーム
- PIIや機密情報を含むリクエストをモデルプロバイダに送信する前にリダクションしたいエンタープライズ組織
