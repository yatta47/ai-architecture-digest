---
type: guidance
title: Amazon EKS 上に SageMaker AI Spaces でGPU共有型の対話IDE基盤を構築
title_original: Run interactive IDEs on Amazon EKS with SageMaker AI to power up your AI workflows
industry: cross-industry
cloud:
- aws
patterns:
- unified-runtime
- cost-optimization
components:
- Amazon SageMaker AI
- Amazon EKS
- AWS Load Balancer Controller
- Amazon Route 53
- AWS Certificate Manager
- AWS KMS
- Amazon EBS
- Amazon EFS
- Amazon Cognito
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/run-interactive-ides-on-amazon-eks-with-sagemaker-ai-to-power-up-your-ai-workflows/
published_at: '2026-08-10'
---

## 概要

Amazon EKS上でSageMaker AI Spacesアドオンを使い、データサイエンティストが使い慣れたクラスタ内でJupyterLab/Code EditorをGPUノード共有のまま起動できるようにする構成。ALB+Route53+ACMでTLSを終端し、EKS Pod IdentityでIAMロールをスコープし、EBS/EFSで永続化する。環境構築が数日からおよそ5分に短縮し、GPUノードの利用率を最大30%向上させる。

## 設計のポイント

- SageMaker AI Spacesアドオンにより、独立したJupyterHub環境を構築せずに既存EKSクラスタ上でGPU・ストレージ・IAMロールを共有したままインタラクティブIDEを提供する
- AWS Load Balancer ControllerがALBをパブリックサブネットに配置できるよう、事前に全サブネットへタグ付けしておくことが必須の前提条件
- EKS Pod IdentityでSpace Podごとにスコープされたロールを付与し、KMSでJWTを暗号化するAuthミドルウェアをTraefik経由でルーティングする
- 学習ワークロードとインタラクティブワークロードを同一クラスタに統合することでGPUノードの遊休時間を減らし、常時起動GPU環境のコストを回避する

## 使いどころ

- GPUを使うMLパイプラインの合間にデータサイエンティストが対話的にJupyterLab/VS Codeを使いたいチーム
- 常時起動の専用ノートブック環境のコストを避けつつGPUノードを共有したいプラットフォームチーム
- OIDC(Cognito)でのシングルサインオンなどエンタープライズ認証と統合したいAI基盤運用チーム
