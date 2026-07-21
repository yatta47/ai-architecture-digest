---
type: guidance
title: トレーダー向けSQLコパイロットに学ぶ、エージェント改善ループへの人間の判断の組み込み方
title_original: Human judgment in the agent improvement loop
industry: financial-services
cloud: []
patterns:
- human-in-the-loop
- context-engineering
components: []
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/human-judgment-in-the-agent-improvement-loop
published_at: '2026-06-16'
---

## 概要

AIエージェントに組織の暗黙知を反映させるための「改善ループ」の設計ガイド。金融機関のトレーダー向けSQLコパイロットを例に、ワークフロー設計・ツール設計・エージェントへの文脈提供という各要素にリスク/コンプライアンス担当者などのドメイン専門家の判断をどう組み込むかを解説する。

## 設計のポイント

- ワークフローの一部を決定的コードで固定し、規制やリスクの高いステップはLLMの自由裁量に任せない
- ツールセットをワークフロー段階ごとに絞り込み、モデルが不要な選択肢を選ばないようにする
- エージェント起動時に読み込む文脈をSkills等で構造化し、システムプロンプトを肥大化させずに必要な知識だけ取得させる

## 使いどころ

- 専門知識やドメイン内の暗黙知をエージェントに反映させたい組織
- 規制の強い業務(金融・法務等)でLLM生成結果に自動チェックを組み込みたい場合
