---
type: announcement
title: Deep Agentsのハーネスを軽量化しミドルウェアを設定可能にしたv0.7
title_original: Deep Agents v0.7
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- cost-optimization
- eval
components:
- Deep Agents
- LangSmith
- FilesystemMiddleware
- SummarizationMiddleware
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/deep-agents-v0-7
published_at: '2026-07-29'
---

## 概要

LangChainはオープンソースのエージェントフレームワークDeep Agentsのv0.7をリリースし、ベースシステムプロンプトの削除やツール説明の削減、todoミドルウェアのオプト化により基本入力トークンを65%削減した。3種類のベンチマーク(自律・対話・長文コンテキスト)と4モデルでの評価によりパフォーマンスを維持できることを確認し、あわせてミドルウェアの上書きなど設定自由度も高めた。

## 設計のポイント

- ベースシステムプロンプトやツール説明を削減してエージェントの基本入力トークンを削減する
- todoリスト管理ミドルウェアをデフォルトオフにし、長時間タスクや非力なモデルなど必要な場合のみオプトインさせる
- ミドルウェアのnameが一致すれば標準実装を上書きできるようにし、要約の閾値やプロンプトなど個別最適化を可能にする
- ファイルシステム操作(read_file/grep/glob)にページネーションや部分結果返却を導入し大規模リポジトリでも安定動作させる

## 使いどころ

- コーディングやデータ分析などの自律エージェントでトークンコストを削減したいチーム
- 独自のシステムプロンプトやミドルウェア設定をハーネスに持ち込みたい開発者
- 長い複数ステップタスクや非力なモデルでtodoリストによる進行管理が必要な場合
- 会話要約のトリガー閾値やプロンプトをアプリケーションごとに調整したいチーム
