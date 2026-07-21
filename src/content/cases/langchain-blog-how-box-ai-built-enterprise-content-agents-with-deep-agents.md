---
type: case
title: Boxの企業コンテンツエージェント、親子構造のDeep Agentsで動的に分業する
title_original: 'Building Box AI: How an Enterprise Content Platform Went AI-Native with Deep Agents'
company: Box
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- rag
- document-processing
- context-engineering
components:
- Deep Agents
- Box AI
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/building-box-ai-how-an-enterprise-content-platform-went-ai-native-with-deep-agents
published_at: '2026-06-15'
---

## 概要

Box AIは単一ドキュメントへのQ&Aから、企業内の膨大な文書横断で検索・統合・レポート生成を行うエージェント基盤へと進化する過程で、モデル非依存性と開発速度を重視しDeep Agentsを採用した。親エージェント（Global Agent）が意図を分類し必要に応じて子エージェントを動的に生成して並列に検索・分析・統合させる親子構造を採用し、固定的な専門サブエージェント構成だった前身より4倍速く出荷できるようになった。

## 設計のポイント

- 専門役割ごとに固定のサブエージェントを事前定義するのではなく、親エージェントが実行時に必要な子エージェントを動的に生成する構成にする
- 子エージェントをツールとして親から呼び出せる形にし、キーワード検索の実行も子エージェントへの委譲も同じ呼び出しインターフェースに統一する
- ミドルウェア層でモデル/ツール呼び出しをインターセプトし、引用生成・プロンプトキャッシュ・コンテキスト要約（17万トークン超で自動要約）を共通処理として組み込む
- モデルプロバイダを抽象化するモデル抽象化層を設け、顧客が選ぶLLMプロバイダに依存しないアーキテクチャにする

## 使いどころ

- 数千件規模の企業内文書を横断して検索・統合・レポート生成させたいエンタープライズプラットフォーム
- 複数のLLMプロバイダに対応しつつ、エージェント基盤の再構築コストを抑えたいプロダクトチーム
