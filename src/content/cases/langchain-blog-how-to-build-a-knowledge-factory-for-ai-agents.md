---
type: opinion
title: 企業固有の知識をエージェント向けに維持する「ナレッジファクトリー」
title_original: How to build a knowledge factory
company: LangChain
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
components:
- LangSmith Engine
- Deep Agents
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/knowledge-factory
published_at: '2026-11-21'
---

## 概要

AIを業務に活かす鍵はモデルでも文脈の量でもなく、社内の暗黙知を集めて整え維持する仕組みだとするLangChainの考察。ソフトウェアファクトリーの発想を一般的な知識労働に広げ、自社のGTMやコンテンツのエージェントで運用している。

## 設計のポイント

- 知識をやり方(スキル)、事業の知識(ドメイン知識)、データの在り処(データアクセス指針)に分けて管理する。
- 文脈と知識を区別し、知識は将来の作業の文脈になるものとして継続的に更新する。
- 頻繁に変わるデータは知識化せず、直接エージェントに渡す。

## 使いどころ

- エージェントが社内の基準や用語を踏まえて動くようにしたいとき。
- 属人的な手順をスキルとして共有可能にしたいとき。
- エージェントごとに知識を維持する運用を設計するとき。
