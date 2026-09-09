---
type: announcement
title: Copilot横断検索を備えた統合サポートポータル
title_original: 'New customer portal: help.github.com'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- rag
components:
- GitHub Copilot
- help.github.com
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-08-new-customer-portal-help-github-com
published_at: '2026-09-08'
---

## 概要

GitHubはサポート・ドキュメント・学習コンテンツ・コミュニティ・アカウント管理を1つに束ねた新ポータルhelp.github.comを立ち上げ、サインイン不要でCopilotによる横断検索・自動応答を提供する。数週間かけて段階的にロールアウトし、旧サイトsupport.github.comも並行して稼働を続ける。

## 設計のポイント

- 分散していた複数のサポート/ドキュメントサイトを単一の入口に統合し、ナビゲーションの手数を削減
- Copilotによる検索を横断的にかけることでサインイン前でもセルフサーブの回答を可能にする
- 段階的ロールアウトで旧ポータルを並行稼働させ、移行時の可用性リスクを抑える

## 使いどころ

- ヘルプ/ドキュメント/コミュニティ情報が複数サイトに分散し、ユーザーが情報を探しにくい大規模プロダクト
- サインイン前のユーザーにもセルフサーブでAIによる回答を提供したいサポート窓口
