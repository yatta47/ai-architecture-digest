---
type: announcement
title: LangChainがBenchmark主導で1000万ドルのシード資金を調達
title_original: Announcing our $10M seed round led by Benchmark
company: LangChain
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/announcing-our-10m-seed-round-led-by-benchmark
published_at: '2026-08-26'
---

## 概要

LangChainは、LLMアプリケーションを構成可能なコンポーネントで組み立てるオープンソースフレームワークとして急成長し、GitHubスター2万・Discord会員1万・コントリビューター350人超という規模になったことを受け、Benchmark主導で1000万ドルのシード資金を調達したことを発表した。「データを意識する」「エージェント的である」という2つの原則を軸に、モデルプロバイダー・ドキュメントローダー・ベクトルストア・ツールなどのコンポーネント群と、その組み合わせであるチェーン/エージェントを提供する方針を示している。

## 設計のポイント

- LLMアプリを「データを意識する（外部データソースに接続する）」「エージェント的である（環境と相互作用する）」という2つの原則で捉え、フレームワーク全体の設計方針とした
- モデルプロバイダー・ドキュメントローダー・テキスト分割・ベクトルストア・ツールをそれぞれ独立したコンポーネントとして抽象化し、自由に組み合わせられるようにした
- チェーン（決まった手順の組み合わせ）とエージェント（LLMが動的に手順を決める組み合わせ）を明確に区別し、用途に応じて使い分けられるようにした

## 使いどころ

- LLMアプリのアーキテクチャをゼロから設計するのではなく、既存の抽象化された部品を組み合わせて構築したい開発者
