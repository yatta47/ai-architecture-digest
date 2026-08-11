---
type: case
title: 建設BIM特化の基盤モデルをCPT→SFT→RLVRの3段階パイプラインで構築
title_original: How ONESTRUCTION built the Ishigaki-IDS foundation model with AWS GenAIIC
company: ONESTRUCTION
industry: other
cloud:
- aws
patterns:
- fine-tuning
- reinforcement-learning
components:
- Amazon EC2 P5en
- AWS ParallelCluster
- Amazon FSx for Lustre
- Qwen3
- IDS-Audit-Tool
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-onestruction-built-the-ishigaki-ids-foundation-model-with-aws-genaiic/
published_at: '2026-08-11'
---

## 概要

建設BIM特化のドメインでは公開データが乏しく、IFC語彙やIDS特有の構文をモデルに学習させるのが課題だった。ONESTRUCTIONはQwen3をベースに、合成データを用いた継続事前学習(CPT)、指示応答ペアによるSFT、buildingSMARTのIDS-Audit-Toolを報酬関数とするRLVR(検証可能報酬による強化学習)を組み合わせた3段階パイプラインでIshigaki-IDSを構築した。AWS GenAIICの技術アドバイザリのもと、EC2 P5enとFSx for Lustreによる分散学習基盤で、データが乏しいニッチ領域でも短期間でドメイン特化モデルを実現した。

## 設計のポイント

- データが乏しいドメインでは合成データ生成でCPTの大部分を賄い、ドメイン知識をモデルに注入する
- SFTだけでは構造の妥当性が担保できないため、ルールベースの検証ツールを報酬関数としたRLVRを追加する
- モデルサイズ違い(8B/14B/32B)で小規模から実験し、本番投入前にコストを抑えて検証する
- 外部専門家との定期レビューでデータ設計・評価指標・学習手法を反復改善する

## 使いどころ

- 公開コーパスが少ないニッチな業界標準やドメイン固有フォーマットをLLMに習得させたいチーム
- 非専門家でも専門的な構造化ドキュメント(XML等)を扱えるようにしたいプロダクト
- 厳密な構文・語彙ルールを持つ出力を生成する必要があるドメイン特化エージェント
