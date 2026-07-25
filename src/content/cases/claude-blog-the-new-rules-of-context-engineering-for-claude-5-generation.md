---
type: guidance
title: Claude 5世代モデル向けにsystem promptを80%削減した新しいコンテキストエンジニアリング
title_original: The new rules of context engineering for Claude 5 generation models
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- context-engineering
- prompt-optimization
- ai-agent
components:
- Claude Code
- Claude Opus 5
- Claude Fable 5
- CLAUDE.md
- Skills
- ToolSearch
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
published_at: '2026-07-24'
---

## 概要

AnthropicはClaude Code向けsystem promptの80%以上を新世代モデル向けに削減したが、コーディング評価上の性能劣化は測定されなかったと報告する。細かいルールの列挙やツール利用例の反復といった旧来の慣行を見直し、モデルの判断力とprogressive disclosure、自動メモリに置き換えた学びを共有する。

## 設計のポイント

- 厳格なルールを羅列するのではなく新世代モデルの判断力を信頼し、状況依存で誤りうる指示は削除して周辺コンテキストからの推論に任せる
- ツール利用例を大量に与えるのではなく、ツール自体のパラメータ設計を工夫して表現力を高め、モデルの探索空間を狭めないようにする
- 全情報を事前に詰め込むのではなく、SkillsやToolSearchによるprogressive disclosureで必要な時だけコンテキストを読み込む
- CLAUDE.mdへの重複した記憶の書き込みをやめ、自動メモリ機構に一本化してcontext rotを防ぐ

## 使いどころ

- エージェント向けsystem promptが肥大化し矛盾する指示だらけになっているチーム
- 多数のツール定義やドキュメントを常時コンテキストにロードしてトークンを浪費している開発者
- 自前のAIエージェントのコンテキスト設計を新世代モデルの能力に合わせて見直したい場合
