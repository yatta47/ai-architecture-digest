---
type: announcement
title: Skillの品質を継続検証するskill-creatorのevalとベンチマーク機能
title_original: 'Improving skill-creator: Test, measure, and refine Agent Skills'
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components:
- skill-creator
- Claude Code
- Claude.ai
- Cowork
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
published_at: '2026-03-03'
---

## 概要

skill-creatorにeval作成・並列実行・ベンチマークモードを追加し、モデル更新に伴うSkillの品質劣化やトリガー精度の低下を非エンジニアでも検出・改善できるようにした発表。A/B比較用のcomparatorエージェントや、独立コンテキストでの並列eval実行にも対応した。

## 設計のポイント

- capability upliftとencoded preferenceという2種類のSkillを区別し、evalの目的（モデル進化への追随か、業務手順への忠実さか）を分けて考える
- evalは各々を独立したコンテキストを持つサブエージェントで並列実行し、コンテキストの汚染を避けて実行時間を短縮する
- Skillのdescription文をサンプルプロンプトと突き合わせて分析し、トリガーの過検知・見逃しを機械的に削減する

## 使いどころ

- 多数のSkillを運用しており、モデル更新のたびに品質劣化がないか手動確認するコストを下げたいチーム
- Skillのトリガー精度が低く、意図しない場面で発火したり必要な場面で発火しなかったりする課題を抱える運用者
