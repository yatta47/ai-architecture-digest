---
type: guidance
title: Claudeチームが教える2026年版プロンプトエンジニアリング実践術
title_original: Best practices for prompt engineering for 2026
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- context-engineering
- ai-agent
components:
- Claude
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/best-practices-for-prompt-engineering
published_at: '2025-11-10'
---

## 概要

Claudeチームが、AIモデルからより良い出力を引き出すためのプロンプトエンジニアリングの基本原則と応用テクニックを解説する記事。明確な指示・目的や文脈の提示・具体性・少数事例の活用・不確実性の表明許可といった基礎に加え、エージェント的タスクや複雑な出力形式に対応するための応用手法としてレスポンスのプリフィルなどを紹介している。

## 設計のポイント

- 曖昧な依頼文ではなく、行動動詞で始まる明確で具体的な指示を与え、欲しい出力内容そのものを明記する。
- 制約やルールの背景・目的をあわせて伝えることで、モデルが関連する判断を状況に応じて適切に行えるようにする。
- 望む出力形式や語調を示したい場合はまず1例（one-shot）を与え、精度が不十分な場合のみ例を追加する（few-shot）。
- 不確実な場合は推測せず『わからない』と表明してよいと明示的に許可し、ハルシネーションのリスクを下げる。

## 使いどころ

- 曖昧な指示のせいで何度もやり取りが発生し、意図通りの出力が得られず手戻りが多いチーム。
- エージェント型のワークフローや複雑なデータ構造を扱う高度なプロンプト設計を最適化したい開発者。
- 金融データ分析など、誤った断定より不確実性の正直な表明が求められる高信頼業務。
- JSON/XML等、後段の自動処理のために出力フォーマットを厳密に固定したいAPI連携パイプライン。
