---
type: announcement
title: LangSmithによるDeep Agentのトレース・デバッグ基盤
title_original: Debugging Deep Agents with LangSmith
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- ai-agent
- root-cause-analysis
- context-engineering
components:
- LangSmith
- Polly
- langsmith-fetch
- Claude Code
- DeepAgents CLI
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/debugging-deep-agents-with-langsmith
published_at: '2026-08-25'
---

## 概要

LangChainは、数十〜数百ステップ・複数ターンにわたって実行される「Deep Agent」のデバッグを支援するため、LangSmithにAIアシスタント「Polly」と、トレース/スレッドを取得するCLI「langsmith-fetch」を追加した。エージェント実行をRuns/Traces/Threadsの階層でトレースし、AIによる分析とプロンプト改善提案を組み合わせることで、人手では追いきれない長大なトレースの原因調査を効率化する。

## 設計のポイント

- エージェント実行をRuns（1ステップ）→Traces（1回の実行）→Threads（複数ターンの会話）の3階層で構造化してトレースする
- トレース/スレッド/プロンプトプレイグラウンドの各画面でチャット型AIアシスタント（Polly）に自然言語で非効率やミスを問い合わせられるようにする
- IDEやコーディングエージェント（Claude Code等）からCLI経由でトレース/スレッドを直接取得できるようにし、UIとローカル開発のギャップを埋める
- 用途に応じてpretty/json/rawの複数出力フォーマットを切り替えられるようにし、ターミナル閲覧・jq連携・LLMへの再投入のいずれにも対応する

## 使いどころ

- 数十〜数百ステップに渡るDeep Agentの実行で、どの判断・プロンプト指示・ツール呼び出しが問題を引き起こしたか特定したいとき
- human-in-the-loopで複数ターンにまたがる会話スレッド全体の挙動を、時間をまたいで把握したいとき
- Claude CodeなどのコーディングエージェントからLangSmithのトレースを直接参照し、デバッグやデータセット構築を効率化したいとき
