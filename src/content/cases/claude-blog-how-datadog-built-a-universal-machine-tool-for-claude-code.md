---
type: case
title: エージェントが仕様を書き、決定論的カーネルがコードを生成・検証する「万能工作機械」Temper
title_original: How Datadog built a “universal machine tool” for Claude Code
company: Datadog
industry: cross-industry
cloud: []
patterns:
- spec-driven-development
- ai-agent
- unified-runtime
- policy-as-code
components:
- Claude Code
- Claude Managed Agents
- FoundationDB
- PostgreSQL
- MongoDB
- Temper
- Courier
- BitsEvolve
- Helix
outcome:
  type: reliability
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code
published_at: '2026-07-21'
---

## 概要

Datadogは社内のエンジニアリング全体でClaude Codeを活用し、長時間稼働するエージェントが独自のツールやグルーコードを乱立させる問題に直面した。Courier、BitsEvolve、Helixという3つのプロジェクトを経て、エージェントにアプリケーションコードではなく「仕様」を書かせ、決定論的なカーネルがその仕様を4層の解析で検証してからシステムをデプロイする基盤Temperを構築した。仕様が検証対象と実行対象を兼ねることで、検証済みの内容と実際に稼働するシステムの間にドリフトが生じない仕組みを実現している。

## 設計のポイント

- エージェントにアプリケーションコードを直接書かせず、意図と問題領域を記述した仕様を生成させる
- 仕様そのものを検証対象かつ実行対象にすることで、検証結果と実運用システムの間にドリフトを生じさせない
- 4層の解析による検証を経てからカーネルがシステムをデプロイする段階的な検証パイプラインを設ける
- Courier→BitsEvolve→Helix→Temperと小さなプロジェクトを積み重ね、各段階で見つかったボトルネックを次の設計に反映させる

## 使いどころ

- 長時間稼働するエージェントセッションが独自ツールやグルーコードを乱立させてしまう開発組織
- ミッションクリティカルなデータベースやインフラの構築・運用をエージェントに任せたいチーム
- エージェントのコード生成速度が人間によるレビュー能力を超え、検証がボトルネックになっている現場
