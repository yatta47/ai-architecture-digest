---
type: case
title: 臨床評価が難しい科学領域で、複数モデルの意見一致度を品質シグナルにするBenchlingのエージェント設計
title_original: How Benchling builds agents when the smartest AI isn't smart enough
company: Benchling
industry: healthcare
cloud: []
patterns:
- multi-agent-orchestration
- multi-model-routing
- eval
components:
- LangSmith
- Claude
- Gemini
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/benchling-max-agency-podcast
published_at: '2026-06-12'
---

## 概要

ライフサイエンス企業向けR&Dデータ基盤Benchlingは、科学者のデータ検索・実験設計・レポート作成を支援するBenchling AIをマルチエージェント構成で構築している。同一モデルを複数回実行するのではなく異なるプロバイダのモデルを並行実行して答えを突き合わせ、モデル間の一致/不一致自体をデータ品質やエラーのシグナルとして活用している。

## 設計のポイント

- 同じモデルを繰り返し実行するのではなく複数プロバイダの異なるモデルに同一タスクを解かせ、意見の一致/不一致を品質指標として使う
- 科学分野ではクリーンな評価用ベンチマークを作りにくいため、週替わりの担当者(fire chief)による本番トレースのレビューとユーザーのthumbs up/downを評価の柱に据える
- 10年以上蓄積してきた構造化データをエージェントに与えることを最大の差別化要因として重視し、モデル性能だけに頼らない
- エージェント自身が自らのスキルを作成・更新できる仕組みを持たせ、メモリを固定プロンプトではなく成長する資産として扱う

## 使いどころ

- 正解が一意に定まらない、あるいはクリーンな評価用データセットを作りにくい専門領域でエージェントを運用したいチーム
- 単一モデルの出力だけでは信頼性を担保しづらい高リスクなタスクで、複数モデルのクロスチェックによる品質担保を検討しているチーム
