---
type: announcement
title: CoworkとチャットをClaude一つに統合しタスクに応じてドキュメント/スライドも生成
title_original: Claude Cowork and chat are now one Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- Claude Cowork
- Claude Docs
- Claude Slides
- Claude Design
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/cowork-is-now-claude
published_at: '2026-09-16'
---

## 概要

Anthropicは長時間タスク向けの別ツールだったClaude Coworkと通常のチャットを1つのClaudeに統合し、会話の文脈やコネクタ・スキルを引き継いだままタスクの大小に応じてClaudeが処理を委ねられるようにした。同時にClaude DocsとClaude Slidesを新設し、Claude Designも会話内から直接使えるようにすることで、依頼した文書・スライドが同じ会話から一貫して生成されるようにした。

## 設計のポイント

- Cowork/Chat/Designを分離せず、どこで始めたタスクも同じ会話の文脈・コネクタ・スキルを引き継いで実行できるようにする
- デフォルトでは送信・投稿・支払いなどのアクション前にユーザー承認を挟み、設定でチェックイン頻度を調整できるようにする
- 同一会話から生成したレポートとスライドが自動的に内容の整合を保つようにする
- 生成物をartifactとして1つの共有可能なリンクに集約し、要素単位の編集やコメント指示を可能にする

## 使いどころ

- 締め切りのあるレポート作成をチャットで依頼し外出中でも進捗を確認したい担当者
- 文書とスライドを同じ元データから一貫して作りたいチーム
- 定型業務を毎週決まった時間に自動実行させたい個人利用者
