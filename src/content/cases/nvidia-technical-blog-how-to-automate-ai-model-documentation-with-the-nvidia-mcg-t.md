---
type: announcement
title: NVIDIA MCGツールキットによるAIモデルカード自動生成
title_original: How to Automate AI Model Documentation with the NVIDIA MCG Toolkit
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
- multi-cloud
patterns:
- rag
- document-processing
- llmops
- eval
components:
- NVIDIA Inference Microservices (NIM)
- GPT-OSS-120B
- NVIDIA Nemotron RAG
- Oracle Cloud Infrastructure (OCI)
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-automate-ai-model-documentation-with-the-nvidia-mcg-toolkit/
published_at: '2026-06-30'
---

## 概要

NVIDIAのModel Card Generator(MCG)ツールキットは、ソースコードやドキュメントを直接読み込み、RAGパイプライン(NVIDIA NIMによる埋め込み・リランキングとGPT-OSS-120Bによる抽出)を使ってAIモデルカードをModel Card++形式で自動生成する。Ingestion→Extraction→Renderingの3段階構成で1分未満・完了率91%・精度76%を達成し、情報不足の項目は推測せず欠落をフラグする。Oracleは早期採用企業としてOCI AIインフラにこのツールキットを組み込み、モデル文書化とGPUリソース最適化に活用している。

## 設計のポイント

- Ingestion→Extraction→Renderingの3段階モジュール型パイプラインとし、各ステージを独立コンテナ化して個別に交換可能にする
- コード・設定ファイル・ドキュメントごとに専用のリトリーバーを用意し、高精度な埋め込み・リランキングモデルで情報源の優先度をつける
- 出力形式をModel Card++テンプレートと構造化JSONに固定し、テンプレートのみ差し替えれば規制要件の変化に追従できるようにする
- 情報が不足する項目は推測せずに欠落フラグを立て、文書生成ツールをギャップ検出ツールとしても機能させる

## 使いどころ

- EU AI ActやCalifornia AB-2013など強まる規制の下でモデルカードを迅速かつ監査可能に整備したいAI/MLプラットフォームチーム
- GitHub・GitLab・HuggingFace上の多数のモデルリポジトリのドキュメントを一括で標準化したい場合
- GPUクラスタ運用と合わせてモデル文書化を自動化したいクラウドプロバイダやエンタープライズのAI基盤チーム
