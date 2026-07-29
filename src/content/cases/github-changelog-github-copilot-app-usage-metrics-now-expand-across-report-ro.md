---
type: announcement
title: GitHub CopilotアプリのAI利用状況を組織全体のレポートに統合
title_original: GitHub Copilot app usage metrics now expand across report rollups
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot
- GitHub Copilot app
- Copilot usage metrics API
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-28-github-copilot-app-usage-metrics-now-expand-across-report-rollups
published_at: '2026-07-28'
---

## 概要

GitHub Copilotアプリの利用実績が、enterprise/organization向けユーザー別レポートやfeature・model・language別の集計に統合された。個々のユーザーが生成したコード量やどのモデル・言語で作業しているかを、IDEやチャットなど他のCopilot利用面と同じ指標で横断比較できるようになった。既存フィールドの構造は変えず後方互換性を保っている。

## 設計のポイント

- 既存のレポートスキーマ（totals_by_feature等）にAIアプリの利用実績を後方互換な形で追加し、既存の集計ロジックを壊さずに拡張する。
- ユーザー単位の利用有無(used_copilot_app)とセッション・トークン使用量を分離して記録し、アダプションと生産量の両方を追跡できるようにする。
- 利用実績がないユーザー/組織ではフィールド自体を省略し、レスポンスサイズと解析の複雑さを抑える。

## 使いどころ

- エンタープライズ管理者がCopilotアプリの利用者を特定し、展開状況を可視化したい場合。
- IDE・チャット・コードレビュー・エージェントなど複数のAI利用面を同じ指標で横断比較したい場合。
- AIコーディングツールのコスト管理やガバナンスレポートに利用実績を組み込みたい場合。
