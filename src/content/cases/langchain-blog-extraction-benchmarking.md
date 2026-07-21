---
type: case
title: チャットログから構造化情報を抽出するLLM抽出タスクのベンチマーク
title_original: Extraction Benchmarking
company: LangChain
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
- rag
- human-in-the-loop
components:
- LangSmith
- Chat LangChain
- GPT-4
- Claude 2
- Code Llama 2
- Llama 2
- Yi-34B
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/extraction-benchmarking
published_at: '2026-06-30'
---

## 概要

LangChainはRAGアプリ「Chat LangChain」の会話ログから構造化情報を抽出するタスクの新しいベンチマークデータセットを公開した。トピック分類・感情・毒性・フォローアップアクションなどをネストしたPydanticスキーマで抽出させ、GPT-4やClaude-2、Llama系オープンソースモデルなど複数モデルの抽出精度を比較している。抽出した構造化データはダッシュボードでの分析やファインチューニング用データ収集パイプラインに活用できるとしている。

## 設計のポイント

- 本番の会話ログをそのままLLMに要約させるのではなくネストした構造化スキーマで分類・要約・抽出を同時に行わせる
- LangSmithのアノテーションキューを使い人手レビューでラベルの品質と分類taxonomyを継続的に更新する
- LLM-as-judgeではなくスキーマ検証や分類精度、編集距離など専用のカスタム評価指標で構造化出力を評価する
- 初期は合成生成したデータを土台にしつつラベル済みデータをfew-shot例として使い生成品質を高める

## 使いどころ

- 本番のチャットボットの会話ログから利用実態を定量的に把握したいチーム
- 構造化ログを分析ダッシュボードやファインチューニング用データ収集に流用したいプロダクトチーム
- 抽出・分類タスクで複数のLLMの精度を比較検討したい開発者
