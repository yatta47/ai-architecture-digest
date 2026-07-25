---
type: case
title: Jeppesen(ボーイング)、統合エージェント基盤でエンジニアリング工数を大幅削減
title_original: Jeppesen, a Boeing Company, Saves 2,000 Engineering Hours with Unified Chat Framework Built on LlamaIndex
company: Jeppesen (a Boeing company)
industry: manufacturing
cloud:
- azure
- aws
patterns:
- ai-agent
- event-driven
- llmops
- policy-as-code
components:
- LlamaIndex Workflows
- Azure AI Search
- Qdrant
- Azure Cosmos DB
- Azure Table Storage
- Azure Cache for Redis
- Neo4j
- Databricks Data Mesh
- GraphQL
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/jeppesen-a-boeing-company-saves-2-000-engineering-hours-with-unified-chat-framework-built-on
published_at: '2026-07-19'
---

## 概要

Jeppesen（ボーイング傘下）は社内で乱立していたチャットボット開発を統合するため、LlamaIndexのイベント駆動エージェントワークフローを核とした社内フレームワーク『Unified Chatbot Framework(UCF)』を5〜7名の小規模チームで構築した。エージェント1件あたりの開発時間は512時間から64時間（約87%削減）に短縮され、10〜11の本番プロダクトに展開、既に1,792時間、全社展開後は年間約4,900時間の削減が見込まれている。

## 設計のポイント

- 硬直的なチェーン/グラフ型フレームワークではなく、セッション・状態管理を内蔵したイベント駆動ワークフローを基盤に選定する
- 約50行のコードとJSON設定ファイルでエージェントを組み立てられるテンプレート化により、セキュリティ・コンプライアンスを標準搭載する
- LLM・ベクトルDB・会話メモリストアを『持ち込み可（Bring-Your-Own）』にし、Azure/AWS/HuggingFaceやQdrant等を各チームが選択できるようにする
- GraphQL/SQL/REST/Neo4j/Databricks Data Meshなど標準ツールコネクタを共通提供し、チームごとの重複実装をなくす

## 使いどころ

- 複数チームが個別にチャットボット/エージェントを開発し重複やガバナンス負荷が生じている大企業
- エージェント開発時間を短縮しつつ、全社で一貫したセキュリティ・コンプライアンス水準を維持したい組織
