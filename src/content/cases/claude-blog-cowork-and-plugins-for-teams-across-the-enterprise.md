---
type: announcement
title: 全社展開向けプライベートプラグイン市場とCowork連携基盤
title_original: Cowork and plugins for teams across the enterprise
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Claude Cowork
- Claude Agent SDK
- MCP
- OpenTelemetry
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/cowork-plugins-across-enterprise
published_at: '2026-02-24'
---

## 概要

Cowork管理者が組織専用のプライベートプラグイン市場を構築でき、コネクタ・Skill・プラグインを一元管理できるようにする機能拡張を発表。HR・デザイン・エンジニアリングなど部門別のプラグインテンプレートや、ExcelとPowerPointをまたぐ横断ワークフローも提供する。

## 設計のポイント

- プラグイン・Skill・コネクタを『Customize』という単一のメニューに統合し、管理者が組織全体の構成を一箇所で把握できるようにする
- スラッシュコマンドを構造化フォームで起動させ、非エンジニアでも決まったワークフローを迷わず実行できるようにする
- OpenTelemetryを組み込み、部門横断での利用状況・コスト・ツール利用をテレメトリとして可視化できるようにする

## 使いどころ

- 複数部門でClaudeを使っており、部門ごとに最適化されたプラグインを配布・統制したいエンタープライズ管理者
- ExcelでのモデリングからPowerPointでの資料化まで、アプリをまたぐ一連の作業をエージェントに任せたい知識労働者
