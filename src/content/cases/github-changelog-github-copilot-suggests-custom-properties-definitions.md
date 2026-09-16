---
type: announcement
title: GitHub Copilotがカスタムプロパティの許可値候補を提案しガバナンスメタデータ整備を支援
title_original: GitHub Copilot suggests custom properties definitions
company: GitHub
industry: cross-industry
cloud: []
patterns:
- guardrails
components:
- GitHub Copilot
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-15-github-copilot-suggests-custom-properties-definitions
published_at: '2026-09-15'
---

## 概要

GitHub Copilotは組織のカスタムプロパティ定義を作成する際に、プロパティ名に応じた許可値の候補を提案する機能をパブリックプレビューで追加した。例えばFedRAMPのような複数選択プロパティにはコンプライアンス関連の値を、internet-facingのような単一選択プロパティにはyes/noを提案し、ワンクリックで採用できるようにすることで、大規模なリポジトリ群に一貫したガバナンスメタデータを整備しやすくする。

## 設計のポイント

- カスタムプロパティの名前からCopilotが妥当な許可値候補を推論し提案する
- 提案をワンクリックで採用できるようにし、メタデータの表記ゆれを防ぐ
- ポリシー設定でこの提案機能自体の有効・無効を組織単位で制御できるようにする

## 使いどころ

- 多数のリポジトリに一貫した命名規則でガバナンスメタデータを付与したいエンタープライズ管理者
- どのカスタムプロパティやどんな値を定義すべきか判断に迷う組織オーナー
