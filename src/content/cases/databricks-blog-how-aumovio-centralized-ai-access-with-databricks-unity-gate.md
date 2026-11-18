---
type: case
title: AUMOVIOがLLMアクセスをUnity Gatewayに一本化
title_original: How AUMOVIO centralized AI access with Databricks Unity Gateway
company: AUMOVIO
industry: manufacturing
cloud: []
patterns:
- llm-gateway
- guardrails
- cost-optimization
components:
- Databricks Unity Gateway
- Microsoft Entra ID
- Databricks
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-aumovio-centralized-ai-access-databricks-unity-gateway
published_at: '2026-11-18'
---

## 概要

AUMOVIOはチームごとに乱立したLLMアクセス経路を、1つの中央AIゲートウェイに統合した。既存のデータ基盤、Entra ID連携、ガバナンスの観点からUnity Gatewayを選び、利用の可視化、コスト帰属、承認・ログ・ガードレールの共通化を進めた。

## 設計のポイント

- ゲートウェイを自作せず、運用負荷を理由に既存データ基盤上のサービスを採用する。
- Entra IDトークン交換でAPIキー配布なしに接続し、ID失効でアクセスも終了させる。
- 利用・コスト・ガバナンスを単一経路に集約する。

## 使いどころ

- 複数部門が個別にLLMを利用し管理が分散している大企業。
- LLMコストをチーム別に配賦したい情報システム部門。
