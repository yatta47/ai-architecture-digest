---
type: guidance
title: 信頼できるAIエージェント評価(eval)の設計指針
title_original: 'AI agent evaluation: Tips from Anthropic on building evals you can trust'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
- llmops
components: []
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/ai-agent-evaluation-how-to-build-evals-you-can-trust/
published_at: '2026-07-28'
---

## 概要

Anthropic Applied AIチームのMarius Buleandra氏は、新モデルがSQLエージェント評価で9ポイント上回ったように見えたが、実際はハーネスの欠陥をLIMIT句で回避していただけだったという事例を通じ、エージェント評価がスコアだけでは因果関係を見誤ることを指摘する。エージェントは軌跡全体で誤りが伝播し、タスクが曖昧で、環境も変化し続けるため、最終結果だけでなく意思決定の系列・モデル/指示・ハーネス・外部ツール状態・採点器まで含めて評価する必要がある。

## 設計のポイント

- 回帰評価(regression evals)と能力評価(capability evals)を明確に区別し、前者は既存機能の非破壊、後者はフロンティア能力の拡大を測る目的で使い分ける。
- スコアの改善が本物の能力向上か、ハーネスの欠陥やグレーダーの抜け穴によるものかを、トランスクリプトを開いて確認する。
- エージェント評価では最終出力だけでなく、ツール呼び出しの系列・システム指示・ハーネス・外部システムの状態・採点器の6層を検証対象にする。
- 顧客インシデントや修正済みバグを回帰評価の材料にし、フロンティア寄りのタスクは能力評価としてhill climbingのように継続的に更新する。

## 使いどころ

- モデルやプロンプト、ツール、ハーネスを変更するたびにリリースの安全性を判断したいエージェント開発チーム。
- エージェントの新しい能力がどこまで拡張したかを可視化し、プロダクト戦略に反映したいチーム。
- 評価スコアの改善が本物かどうかをトランスクリプト分析で検証したいML/エージェント評価担当者。
