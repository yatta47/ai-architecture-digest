---
type: announcement
title: ブラウザ操作AIエージェント「Claude in Chrome」の安全なパイロット提供
title_original: Piloting Claude in Chrome
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- defense-in-depth
- human-in-the-loop
components:
- Claude in Chrome
- Claude Code
- Computer Use
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-for-chrome
published_at: '2025-08-25'
---

## 概要

Anthropicは、ユーザーに代わりブラウザ内で操作を行うエージェント「Claude in Chrome」を、Maxプラン利用者1,000人限定の招待制でパイロット提供した。レッドチーム評価では対策なしの状態でプロンプトインジェクション攻撃成功率が23.6%だったが、権限管理・アクション確認・システムプロンプト改善・高リスクサイトのブロック・不審な指示検知の分類器導入により11.2%まで低減し、既存のComputer Use機能より安全性を高めた。その後Max全体、続いてPro/Team/Enterpriseへと段階的に提供範囲を拡大し、Claude Codeとの連携も追加された。

## 設計のポイント

- サイト単位の権限管理と高リスク操作時のアクション確認を第一の防御線として組み込む
- システムプロンプトを改善し、機密データの扱いや疑わしい指示への対応方針をエージェントに明示する
- 金融・アダルト・海賊版コンテンツなど高リスクカテゴリのサイトをあらかじめブロックリストで遮断する
- 不審な指示パターンやデータアクセス要求を検知する専用の分類器を追加し、多層防御を実現する

## 使いどころ

- カレンダー管理・メール下書き・経費精算などブラウザ上の定型業務を自動化したい個人ユーザー
- 自社のAPI上でブラウザ操作型AIエージェントを構築する開発者が、安全対策設計の参考にする場合
- 招待制の限定パイロットでリスクを抑えながら新しいエージェント機能を段階的に検証したい製品チーム
