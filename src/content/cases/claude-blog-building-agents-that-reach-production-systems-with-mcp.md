---
type: guidance
title: エージェントを本番システムに接続する３つの方式とMCPが選ばれる理由
title_original: Building agents that reach production systems with MCP
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- llm-gateway
components:
- MCP
- Claude
outcome:
  type: reliability
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
published_at: '2026-04-22'
---

## 概要

エージェントを外部システムに接続する方法として直接API呼び出し・CLI実行・MCPの3方式を比較し、それぞれが向くシーン・限界を整理する。直接API呼び出しはM×N問題を生み、CLIはローカル環境限定になりがちなため、認証・発見・意味論を標準化するMCPが本番運用のエージェント連携で選ばれやすいと説明する。

## 設計のポイント

- 1エージェント対1サービスなど小規模な連携では直接API呼び出しで十分で、過剰設計を避ける
- ローカル環境やサンドボックスコンテナ内の軽量な統合にはCLI実行が高速で適している
- サービス数が増える・複数のエージェント基盤から同じシステムに繋ぎたい場合はMCPで共通層を1つ用意しM×N問題を避ける

## 使いどころ

- 単発のプロトタイプや1対1連携しか必要ないチームは直接API呼び出しから始めるべき場面
- 複数の本番エージェントプラットフォームから同じ社内システム群に安全にアクセスさせたい場面
