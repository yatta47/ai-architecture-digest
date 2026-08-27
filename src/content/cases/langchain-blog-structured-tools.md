---
type: announcement
title: LangChainの構造化ツール（Structured Tools）で複数引数・型付きスキーマのツール呼び出しに対応
title_original: Structured Tools
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- LangChain
- StructuredTool
- PlayWright Browser toolkit
- File management toolkit
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/structured-tools
published_at: '2026-08-25'
---

## 概要

LangChainは、従来1つの文字列入力しか受け付けなかったツールを、Pydanticベースの型付きスキーマで任意個数・任意型の引数を受け取れるStructuredToolへ拡張し、これに対応する新しいエージェントクラスを公開した。あわせてファイル操作ツールキットとステートフルなWebブラウザ操作ツールキットを、この新しい基底クラス上で正式リリースした。

## 設計のポイント

- ツールの識別・選択に使うname/description、入力を検証するargs_schema（Pydantic）、実処理を行う_run/_arunを明確に分離した設計にする
- モデル性能の向上に合わせて『単一文字列入力』という制約を外し、複数の型付き引数を受け取れるツールへ段階的に移行する
- ファイル操作・ブラウザ操作のような複雑な公式ツールキットも同じStructuredTool基底クラス上に統一し、拡張性を確保する

## 使いどころ

- 単一の文字列クエリでは表現できない、複数パラメータを要するAPI呼び出しをエージェントに行わせたい開発者
- エージェントにファイルシステム操作やWebブラウジングなど複数ステップの具体的操作を任せたいチーム
