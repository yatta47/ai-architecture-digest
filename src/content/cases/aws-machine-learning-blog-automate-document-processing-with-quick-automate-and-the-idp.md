---
type: case
title: 抵当貸付の書類処理をIDP AcceleratorとQuick Automateで自動化
title_original: Automate Document Processing with Quick Automate and the IDP Accelerator
industry: financial-services
cloud:
- aws
patterns:
- document-processing
- cost-optimization
components:
- Amazon Textract
- Amazon Bedrock
- Amazon Quick Automate
- GAIIC IDP Accelerator
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automate-document-processing-with-quick-automate-and-the-idp-accelerator/
published_at: '2026-08-19'
---

## 概要

年間5万件のローンを扱う中堅モーゲージ貸し手（架空事例）が、AWS Generative AI Innovation Centerのオープンソース IDP Accelerator と Amazon Quick Automate を組み合わせ、書類の分類・データ抽出・下流システムへのルーティングを完全自動化した。Amazon TextractとAmazon Bedrockが書類の分類と構造化データ抽出を担い、Quick Automateがコード不要のワークフローで抽出結果をローン組成システムへ振り分ける。1件あたりの処理時間は15〜20分から6分未満へ短縮された（想定シナリオ）。

## 設計のポイント

- サーバーレスのIDP Acceleratorが文書のOCR・分類・構造化データ抽出・スキーマ照合による異常検知までを担い、処理量に応じて自動スケールし処理件数課金で固定インフラコストを持たない
- 抽出だけでなく下流ルーティングまでを担当領域として分離し、Quick Automateのノーコードワークフローで承認・検証・例外処理の分岐を組む
- ドキュメント→抽出→ワークフローという流れを疎結合にすることで、借り換えやHELOC、商業融資など新しい書類タイプをインフラ再構築なしに追加できる
- ピーク期の一時要員採用に頼らず、サーバーレスの自動スケールでボリュームスパイクに対応する

## 使いどころ

- 書類の分類・抽出・検証を手作業で行っており、繁忙期に人員コストが跳ね上がる金融・保険・医療・公共部門の書類集約型業務
- 抽出したデータを複数の下流システムへ振り分けるワークフローをコードを書かずに構築したいチーム
- 新しい書類種別が頻繁に増える業務で、都度インフラを作り直したくない場合
