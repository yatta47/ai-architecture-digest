---
type: case
title: Amazon Novaで実現する介護施設向け医療文書処理パイプライン
title_original: How Guardoc transforms medical document processing with Amazon Nova models
company: Guardoc Health
industry: healthcare
cloud:
- aws
patterns:
- rag
- document-processing
- multi-model-routing
- cost-optimization
components:
- Amazon Nova Pro
- Amazon Nova 2 Lite
- Amazon Bedrock
- Amazon Textract
- Amazon Titan Text Embeddings V2
- Amazon DynamoDB
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-guardoc-transforms-medical-document-processing-with-amazon-nova-models/
published_at: '2026-07-27'
---

## 概要

介護施設向けに医療文書処理を手がけるGuardoc Healthは、手書き注釈・チェックボックス・混在フォーマットなど非定型な医療記録から症状を高精度に検出する課題に取り組んだ。Amazon TextractによるOCR抽出、Amazon Titan Text Embeddings V2による患者単位のベクトル化、Amazon Nova 2 LiteとNova Proを組み合わせたコスト階層型のRAGパイプラインを構築し、症状分類にページ単位のマルチモーダル推論まで行う。この結果、文書処理エラーを46%削減し、監査による罰金を70%削減、1施設あたり年間40万ドル超のROIを実現した。

## 設計のポイント

- 臨床的に意味のある単位（投薬リスト・診断セクションなど）に沿ってチャンク分割し、任意のバイト長で区切らないようにする
- 埋め込みとインデックスは患者ごとにパーティション化し、共有ベクトルインデックスに依存せず患者数に応じて水平スケールする
- 軽量モデル（Nova 2 Lite）で明らかな非該当を先に除外し、最終判定だけ高コストなマルチモーダルモデル（Nova Pro）に回すコスト階層設計にする
- すべての分類結果を元の該当ページに遡って紐付け、根拠を追跡可能にする

## 使いどころ

- 手書き・印字・チェックボックス・表形式が混在する医療文書を大量に処理する介護施設や医療機関
- 1日100万件規模の文書量でも1%のエラーが重大なコンプライアンスリスクになるような高ボリューム×高精度が要求される業務
- プライアーオーソリゼーションフォームなどチェックボックスの状態が保険適用可否を左右する文書処理
