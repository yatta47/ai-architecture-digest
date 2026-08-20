---
type: case
title: Slackが実践する『会話を知識に変える』人間・エージェント協働チームの作り方
title_original: 'Turning conversation into knowledge: how Slack builds human-agent teams'
company: Slack
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- context-engineering
components:
- Claude
- Slack
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams
published_at: '2026-08-19'
---

## 概要

Slack CPOのJaime DeLanghe氏へのインタビューをもとに、会話の履歴をナレッジベースとして扱い、SlackとClaudeを組み合わせて人間とエージェントが役割分担するチームの実践を紹介する。公開チャンネルをデフォルトにしてエージェントが参照できる文脈を広げる、朝のブリーフィングなど定型作業をエージェントに任せて人間はレビュー・意思決定に集中する、エージェントにも人間の同僚のような明確な役割を持たせるといった具体的な運用ノウハウをまとめている。

## 設計のポイント

- 公開チャンネルをデフォルトにし、意思決定や作業中の会話をエージェントが読める場所に残すことで、エージェントが参照できる文脈そのものを広げる
- 『何が決まったか』ではなく『なぜそう決まったか、状況がどう変わったか』をエージェントに再構成させることで、記録の検索よりも深い文脈理解を引き出す
- 朝のブリーフィングやレポート作成などプロダクション作業をエージェントに任せ、人間はレビューと意思決定、次の作業指示に専念するという定常的なハンドオフのリズムを作る
- エージェントにも人間の同僚のように明確な役割と担当領域を持たせ、価値が『感じられる』ものでなければ役割を見直す運用にする

## 使いどころ

- 社内の会話やドキュメントが分散していて、同じ質問や調査を何度も繰り返している組織
- エージェントに定型的な要約・レポート・エスカレーション検知を任せ、人間はレビューと意思決定に集中したいチーム
- 複数の専門エージェントを社内に導入する際、役割と責任範囲をどう設計すればよいか悩んでいる組織
