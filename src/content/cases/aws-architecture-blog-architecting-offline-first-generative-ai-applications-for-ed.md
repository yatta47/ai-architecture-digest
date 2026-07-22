---
type: guidance
title: エッジ拠点向けオフラインファースト生成AIのリファレンスアーキテクチャ
title_original: Architecting offline-first generative AI applications for edge deployments using AWS services
industry: manufacturing
cloud:
- aws
patterns:
- rag
- fine-tuning
- out-of-band-inference
- llmops
components:
- Amazon S3
- Amazon Bedrock
- Amazon SageMaker AI
- AWS IoT Greengrass
- Strands Agents
- ChromaDB
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/architecting-offline-first-generative-ai-applications-for-edge-deployments-using-aws-services/
published_at: '2026-07-22'
---

## 概要

クラウド接続が不安定・不可な工場や遠隔地の現場向けに、モデルのカスタマイズやデプロイ管理はクラウド側で行い、推論自体はエッジ側で完結させるオフラインファースト構成のリファレンスアーキテクチャ。Amazon BedrockやSageMaker AIでのモデル準備、IoT Greengrassによるデプロイ配信、エッジ上のStrands Agentsによるローカル推論を組み合わせ、ファインチューニングとRAGを併用するハイブリッド方式を採用している。

## 設計のポイント

- モデルのカスタマイズ戦略(FT/CPT/RAGおよびその組み合わせ)はユースケースの要件から逆算して選定する
- RAGパイプライン(ChromaDB+埋め込みモデル)をCPU/SSD上で完結させ、限られたVRAMをLLM推論専用に確保する
- クラウドとエッジ間はIoT Greengrassのデバイス証明書によるmTLSで通信し、各サービスは最小権限のIAMロールで分離する
- ドキュメントは512トークン単位・50トークンオーバーラップでチャンク化し、5GB規模のデータでも検索レイテンシを50ms未満に保つ

## 使いどころ

- 洋上プラットフォームや遠隔掘削現場など衛星回線が不安定な保守クルーが安全手順や設備マニュアルに即座にアクセスしたい場合
- 遠隔地の農業施設で精密農業機器のマニュアルや栽培・安全プロトコルをオフラインで参照したい場合
- 製造現場の作業員がリアルタイムのログとマニュアルを突き合わせて障害対応を行いたい場合
