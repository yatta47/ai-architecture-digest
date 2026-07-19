---
type: case
title: 実験機器データを継続的に構造化しAIレディな科学データ基盤を実現
title_original: 'From Experiment to Insight: How Dotmatics Luma and Databricks Make AI-Ready Science a Reality'
company: Dotmatics
industry: healthcare
cloud: []
patterns:
- data-federation
- context-engineering
components:
- Dotmatics Luma
- Databricks
- Delta Sharing
- Unity Catalog
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/experiment-insight-how-dotmatics-luma-and-databricks-make-ai-ready-science-reality
published_at: '2026-07-16'
---

## 概要

科学データプラットフォームDotmatics Lumaは、多数の実験機器から出力される断片化データを自動収集し、FAIR準拠の構造化された「科学記録」へリアルタイムに変換する。基盤にDatabricksを用いることでエンタープライズ規模のガバナンスとAI活用を両立し、断片化したデータのままAIに学習させると信頼できない結果になるという課題に、機器接続とハーモナイゼーションで対処している。

## 設計のポイント

- 機器からの出力を継続的・自動的に取り込み、実験の途中で失われがちなメタデータ・系譜・文脈をデジタルスレッドとして保持する。
- 科学領域に特化したLumaと汎用データ基盤のDatabricksを分離し、それぞれの専門性（科学的文脈 vs スケーラブルなガバナンス）を組み合わせる。
- Delta Sharingにより、CROや学術パートナーなど外部組織とガバナンスを損なわずにデータを共有できるようにする。
- データ痛みが最も大きい領域（例: クロマトグラフィー）から着手し、価値を実証してから他のモダリティへ展開する反復可能なモデルを採用する。

## 使いどころ

- 複数ベンダーの実験機器からのデータをAIで解析可能な形に統合したい研究開発組織。
- 監査可能性とトレーサビリティが要求される創薬・規制提出プロセスにAIを組み込みたいライフサイエンス企業。
- 研究データを財務・調達など他の企業データと同じガバナンス基盤上で扱いたい組織。
