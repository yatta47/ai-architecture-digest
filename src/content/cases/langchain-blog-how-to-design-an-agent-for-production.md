---
type: case
title: メールだけで予定調整が完結するCal.aiのOpenAI Functionsエージェント設計
title_original: How to design an Agent for Production
company: Rubric Labs
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- OpenAI Functions
- GPT-4
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-design-an-agent-for-production
published_at: '2026-08-26'
---

## 概要

Rubric LabsはCal.com向けのメールベースAIスケジューリングアシスタント「Cal.ai」を、LangChainのOpenAI Functionsエージェントを使って本番実装した。受信メールをDKIM検証・パース後にエージェントループへ渡し、予定のCRUD操作に対応するツール群とユーザー固有情報（タイムゾーン等）を注入したプロンプトを組み合わせて、自然文の依頼を構造化された予定操作に変換している。

## 設計のポイント

- Cal.comのAPIが公開する明確な入出力を持つ予約操作をそのままツールとして定義し、構造化データの扱いに強いOpenAI Functionsエージェントを採用した
- メール受信時にDKIM検証となりすまし防止チェックを行い、エージェントに渡す前に入力の信頼性を担保した
- ユーザーID・タイムゾーン・稼働時間などの個人情報をプレフィックスプロンプトに埋め込み、汎用エージェントを個々のユーザー向けに文脈化した
- レスポンス速度を優先してgpt-3.5-turboも検討したが、最終的な精度要件からGPT-4を採用するというトレードオフ判断を行った

## 使いどころ

- 自然言語メールから構造化されたシステム操作（予約・CRUD）を実行するAIアシスタントを作りたいチーム
- 外部APIが明確な入出力スキーマを持つ業務でOpenAI Functionsエージェントを採用する設計の参考
