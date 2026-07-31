---
type: announcement
title: LangSmithに組み込まれたランタイムガバナンス層「LLM Gateway」
title_original: 'LangSmith LLM Gateway: runtime governance built into the agent lifecycle'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- guardrails
- llmops
components:
- LangSmith
- LangSmith LLM Gateway
- LangSmith Engine
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-llm-gateway
published_at: '2026-07-31'
---

## 概要

LangChainはエージェントとLLMプロバイダーの間に位置するランタイムガバナンス層「LangSmith LLM Gateway」をプライベートベータ公開。支出上限の強制やPII/機密情報のリクエスト前redaction、ポリシー違反イベントを既存のトレースと同じ画面で確認できる統合を実現する。

## 設計のポイント

- ゲートウェイをオブザーバビリティ基盤(LangSmith)と同一製品内に統合し、ブロックされたリクエストからトレース、修正までを1画面で完結させる
- 組織・ワークスペース・ユーザー・APIキーの各階層で支出上限を設定できるレイヤード制御を提供する
- 導入はbase_urlの変更のみで完結させ、既存コードやエージェント実装への変更を不要にする
- PIIや機密情報をモデルに到達する前、およびトレースに書き込まれる前にリダクトし、下流への伝播を防ぐ

## 使いどころ

- 夜間のリトライループなどで想定外の高額請求が発生するリスクを抑えたいエージェント運用チーム
- 顧客対応エージェントが個人情報を含むデータを扱う際のガバナンス強化
- 既にLangSmithで開発・観測しているチームが別ツールを追加せずガバナンスを導入したい場合
