---
type: announcement
title: LLMアプリの評価を標準化するopenevals/agentevalsパッケージ
title_original: Evaluating Large Language Models With OpenEvals
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ai-agent
components:
- openevals
- agentevals
- LangSmith
- LangGraph
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/evaluating-llms-with-openevals
published_at: '2026-06-30'
---

## 概要

LangChainは、LLMアプリケーションやエージェントの評価をゼロから構築する負担を減らすため、汎用の評価器群を提供するopenevalsと、エージェントのツール呼び出し軌跡評価に特化したagentevalsという2つのオープンソースパッケージを公開した。LLM-as-judge評価・構造化データの検証・エージェントのトラジェクトリ評価という3つの代表的な評価パターンをカバーし、LangSmithに結果を記録することで継続的な評価運用を支援する。

## 設計のポイント

- LLM-as-judgeはリファレンス不要（reference-free）で運用できるようにし、根拠となる理由コメントも生成させて透明性を確保する
- 構造化出力の評価は完全一致とLLM-as-judgeを使い分けられるようにする
- エージェント評価はツール呼び出し軌跡（順序込み）とLangGraphのノード遷移軌跡の両方を検証できるようにする
- 評価結果はLangSmithに記録し、時系列でのトラッキングとチーム共有を前提にした運用にする

## 使いどころ

- チャットボットの応答品質やハルシネーションをゼロから評価基盤を作らず検証したいチーム
- PDFや画像からの構造化データ抽出、ツール呼び出しパラメータの妥当性を検証したい場合
- エージェントが正しいツールを正しい順序で呼んでいるかを継続的に監視したいプロダクト
