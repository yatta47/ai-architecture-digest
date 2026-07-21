---
type: announcement
title: Claude Code・Claude CoworkがFedRAMP High認証環境で政府機関向けに提供開始
title_original: Bringing Claude Code and Claude Cowork to government
industry: public-sector
cloud: []
patterns:
- ai-agent
- guardrails
components:
- Claude Code
- Claude Cowork
- Claude for Government Desktop
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government
published_at: '2026-07-07'
---

## 概要

Claude for Government DesktopがFedRAMP High認証環境上でClaude CodeとClaude Coworkのパブリックベータ提供を開始した。予算に紐づく支出管理、部門ごとの権限委譲、ハッシュチェーン監査ログなど、政府機関のATOプロセスに対応するガバナンス機能を備える。

## 設計のポイント

- 会話履歴を機関管理デバイス側にローカル保存し、推論のみFedRAMP High認証環境内で実行する構成にする
- SCIMグループマッピングでレート制限・支出上限・利用可能モデルをシート階層ごとに設定できるようにし、部門組織構造に合わせた委任管理を可能にする
- 全ての管理操作をハッシュチェーン監査ログに記録し、機微な操作は二者承認を必須にすることでATO/IG対応のオーバーサイトを組み込む

## 使いどころ

- FedRAMP High相当のセキュリティ要件下でAIエージェントを導入したい政府機関
- 予算配分とサブ機関への権限委譲を伴う調達・管理を行う公共部門のIT管理者
