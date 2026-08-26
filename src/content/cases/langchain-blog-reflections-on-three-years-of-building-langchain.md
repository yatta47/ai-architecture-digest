---
type: opinion
title: LangChain創業者が語る、langchainからLangGraph・LangSmithへ至るエージェント基盤3年間の進化
title_original: Reflections on Three Years of Building LangChain
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-runtime
- context-engineering
- llmops
components:
- LangChain
- LangSmith
- LangGraph
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/three-years-langchain
published_at: '2026-08-26'
---

## 概要

LangChain創業者Harrison Chaseが、2022年のOSSパッケージlangchain公開から、観測性・評価基盤LangSmith、制御性と本番ランタイムを備えたLangGraphへと至る3年間の製品進化を振り返る。信頼できるエージェント構築という課題に対し、モデル/フレームワーク非依存の設計思想を貫きながら、直近ではlangchainをツール呼び出しループとミドルウェアを中核に据えた1.0として再設計したことを明かしている。あわせて1.25億ドル規模の資金調達も発表している。

## 設計のポイント

- 観測性・評価ツール(LangSmith)は特定のLLMやフレームワークに依存させず独立したプロダクトとして構築し、エコシステム全体への適用性を確保する
- 高レベルの抽象化(langchain)は立ち上げの速さを、低レベルで明示的な制御(LangGraph)は本番移行時のカスタマイズ性を、それぞれ別レイヤーで担わせる
- 本番ランタイムにはストリーミング・状態管理・human-in-the-loop・耐久実行(durable execution)を第一級機能として組み込む
- エージェントの核となるツール呼び出しループをシンプルに保ちつつ、ミドルウェアという拡張点でコンテキストエンジニアリングの自由度を開発者に与える

## 使いどころ

- プロトタイピングから本番運用へとエージェントを移行させたいチームが、制御性と拡張性を求める場面
- 複数のLLMプロバイダやベクトルDBを併用し、後からモデルを切り替える可能性がある開発者
- エージェントの品質問題(誤ったコンテキストによる誤動作)をデバッグ・改善するための可観測性/評価基盤を必要とするチーム
- フレームワークの学習コストと開発速度のトレードオフを踏まえて、まず素早く始めたいスタートアップやPoC担当者
