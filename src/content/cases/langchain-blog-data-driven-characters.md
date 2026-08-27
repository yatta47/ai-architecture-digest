---
type: case
title: 任意のコーパスから会話可能なキャラクターチャットボットを生成する仕組み
title_original: Data-Driven Characters
industry: media
cloud: []
patterns:
- rag
- memory-consolidation
components: []
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/data-driven-characters
published_at: '2026-08-26'
---

## 概要

LangChainに参加したエンジニアが、任意のテキストコーパス（映画の脚本やエッセイ集など）からキャラクターチャットボットを自動生成する「data-driven-characters」を開発した。character.aiのように手作業でキャラクター設定を書く代わりに、要約や検索ベースの複数のメモリ管理方式でキャラクターの背景を根拠付け、character.aiへのエクスポートやStreamlitでの自前ホスティングにも対応させた。

## 設計のポイント

- キャラクター設定を手作業で書く代わりに、原作コーパス（脚本・エッセイ等）から要約・検索ベースのメモリを構築してキャラクターを根拠付ける設計にした
- メモリ管理方式（要約か検索か）をユーザーが選べるようにし、既存サービスにはない「メモリの中身をコントロールできる」体験を提供した
- character.aiへのエクスポート、ローカルCLI、自己完結型Streamlitアプリという3つの利用形態を用意し、用途に応じて選べるようにした

## 使いどころ

- 実在の人物や架空のキャラクターと対話できる体験を自社コンテンツから作りたいメディア/エンタメ企業
- 訓練データに含まれない新しいキャラクター（最近の映画・独自コンテンツ）を会話可能にしたい開発者
