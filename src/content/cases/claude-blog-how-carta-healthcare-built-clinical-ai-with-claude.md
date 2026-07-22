---
type: case
title: 臨床データ抽出エージェント「Lighthouse」、コンテキストエンジニアリングで99%精度を実現
title_original: How Carta Healthcare gets AI to reason like a clinical abstractor
company: Carta Healthcare
industry: healthcare
cloud:
- aws
patterns:
- context-engineering
- document-processing
- ai-agent
components:
- Amazon Bedrock
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/carta-healthcare-clinical-abstractor
published_at: '2026-04-08'
---

## 概要

Carta Healthcareは、年間2.2万件の手術症例を扱う臨床データ登録業務を自動化するプラットフォーム「Lighthouse」を、Amazon Bedrock上のClaudeを用いて構築した。ルールベースのNLPでは対応しきれない曖昧な臨床記録の解釈を、Claudeによる文脈的推論に置き換えることで99%の精度を達成した。同社はプロンプト設計そのものより、手技開始時刻などの症例固有情報を実行時に正しく組み立てる「コンテキストエンジニアリング」こそが本質的な課題だったと述べている。

## 設計のポイント

- 手技開始時刻など症例固有の時間的基準をランタイムでコンテキストに注入し、時系列上正しい検索範囲（例:術前の値のみ）に限定する
- プロンプトの巧拙よりも、参照すべき文書・時間窓・優先順位を組み立てるコンテキスト構築を設計の中心に据える
- パターンマッチ型NLPではなく、矛盾する記録間の重み付けや曖昧さの解消を要する臨床判断はLLMの推論力に委ねる
- モデル選定時は同種のタスクにおける文脈理解・解釈能力そのものを評価基準にする

## 使いどころ

- 病院の診療記録・画像所見・医師ノートなど複数ソースを横断して登録用データを抽出する場面
- 手技前後で数値の有効期限が変わるなど、時間的制約を伴う判断をスケールさせたい業務
- 熟練の人手作業（アブストラクター等）が持つ暗黙の判断基準をAIに引き継がせたい場合
