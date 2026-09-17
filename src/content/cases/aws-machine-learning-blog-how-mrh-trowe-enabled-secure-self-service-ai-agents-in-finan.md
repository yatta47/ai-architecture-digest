---
type: case
title: ドイツの保険ブローカーMRH Troweの安全なセルフサービスAIエージェント
title_original: How MRH Trowe enabled secure self-service AI agents in financial services
company: MRH Trowe
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- guardrails
- context-engineering
- cost-optimization
components:
- Strands Agents
- Amazon Bedrock AgentCore
- LibreChat
- Microsoft Entra ID
- Microsoft Teams
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-mrh-trowe-enabled-secure-self-service-ai-agents-in-financial-services/
published_at: '2026-09-17'
---

## 概要

ドイツの商工保険ブローカーMRH Troweは、Strands Agents・Amazon Bedrock AgentCore・LibreChatを組み合わせ、規制業界に求められるデータ主権とガバナンスを保ちながら約400人の従業員にセルフサービスのAIエージェントを提供した。導入初月で本番稼働に達し、初期コストは1シートあたり約14ドル、ライトサイジングとスケジューリングによりインフラコストを約40%削減する道筋も示した。

## 設計のポイント

- LibreChatがMicrosoft Entra IDで認証したユーザーIDをサーバー側でエージェントに渡し、各従業員が自分自身のカレンダーや議事録データにしかアクセスできないようにした。
- エージェント・モデル・データ処理をAWS欧州(フランクフルト)リージョン内に限定し、ドイツ国内でのデータ保持要件を満たした。
- AgentCoreのセッション単位の分離(コンピュート/ファイルシステムレベル)により、規制業界に必要な安全性を確保しつつStrands Agentsの開発の柔軟性を維持した。
- 従量課金のAgentCoreとLibreChatのトークン予算機能により、利用拡大に応じたコストの透明性を確保した。

## 使いどころ

- 金融・保険など規制の厳しい業界で、シャドーAIを防ぎつつ従業員に自由にエージェントを作らせたい企業。
- 会議の議事録作成など、繰り返し発生する定型業務をAIエージェントに任せたい現場。
- 従業員ごとのID連携に基づき、機密性の高い社内データへのアクセス範囲を厳密に制御したいシステム。
