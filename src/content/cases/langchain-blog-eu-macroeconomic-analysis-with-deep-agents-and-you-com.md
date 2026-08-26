---
type: case
title: Deep AgentsとLangSmithで作るEU27カ国マクロ経済異常検知エージェント
title_original: EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API
company: LangChain
industry: financial-services
cloud: []
patterns:
- multi-agent-orchestration
- context-engineering
- llmops
- ai-agent
components:
- Deep Agents
- LangSmith
- You.com Finance Research API
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/financial-ai-that-investigates-macro-trends-eu-economic-analysis-with-you-com-and-langchain
published_at: '2026-08-26'
---

## 概要

LangChainはDeep AgentsとLangSmith、You.comのFinance Research APIを組み合わせ、EU加盟27カ国のGDPデータを分析して成長・縮小の異常国を検出し、産業別・構造的/循環的要因まで掘り下げた13セクションの引用付きブリーフィングを約45分・API費用約2.20ドルで生成するリサーチエージェントを構築した。異常が検出された国ごとにcountry-investigatorサブエージェントを動的に起動し、アイルランドの製薬輸出主導の成長やドイツの構造的縮小など、根拠を一次ソースまで遡れる形で報告する。

## 設計のポイント

- Deep Agentsのオーケストレーションで異常検知された国ごとにcountry-investigatorサブエージェントを1インスタンスずつファンアウトさせ、委任・並行実行・障害分離・結果集約を任せる設計。
- LangSmithで全ステップ（発行クエリ、レスポンス、中間結果、オーケストレーターの判断）をトレースし、最終レポートの各数値を一次ソースまで遡れる監査証跡を確保する。
- システムプロンプト・Skills・ファイルシステム（Backends）を通じてサブエージェントごとに必要最小限のコンテキストのみを与えるコンテキストエンジニアリングにより、再現性の高い挙動を実現する。
- Finance Research API自体を単一ツール呼び出しとして扱い、公開データと契約データを横断して引用付き回答を返すエージェントをサブエージェントに組み込む設計。

## 使いどころ

- 多数の国・企業のマクロ指標を定期的に比較し、異常値とその発生要因を人手をかけずに調査したいマクロリサーチデスク。
- 意思決定の根拠説明や監査証跡の提示が求められる金融サービス領域で、AIエージェントの各判断ステップを追跡可能にしたい場合。
- 同一のエージェント定義をローカル開発から本番デプロイまで変更なく運用し、スケーリングや永続ストレージ管理を任せたいチーム。
