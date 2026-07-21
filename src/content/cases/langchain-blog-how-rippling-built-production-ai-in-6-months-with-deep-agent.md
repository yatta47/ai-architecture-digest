---
type: case
title: Rippling社の人事・給与プラットフォームにおけるマルチエージェントAIレイヤー
title_original: How Rippling Went AI-Native Across Every Product in 6 Months with Deep Agents and LangSmith
company: Rippling
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- context-engineering
- rag
components:
- Deep Agents
- LangSmith
- LangGraph
- Salesforce
- Carta
- GitHub
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith
published_at: '2026-06-30'
---

## 概要

ワークフォース管理プラットフォームのRipplingは、HR・IT・給与・財務など数千テーブルにまたがる巨大で概念が重複するデータモデルに対して横断的に回答できるAIレイヤー「Rippling AI」を、Deep AgentsとLangSmish上でわずか6か月で構築し数百万ユーザー規模で本番展開した。supervisorエージェントがread/RAG/actionの専門サブエージェントを束ねる多エージェント構成で、コンテキストエンジニアリングと自己修復型の評価ループにより品質を継続的に改善している。

## 設計のポイント

- supervisorエージェントがread/RAG/actionの専門サブエージェントを束ね、ドメイン横断的な問い合わせをどのサブエージェントに振るか判断する多エージェント構成をとる。
- セマンティックレイヤーで関連ドメインを特定してから該当スキルだけを動的に注入し、リランカーで積極的に絞り込むことでコンテキストサイズを100〜500倍削減する。
- 書き込み系のaction agentはLLMに直接データ操作させず、サンドボックス化されたコード実行で入力を正規化し、「何をするか」（LLM推論）と「どう整形するか」（決定的コード）を分離する。
- REPLでランタイム変数ストアをエージェントステップ間に維持し、長い英数字IDを直接受け渡す代わりに変数名で参照させることでハルシネーションを防ぐ。

## 使いどころ

- 数千テーブル・部門横断で概念が重複する巨大なデータモデルを持つ企業が、AI推論レイヤーを1つに統合したい場合。
- チャットや構造化UIを通じて、HR・IT・給与・財務など複数ドメインにまたがる質問に単一の窓口で答えたいプロダクト。
- 本番トレースから回帰を自動検知し、修正案の生成から評価再実行まで半自動化してエンジニアの負担を減らしたい運用チーム。
