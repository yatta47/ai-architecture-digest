---
type: case
title: First OrionがAmazon Nova Actで脆いセレクタベースUIテストをエージェント化
title_original: First Orion accelerates QA automation using Amazon Nova Act
company: First Orion
industry: telecom
cloud:
- aws
patterns:
- ai-agent
- ci-cd
components:
- Amazon Nova Act
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/first-orion-accelerates-qa-automation-using-amazon-nova-act/
published_at: '2026-08-11'
---

## 概要

ブランデッドコール事業のFirst Orionは、モジュール化されたセルベースアーキテクチャへの移行でWebアプリが急増し、SeleniumやPlaywrightによるセレクタベースのUIテストがUI変更のたびに壊れQAのボトルネックとなっていた。Amazon Nova Actを導入し、QAアナリストが自然言語で『ポータルにログインして請求書合計を確認する』のようにテストを記述するだけで、エージェントが画面のラベルやレイアウトを見て多段の操作を自律的に実行するようにした。これによりテストがUI変更に強くなり、自動化エンジニアによるコード変換を待たずにQAアナリストが直接テストを作成できるようになった。

## 設計のポイント

- 固定セレクタに依存せず、画面上のラベル・レイアウト・文脈を見て操作を判断するエージェントに置き換え、UI変更への耐性を高める
- テストを『どう操作するか』のコードではなく『何を検証するか』の自然言語記述として書けるようにし、QAアナリストが直接テストを作成できるようにする
- Pythonコードやアサーション、並列実行とエージェント指示を組み合わせ、既存の開発フローに統合する

## 使いどころ

- 分散型・セルベースアーキテクチャでアプリ数が急増しQAが追いつかない組織
- UIの頻繁な変更でセレクタベースの自動テストが壊れ続けるチーム
- 自動化エンジニアの手を離れてQAアナリストがテストを自走できるようにしたい場合
