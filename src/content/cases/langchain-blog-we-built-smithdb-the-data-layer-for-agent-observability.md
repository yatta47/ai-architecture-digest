---
type: case
title: エージェント観測基盤を支える自社製データベースSmithDBのアーキテクチャ
title_original: We built SmithDB, the data layer for agent observability
company: LangChain
industry: cross-industry
cloud:
- multi-cloud
- on-prem
patterns:
- ai-agent
- llmops
- full-text-search
components:
- SmithDB
- LangSmith
- Apache DataFusion
- Vortex
- PostgreSQL
- Rust
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-smithdb
published_at: '2026-06-25'
---

## 概要

LangChainは、巨大化・多段ネスト化したAIエージェントのトレースデータを扱うために、専用データベースSmithDBを開発しLangSmithの中核基盤として本番投入した。RustとApache DataFusion、Vortexを用いたオブジェクトストレージ主体のLSM型アーキテクチャにより、トレースツリー読み込みや全文検索などの主要ワークロードで従来比最大15倍の高速化を実現した。ステートレスなインジェスト・クエリ・コンパクションサービス構成により、セルフホストやマルチクラウド環境への展開も容易にしている。

## 設計のポイント

- 永続データはオブジェクトストレージに置き、インジェスト・クエリ・コンパクションをすべてステートレスサービスにすることでローカルディスク管理を排除し、コンピュートの追加だけで水平スケールできるようにする。
- セグメントメタデータのみを軽量なPostgresメタストアで管理し、実データ本体は列指向フォーマットでオブジェクトストレージに保存するハイブリッド構成を採る。
- LSM(ログ構造化マージ)ツリー方式を採用し、書き込みをメモリにバッファしてから不変のソート済みセグメントとしてフラッシュ、定期コンパクションすることで書き込みと読み取り双方の性能を両立する。
- Apache DataFusionをクエリエンジンに採用し、ランダムアクセス・ツリー階層フィルタ・全文検索・JSONフィルタ・スレッド再構成など、エージェント特有の多様なクエリパターンを単一エンジンでカバーする。

## 使いどころ

- 数百のネストしたスパンを持つ長時間実行エージェントのトレースを高速に読み込み、デバッグしたいチーム。
- 大量のエージェント実行ログからフルテキスト検索やメタデータフィルタでエッジケースを見つけ、評価データセットを構築したいプロダクトチーム。
- セルフホストやマルチクラウド環境でAIエージェントの観測基盤を自前運用する必要があるエンタープライズ企業。
- コストやレイテンシがボトルネックになっている既存の汎用オブザーバビリティストアを、エージェント特化型の基盤に置き換えたい組織。
