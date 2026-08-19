---
type: case
title: 医療画像DICOMのPHI/PII自動検出をAmazon Bedrockで実現
title_original: How Clario technology detects PHI/PII in DICOM images using Amazon Bedrock
company: Clario (Thermo Fisher Scientific)
industry: healthcare
cloud:
- aws
patterns:
- document-processing
- guardrails
components:
- Amazon Bedrock
- Claude Sonnet 4.5
- Amazon Textract
- Amazon API Gateway
- AWS IAM
- Amazon CloudWatch
- AWS CloudTrail
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-clario-automates-phi-pii-detection-in-dicom-images-using-amazon-bedrock/
published_at: '2026-08-19'
---

## 概要

Clarioは臨床試験で扱う大量のDICOM画像スライスから、メタデータやタグ、画素に埋め込まれたPHI/PIIを検出するため、Amazon BedrockのClaude Sonnet 4.5とAmazon Textractを組み合わせた自動検出基盤を構築した。マネージド基盤モデルとOCRを活用することで、再アーキテクチャなしに数百万枚規模までスケールしつつ、HIPAA/GDPR/ICH E6などの規制要件に沿った監査可能なワークフローを実現している。

## 設計のポイント

- マネージドの基盤モデルとOCRサービスを採用し、モデル運用やインフラのチューニングを外部委託することでスケーラビリティを確保する
- IAM・VPC制御・暗号化を備えたハードニング済みAWS環境内で処理を完結させ、セキュリティとデータレジデンシー要件に対応する
- CloudWatch/CloudTrailによるログ・メトリクス・トレースの一元化で、規制監査に耐える運用ガバナンスを組み込む

## 使いどころ

- 医療画像を扱う臨床試験のスポンサーやCROが、施設横断でPHI/PII除去を標準化したいとき
- DICOMメタデータとピクセル双方に潜む個人情報を、人手レビューなしに大量処理したい場合
- 規制対応（HIPAA/GDPR/ICH E6）を前提としたAI基盤運用の監査証跡設計を検討する場面
