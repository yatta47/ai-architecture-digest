---
type: guidance
title: MCP経由で工場データをLLMエージェントに安全に開放するPlant Copilot
title_original: Agentic AI for the reference solution
industry: manufacturing
cloud:
- azure
patterns:
- ai-agent
- context-engineering
- guardrails
components:
- Model Context Protocol (MCP)
- Azure Container Apps
- Azure Data Explorer
- Microsoft Fabric Eventhouse
- Microsoft 365 Copilot
- Microsoft Copilot Studio
- Microsoft Foundry
- Azure IoT Operations
- Microsoft Entra ID
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/agentic-ai-for-the-solution
published_at: '2026-07-30'
---

## 概要

ISA-95資産階層とOPC UA情報モデルで正規化された工場データを、読み取り専用のMCPサーバー「Plant Copilot」を介してLLMエージェントに公開し、資産名や現在値を根拠に自然言語で回答できるようにする。エージェントはDBに直接触れず、I3X APIとMCPツールのみを通じて動作するため、回答の追跡可能性とテナントガバナンスを両立する。

## 設計のポイント

- LLMに事実を記憶させるのではなく、ISA-95階層・OPC UA型情報・現在値/履歴を取得するツールを与えて『推測』を防ぐ
- エージェントはDBを直接クエリせず、読み取り専用のMCPサーバーとI3X層経由でのみデータにアクセスさせ、認証とデータ形状を強制する
- MCPという標準プロトコルでツールを実装することで、Microsoft 365 CopilotやFoundryなど複数のエージェントホストに同じサーバーを再利用できる
- カスタムMCPコネクタの登録や公開はテナント管理者のポリシー（DLP・Conditional Access等）に委ね、コード側では迂回できないようにする

## 使いどころ

- 工場フロアの現場管理者が『work cell 3の現在のエネルギー消費は？』のような質問を自然言語で行い、根拠付きの回答を得たい場面
- 複数の生産ラインを横断してスループットや稼働状況を素早く把握したいプラント運用チーム
- 将来的に読み取り専用の問い合わせから、承認を伴うアクション実行エージェントへ安全に拡張したいIoTソリューション設計者
