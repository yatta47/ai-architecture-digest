---
type: opinion
title: AI評価がうまくいかない本当の原因は評価設計より前のプロダクト設計にある
title_original: Hamel Husain explains why AI evals fail before the evaluation begins
industry: cross-industry
cloud: []
patterns:
- eval
components: []
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/rise-of-the-ai-engineer-why-ai-evals-fail-before-the-evaluation-begins/
published_at: '2026-07-30'
---

## 概要

評価の専門家Hamel Husainは、多くのAI評価が「モデルの問題」として扱っている失敗の多くが実はプロダクト設計の問題だと指摘する。曖昧なユーザー要求への対処、評価基準の版管理、汎用メトリクスの限界、実トレースに基づく誤り分析、ドメインエキスパートの巻き込みなど、評価を機能させるための前提条件を論じている。

## 設計のポイント

- 評価基準を版管理された成果物として扱い、定義・具体例・所有者・変更理由を記録してスコア変動の原因を切り分ける
- 曖昧なユーザー要求を放置せずアプリ側で確認質問や構造化フィールドの要求として設計に組み込む
- 汎用メトリクス（正確性・関連性など）だけでなく実トレースの誤り分析から得た具体的な失敗パターンを評価基準に変換する
- ドメインエキスパートが素早く誤り分析できるレビューインターフェースを用意し開発者だけに閉じさせない

## 使いどころ

- モデルの品質を疑う前にプロダクト設計側の欠陥を切り分けたいAIプロダクトチーム
- 評価基準がプロダクトの成熟につれて変化していく過程を追跡したいチーム
- セキュリティやコンプライアンスなど専門知識が必要な失敗パターンをドメインエキスパートと共に洗い出したいチーム
