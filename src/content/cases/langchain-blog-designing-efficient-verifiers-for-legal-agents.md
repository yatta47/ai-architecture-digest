---
type: case
title: 法務エージェント検証をバッチ化と安価モデルでコスト1桁〜3桁削減
title_original: Designing Efficient Verifiers for Legal Agents
company: Harvey
industry: legal
cloud: []
patterns:
- eval
- cost-optimization
- reinforcement-learning
components:
- Opus 4.7
- GPT-5.5
- Sonnet 4.6
- DeepSeek v4 Flash
- Claude Haiku 4.5
- Kimi K2.6
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/designing-efficient-verifiers-for-legal-agents
published_at: '2026-06-16'
---

## 概要

LangChainとHarveyが、法務エージェントの出力をルーブリック基準で検証するverifierのコスト効率化を検証。1基準ずつ呼ぶper-criterion方式からルーブリック全体を1回で判定するbatch方式へ、さらに安価なオープンモデル(DeepSeek)へ切り替えることで、frontierモデル同等の精度をコスト1桁〜3桁削減で達成した。

## 設計のポイント

- 採点基準ごとに個別LLM呼び出しをするper-criterion方式ではなく、ルーブリック全体を1回のバッチ呼び出しで判定させてトークンコストを削減する
- 検証には安価なオープンモデル(DeepSeek)を使い、frontierモデルとの一致率で許容水準を確認してから採用する
- false pass(本来failすべき基準を誤ってpassさせる)率を最重要指標として監視し、Haikuのように安いが緩すぎるモデルは避ける

## 使いどころ

- エージェント評価やRLポストトレーニングで大量の採点コールが発生し、検証コストがボトルネックになっている場合
- 専門ドメイン(法務など)で高精度な採点基準を保ちながら検証コストを1桁〜3桁下げたい場合
