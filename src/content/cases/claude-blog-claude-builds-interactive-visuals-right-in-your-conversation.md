---
type: announcement
title: 会話中にインタラクティブな図表を生成するClaudeの新表示機能
title_original: Claude now creates interactive charts, diagrams and visualizations
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Claude
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-builds-visuals
published_at: '2026-03-12'
---

## 概要

Claudeが会話の流れの中でインタラクティブなグラフ・図表・可視化をインラインに生成できるようになった。保存用のartifactsとは異なり、会話の理解を助ける一時的な補助表示として動的に変化・消滅する。

## 設計のポイント

- 永続的な成果物であるartifactsと、説明補助のための一時的インライン可視化を明確に役割分離する
- ユーザーが明示指示しなくても、Claudeがトピックに応じて可視化すべきかを自律判断してデフォルトで生成する

## 使いどころ

- 複利計算や周期表など、数式やデータ構造を対話しながら直感的に理解したい学習・説明シーン
- 会話の中でその場限りの図解が欲しいが、成果物として保存するほどではない場面
