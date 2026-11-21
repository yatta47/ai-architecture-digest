---
type: announcement
title: OracleデータとMicrosoftの業務コンテキストをつなぐエージェント統合
title_original: Microsoft and Oracle bring agentic AI into flow of enterprise work
company: Microsoft / Oracle
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- data-federation
components:
- Oracle AI Database@Azure
- Microsoft Work IQ
- Microsoft Copilot
- Azure Monitor
- Azure Workload Center for Oracle
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/microsoft-and-oracle-bring-agentic-ai-into-flow-of-enterprise-work/
published_at: '2026-11-17'
---

## 概要

MicrosoftとOracleは、OracleのAI Database@Azure上の業務データと、Work IQが把握する会議やメールなどの文脈を、エージェントが横断して推論できる統合を発表した。ExcelやTeams、Copilotから利用できる。

## 設計のポイント

- データを移さずに近接配置したOracleデータベースを、エージェントの参照先として接続する。
- エージェントのデータアクセスを制御する権限を併せて提供する。
- ワークロード仮想インスタンスで構成要素を束ね、監視と運用エージェントにつなぐ。

## 使いどころ

- Oracleに基幹データを持つ企業がCopilotから業務データを扱いたいとき。
- Oracleワークロードの運用監視をエージェントで支援したいとき。
