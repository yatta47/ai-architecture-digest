---
type: case
title: CognitionがDevinで一晩任せられると信頼したClaude Fable 5
title_original: 'Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night'
company: Cognition
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- root-cause-analysis
- llmops
components:
- Devin
- Claude Fable 5
- Frontier Code
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night
published_at: '2026-07-10'
---

## 概要

AIコーディングエージェントDevinを開発するCognitionは、これまで信頼できなかった長時間の自律実行をClaude Fable 5で初めて任せられるようになったと報告する。同社独自の「アンチスロップ」ベンチマークFrontier Codeでのスコアが約10%から30%に跳ね上がり、実際のドッグフーディングでも8時間の自律作業で実質的な進捗を確認できたという。

## 設計のポイント

- テスト合格だけでなく実コードベースで生き残るかを測る独自ベンチマーク(Frontier Code)でモデルを評価する
- ベンチマークスコアを鵜呑みにせず、ハイタッチな開発者が1日実際に使って採用するかどうかで最終判断する(evalを信用しない)
- モデルに実行前の前提(invariants)を明示させ、不明点は『わからない』と言わせることで長時間自律実行の信頼を積み上げる

## 使いどころ

- コーディングエージェントを数時間〜一晩の長時間自律実行に任せられるか見極めたい開発者ツールチーム
- 新モデル導入時にベンチマークだけでなく実運用ワークフローで品質検証したいプロダクトチーム
- 本番ログのインシデントトリアージを自動化したいSRE/運用チーム
