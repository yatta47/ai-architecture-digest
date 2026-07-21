---
type: guidance
title: トレース分析でAIエージェントに長期記憶を持たせるループ設計
title_original: How To Give Your Agent Memory
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- memory-consolidation
- context-engineering
- llmops
components:
- LangSmith Observability
- LangSmith Engine
- LangSmith Context Hub
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-give-your-agent-memory
published_at: '2026-06-24'
---

## 概要

本記事はエージェントに『記憶』を持たせるための一般的な設計を解説し、記憶を実行中のみ有効な短期記憶と、実行をまたいで保持される長期記憶に分け、長期記憶をさらに意味記憶・エピソード記憶・手続き記憶に分類する枠組みを提示する。実装例として、トレース収集(LangSmith Observability)、トレース分析による改善シグナル抽出(LangSmith Engine)、バージョン管理されたコンテキストストアへの反映(LangSmith Context Hub)という3段階のループでLangSmithを使う方法を紹介している。

## 設計のポイント

- 記憶を『実行中のみ有効な短期(ワーキング)記憶』と『実行をまたいで永続する長期記憶』に分離し、それぞれ異なる仕組みで管理する
- 長期記憶を意味記憶(事実・好み)・エピソード記憶(過去の経験・実行例)・手続き記憶(指示・手順・スキル)の3種に分類し、目立つ挙動改善の多くは手続き記憶の修正に起因すると位置づける
- 記憶ループを『トレース収集→トレース分析→メモリ更新』の3段階に分解し、収集(トレースストア)・分析(バックグラウンドプロセス)・更新(バージョン管理されたコンテキストストア)を別コンポーネントとして疎結合に保つ
- すべてのトレースをメモリ化するのではなく、履歴として残すべきデータと、データセット例・eval・コード修正・永続コンテキストへ昇格すべきシグナルを選別し、更新後は実際にランタイムが読み込むことまで検証する

## 使いどころ

- ユーザーが同じ修正や指示を繰り返し入力しなければならないエージェント製品で、一度の指摘を恒久的な挙動改善につなげたい場合
- フォーマット崩れ・ツール呼び出し順序の誤り・サブエージェントへの誤委譲など、繰り返し発生する手続き的な失敗パターンを自動診断し修正したいチーム
- 手動で全実行ログを目視レビューする代わりに、トレースから改善シグナルを継続的に抽出する仕組みを構築したいLLMOps担当者
- 指示・ツール定義・スキルをアプリケーションコードに埋め込まず、バージョン管理された独立ストアとして運用したいエージェント基盤チーム
