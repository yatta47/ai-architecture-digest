---
type: opinion
title: エージェント型コーディングを前提にしたエンジニアリング組織の再設計
title_original: Running an AI-native engineering org
company: Anthropic
industry: other
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- Claude Code
- Claude Cowork
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/running-an-ai-native-engineering-org
published_at: '2026-06-03'
---

## 概要

Anthropic Claude Codeチームのエンジニアリング責任者が、エージェント型コーディングが当たり前になったことで従来のプランニングやコードレビューの慣習がどう変わったかを語る。半年先までの詳細なロードマップ策定をやめてJust-in-Timeでプロトタイプとフィードバックを回す方式にし、コードレビューはスタイル・バグ・テスト追加をClaudeに任せ、法務やセキュリティなど人間の専門判断が必要な領域だけ人がレビューする体制に移行した。

## 設計のポイント

- 計画は半年先まで固めず、プロトタイプを社内ユーザーに使わせてフィードバックで軌道修正するJust-in-Time方式に切り替える
- コードの背景を知りたいときはまず書いた本人ではなくAIに聞き、答えられない場合や自動化できる場合を都度判断する
- コードレビューはスタイル・バグ修正・テスト追加をAIに任せ、法務リスクやセキュリティなど人間の専門知識が要る領域だけ人がレビューする
- 陳腐化したプロセスを躊躇なく廃止する原則をチームの必須ルールとして明文化する

## 使いどころ

- エージェント型コーディングの浸透に合わせて計画・レビュー体制を見直したいエンジニアリング組織
- コードレビューの人手不足に悩み、AIと人間の役割分担を再設計したいチーム
- PM・デザイナー・エンジニアの役割が固定化して身動きが取りにくくなっている組織
