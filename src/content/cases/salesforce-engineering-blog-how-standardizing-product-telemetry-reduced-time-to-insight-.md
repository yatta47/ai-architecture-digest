---
type: case
title: Salesforceが数百製品のテレメトリを標準化しインサイトまでの時間を97%短縮
title_original: How Standardizing Product Telemetry Reduced Time to Insight by 97%
ai_relevant: false
company: Salesforce
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-standardizing-product-telemetry-reduced-time-to-insight-by-97/
published_at: '2026-08-11'
---

## 概要

Salesforceでは製品チームごとに独自のテレメトリ実装とダッシュボードを構築しており、計装からメトリクス反映まで約1ヶ月かかるうえ、信頼できる指標を出すための手作業が製品ごとに重複していた。共通のProduct Data Platform(PDP)を導入し、必須フィールドとガバナンスされた任意属性からなる標準スキーマに一度計装するだけで、自動パイプラインが日次で1日45億行・19,000イベントを処理して製品採用指標を生成できるようにした。結果として計装からインサイト反映までの時間が約97%短縮され、標準化されたデータ基盤はAIパワードのMCPプラグインなど下流の分析ツールの土台にもなった。
