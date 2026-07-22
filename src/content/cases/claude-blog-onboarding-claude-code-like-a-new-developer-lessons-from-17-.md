---
type: case
title: 700,000行超のSkylineコードベースに『新人研修』の手法でClaude Codeをオンボーディングする
title_original: 'Onboarding Claude Code like a new developer: Lessons from 17 years of development'
company: MacCoss Lab (University of Washington)
industry: healthcare
cloud: []
patterns:
- context-engineering
- root-cause-analysis
- ai-agent
components:
- Claude Code
- MCP
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development
published_at: '2026-04-28'
---

## 概要

2008年から700,000行超のC#コードベースを17年間保守してきたプロテイン解析ソフトSkylineの主任開発者が、新人研究者をオンボーディングしてきた手法(段階的にプロジェクトを説明しコンテキストを育てる)をClaude Codeにもそのまま適用した。コードとは別リポジトリにCLAUDE.mdとskillsとしてプロジェクトの知識・デバッグ手順を蓄積し、1年間放置されていた機能を2週間で完成させたほか、開発者不在で塩漬けだったモジュールも短時間で再拡張し、Claudeが自作したMCPサーバーで日次のテスト失敗サマリーを自動生成する体制を構築した。

## 設計のポイント

- AIへのコンテキストをコードベースとは別リポジトリで管理し、ブランチや時期を横断して再利用できるようにする
- CLAUDE.mdには『土地勘』程度の環境情報だけを置き、専門知識はskillsとして切り出して必要な場面で読み込ませる
- デバッグのように特定の振る舞いが必要な場面には『常にこのskillを読み込む』という明示的なトリガー条件を設定し、当て推量での修正を防ぐ
- 担当者の離脱で塩漬けになっていた機能や旧言語のモジュールを、Claude Codeで短期間に再着手・完成させる

## 使いどころ

- 長期間・大規模なコードベースを少人数で保守しているチームが新規貢献者(人・AI問わず)のオンボーディングコストを下げたい場合
- 開発者の離脱によって塩漬けになった未完成の機能やレガシーモジュールを再稼働させたい場合
