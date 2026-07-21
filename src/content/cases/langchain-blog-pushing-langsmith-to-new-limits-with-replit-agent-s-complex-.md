---
type: case
title: Replit Agentの大規模トレースをLangSmithで観測・デバッグする
title_original: Pushing LangSmith to new limits with Replit Agent's complex workflows
company: Replit
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- human-in-the-loop
- llmops
components:
- LangSmith
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/customers-replit
published_at: '2026-06-15'
---

## 概要

コード生成・環境構築・デプロイまで担うReplit Agentは数百ステップに及ぶ巨大なトレースを生成するため、LangChainと共同でLangSmithの大規模トレース処理性能を強化した。トレース内検索やマルチターン会話をまとめるThread Viewを新たに実装し、複数エージェントが人間と協調するワークフローのボトルネックとエラーを素早く特定できるようにした。

## 設計のポイント

- 数百ステップに及ぶ巨大なトレースを効率的に取り込み・表示できるようインジェストとレンダリングを最適化する
- トレース間検索だけでなく、1本の巨大なトレース内でもキーワード検索・フィルタできるようにする
- 計画・編集・検証など役割の異なる複数エージェントのやり取りを、関連する複数スレッドとして束ねて可視化する
- 人間がエージェントの軌道を随時修正できるよう、会話全体を俯瞰できるThread Viewを用意する

## 使いどころ

- 多数のツール呼び出しやサブエージェントを含む長時間稼働のエージェントを開発するチーム
- 人間とエージェントが交互に介入するhuman-in-the-loopなワークフローを運用するプロダクト
