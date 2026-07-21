---
type: opinion
title: 非決定的なLLMエージェントを本番品質に鍛える新分野『エージェントエンジニアリング』
title_original: 'Agent Engineering: A New Discipline'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
components: []
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agent-engineering-a-new-discipline
published_at: '2026-06-16'
---

## 概要

LangChainが、非決定的なLLMエージェントを本番品質に磨き上げる新しい実践領域として『エージェントエンジニアリング』を提唱。プロダクト思考・エンジニアリング・データサイエンスの3スキルを組み合わせ、ビルド・テスト・出荷・観測・改善のサイクルを高速に回すことが鍵だとする。

## 設計のポイント

- プロダクト思考・エンジニアリング・データサイエンスの3スキルセットを組み合わせてエージェントを継続改善する
- 動くかどうかではなく本番トレースを観測し改善点を見つける build-test-ship-observe-refine のサイクルを回す
- 全ての入力をエッジケースとして扱い、evalとA/Bテストで継続的に性能を測定する

## 使いどころ

- 非決定的なLLMエージェントを本番品質まで引き上げたいプロダクト/エンジニアリング/データチーム
- エージェント運用の役割分担や評価体制を設計したい組織
