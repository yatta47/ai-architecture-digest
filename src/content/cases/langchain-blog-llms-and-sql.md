---
type: guidance
title: LLMでSQLデータベースを自然言語操作するText-to-SQLの設計パターン
title_original: LLMs and SQL
company: LangChain
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- ai-agent
components:
- LangChain
- SQL Chain
- SQL Agent
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/llms-and-sql
published_at: '2026-08-25'
---

## 概要

LangChainは、LLMがSQLを書く際に陥りがちな幻覚（存在しないテーブル/カラムの捏造）とコンテキストウィンドウ制限という2つの課題を、データアナリストの作業手順を模した設計で解決する方法を解説する。スキーマをCREATE TABLE文＋数行のサンプルデータとしてプロンプトに含め、必要以上のデータは渡さず、実行エラーが出た場合はLLM自身に学習させて再クエリさせるアプローチを提示する。

## 設計のポイント

- スキーマ全体やテーブル内容を丸ごと渡すのではなく、CREATE TABLE定義と少数（研究上最適とされる3行程度）のサンプル行だけを渡し、幻覚とコンテキスト超過の両方を抑える
- データアナリストが事前にサンプルクエリでデータの中身を把握してから本番クエリを書く手順を、LLMのプロンプト設計に写し取る
- SQL実行時にエラーが出た場合は諦めずエラー内容をLLMにフィードバックし、修正クエリを再生成させるループを組み込む

## 使いどころ

- 既存のSQLデータベースに対して自然言語での問い合わせインターフェースを構築したいBI/データ基盤チーム
- 本番スキーマに対するアドホッククエリでLLMの幻覚SQLを減らしたいエンジニアリングチーム
