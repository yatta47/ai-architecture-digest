---
type: case
title: セマンティックレイヤーをベクトル検索と組み合わせた自然言語→SQL変換
title_original: 'Cube x LangChain: Building AI experiences with LLMs and the semantic layer'
company: Cube
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- rag
components:
- Cube
- OpenAI
- Streamlit
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/cube-x-langchain-building-ai-experiences-with-llms-and-the-semantic-layer
published_at: '2026-08-26'
---

## 概要

CubeとLangChainは、Cubeのセマンティックレイヤー（ビューやメンバー定義）をドキュメント化してベクトルストアに格納し、自然言語の質問と意味的にマッチさせてからSQLを生成するチャット型インターフェースを構築した。テーブル定義を丸ごとLLMに渡すのではなく、段階的に候補を絞り込むことでLLMの幻覚を抑え、正確なSQL生成につなげている。

## 設計のポイント

- テーブル定義を直接LLMに渡す代わりに、セマンティックレイヤーのビュー・メンバー定義をベクトルストアに格納し、質問文と意味的にマッチする定義だけを検索して使う設計にした
- まず最も近いテーブル（ビュー）を検索し、続けてそのテーブルのカラム候補を絞り込むという段階的な絞り込みでプロンプトに詰め込む情報量を抑えた
- SQL生成の正しさをセマンティックレイヤー側の制約に委ねることで、LLMのスキーマ誤認識（幻覚）による誤ったクエリ生成を抑えた

## 使いどころ

- 自然言語からSQLを生成するインターフェースを構築したいアナリティクス基盤チーム
- 多数のテーブル・指標を持つデータウェアハウスでスキーマ全体をLLMに渡せない場合の設計例
- ノーコードで社内データに質問できるチャットBIを検討しているプロダクトチーム
