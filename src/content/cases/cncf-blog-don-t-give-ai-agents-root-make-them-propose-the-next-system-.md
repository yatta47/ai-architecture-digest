---
type: opinion
title: AIエージェントにrootを渡さず次のシステム状態を提案させる設計
title_original: 'Don''t give AI agents root: make them propose the next system state'
company: Kairos
industry: cross-industry
cloud: []
patterns:
- ai-agent
- policy-as-code
- human-in-the-loop
- defense-in-depth
components:
- bootc
- Flatcar Container Linux
- Kairos
- Kubernetes
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/08/dont-give-ai-agents-root-make-them-propose-the-next-system-state/
published_at: '2026-10-08'
---

## 概要

エージェントに本番のroot権限を与えず、ベースシステムの変更を版管理された定義と新しいイメージとして提案させ、レビューと来歴を通して適用すべきだと論じる。コンテナと不変ホストによる境界を土台にするが、不変性だけではサンドボックスにならない点も指摘する。

## 設計のポイント

- ランタイムで状態を即興で変えず、別の場所で作った定義済みの状態を実行する。
- エージェントは調査はできるが、ベースシステムの変更はコミットとイメージ更新で表現させる。
- ソース、ビルド、デプロイの来歴を残し、問題をコミットとイメージまで遡れるようにする。

## 使いどころ

- 自律エージェントに本番運用を任せる範囲を設計するプラットフォームチーム。
- イメージベースの不変ホストを検討する運用者。
