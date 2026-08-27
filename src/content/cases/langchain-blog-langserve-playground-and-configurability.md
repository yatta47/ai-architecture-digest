---
type: announcement
title: デプロイ済みチェーンに自動で付与される設定切替可能なPlayground UI
title_original: LangServe Playground and Configurability
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- multi-model-routing
components:
- LangServe
- Tavily
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langserve-playground-and-configurability
published_at: '2026-08-26'
---

## 概要

LangChainはLangServeでデプロイしたチェーン/エージェントに対し、モデルやリトリーバーなどの構成要素をUI上で切り替えられるPlaygroundと、その設定をURLに埋め込んで共有できるConfigurability機能を追加した。エンジニア以外のメンバーもストリーミング応答や中間ステップを見ながら試せるようにし、共通アーキテクチャの実験・共有を容易にした。

## 設計のポイント

- チェーン/エージェントのモデル・プロンプト・リトリーバーなど構成可能な要素をLangChain Expression Languageのconfigurable機能で宣言し、コードを触らずに差し替え可能にした
- 設定内容をURLに埋め込むことで、特定の構成を持つ画面をそのまま共有・比較できるようにした
- デプロイ済みのチェーンに自動でPlayground UIを用意し、非エンジニアもストリーミング応答や中間ステップのログを見ながら試せるようにした

## 使いどころ

- 複数のLLM/リトリーバーを切り替えて比較検証したい開発チーム
- エンジニア以外のメンバーにエージェントの挙動を触ってもらいたい場面
- 本番運用前にパラメータ違いによる出力差を素早く試したい場合
