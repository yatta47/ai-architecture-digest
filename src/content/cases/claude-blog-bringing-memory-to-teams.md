---
type: announcement
title: Claudeアプリにチーム向けプロジェクト単位メモリ機能を導入
title_original: Bringing memory to Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- memory-consolidation
- context-engineering
components:
- Claude Enterprise
- Claude Team
- Claude Pro
- Claude Max
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/memory
published_at: '2025-09-11'
---

## 概要

Anthropicは、チームの作業文脈や好みを記憶しコンテキストの再説明を不要にする「メモリ」機能をClaudeアプリに導入した。プロジェクトごとに独立したメモリを持たせることで機密情報や無関係な案件の混在を防ぎ、記憶内容を閲覧・編集できるサマリーや、記憶に残さないIncognitoチャットも提供する。安全性検証を経てTeam/Enterprise向けに先行提供し、その後Pro/Maxプランへ段階的に拡大した。

## 設計のポイント

- プロジェクトごとに独立したメモリを持たせ、案件間の情報混在を防ぐ安全ガードレールとして機能させる
- 記憶内容を1つのサマリーとして可視化し、ユーザーが閲覧・編集・指示更新できるようにする
- メモリに残したくない会話向けにIncognitoチャットを用意し、通常の記憶・履歴と分離する
- リスクの高い機能のため事前に安全性テストを重ね、Team/Enterpriseから段階的にPro/Maxへロールアウトする

## 使いどころ

- 営業チームが商談ごとのクライアント文脈を毎回説明せずに引き継ぐ
- プロダクトチームがスプリントをまたいで仕様や優先事項を保持する
- 経営層が複数の取り組みの状況をコンテキストを再構築せずに追跡する
- 機密性の高い戦略検討や個人的な相談をIncognitoチャットで記憶に残さず行う
