---
type: guidance
title: Deep Agentsのスキルにツールを紐づけてコンテキストを節約
title_original: Revamping skills in Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Deep Agents
- Agent Skills
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
published_at: '2026-10-07'
---

## 概要

Deep Agentsのスキルにツールを紐づけ、スキルを読むまでツールのスキーマをコンテキストに出さない。実行時のスキル固定や、スレッド途中の再読み込みにも対応する。

## 設計のポイント

- ツールスキーマをスキルとともに遅延ロードしてコンテキストを節約する。
- 対応モデルでは途中追加してもプロンプトキャッシュを保つ。
- 必要なスキルを最初のモデル呼び出し前に固定できる。

## 使いどころ

- ツールが多く、コンテキストを圧迫するエージェントに効く。
- 長時間稼働するエージェントのスキル更新に使える。
