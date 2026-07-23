---
type: announcement
title: Claude Opus 4.6によるファイナンス業務の高度化とCowork/Excel/PowerPoint連携
title_original: Advancing finance with Claude Opus 4.6
company: Anthropic
industry: financial-services
cloud: []
patterns:
- ai-agent
- document-processing
- eval
components:
- Claude Opus 4.6
- Claude in Excel
- Claude in PowerPoint
- Cowork
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/opus-4-6-finance
published_at: '2026-02-05'
---

## 概要

AnthropicはClaude Opus 4.6のリリースに合わせ、財務分析・投資調査向けの性能向上（Finance AgentやTaxEvalでの最高水準達成）と、それを活かす製品群を発表した。デスクトップフォルダに直接アクセスして複数の分析を並行して進められる新機能Cowork、より複雑な財務モデルに対応したClaude in Excel、新たにベータ公開されたClaude in PowerPointにより、デューデリジェンス資料やプレゼン資料の初稿作成を数週間から数分単位に短縮できるとしている。

## 設計のポイント

- 汎用チャットではなくExcelやPowerPointといった既存の実務ツールにサイドバーとして組み込み、既存のワークフローの中でモデルを使わせる
- デスクトップのフォルダ単位でファイルの読み書き権限を与えるCoworkにより、複数の分析タスクを並行して進めながら人間が思考プロセスを都度ステアリングできるようにする
- スキルとコネクタを束ねたプラグイン機構により、仕訳・差異分析・調整など業務固有の定型ワークフローをテンプレート化する
- Real-World Finance・Finance Agent・TaxEvalなど業務に即したベンチマークで継続的に定量評価し、モデル更新ごとの実務上の進歩を可視化する

## 使いどころ

- 投資銀行やPEファームのアナリストがデューデリジェンス資料や財務モデルの初稿作成を高速化したい場合
- コーポレートファイナンスチームが仕訳・分散分析・照合などの定型的な経理業務を自動化したい場合
- クライアント向けプレゼン資料を既存テンプレートのレイアウトを踏襲しながら素早く作成・修正したいチーム
