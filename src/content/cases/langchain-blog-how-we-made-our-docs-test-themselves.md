---
type: case
title: ドキュメントのコードサンプルをAgentが自動でテスト化
title_original: How we made our docs test themselves
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- ci-cd
components:
- Deep Agents CLI
- Skills
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/our-docs-test-themselves
published_at: '2026-10-13'
---

## 概要

LangChainはドキュメント内の陳腐化するコードサンプルを、Deep Agents CLIとSkillsに手順を書いて委譲し、独立ファイル化してCIで実行する形へ移行した。

## 設計のポイント

- 移行手順をSkillとして1度書き、エージェントに繰り返し実行させる。
- サンプルをコードとして扱いCIで失敗させて陳腐化を検知する。

## 使いどころ

- SDKやAPIの変更が速いプロダクトのドキュメント保守。
