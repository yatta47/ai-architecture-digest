---
type: announcement
title: LLMエージェントに安全な実行基盤を与えるプラグインインフラ「Connery」
title_original: 'Meet Connery: An Open-Source Plugin Infrastructure for OpenGPTs and LLM apps'
company: Connery
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- Connery
- OpenGPTs
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/meet-connery-an-open-source-plugin-infrastructure-for-opengpts-and-llm-apps
published_at: '2026-08-26'
---

## 概要

ConneryはLLMアプリが外部サービス（Gmail、AWSなど）を安全に操作するためのオープンソースのプラグイン基盤で、接続管理・パーソナライズ・人間による承認（human-in-the-loop）・監査ログといった機能をOpenGPTsなどのLLMアプリに提供する。LLMベースのアプリは自然言語の解釈ミスなど従来のアプリにない不確実性があるため、アクションのメタデータ整備や重要な操作の実行前レビューといった安全対策をインフラ側で標準化することを狙っている。

## 設計のポイント

- ユーザーごとの外部サービス接続（OAuth等）とシークレット管理をアプリ側ではなくプラグイン基盤側に集約し、認証まわりの実装負担を無くした
- 各アクションに説明・入力スキーマ・検証ルールをメタデータとして持たせ、LLMがアクションを誤って選択・実行するリスクを減らした
- メール送信など重要な操作の実行前にユーザーが入力内容を確認・編集できるhuman-in-the-loopの仕組みを組み込んだ
- 監査ログを標準機能として持たせ、LLMエージェントが実行した操作の一貫性・コンプライアンス・透明性を担保した

## 使いどころ

- LLMエージェントに外部サービスへの実操作（メール送信、カレンダー操作等）を任せたいプロダクトチーム
- 個人アシスタント型LLMアプリで安全性・監査要件を満たしたい開発者
