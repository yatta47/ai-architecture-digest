---
type: guidance
title: EKSとAKSのストレージオプション比較によるKubernetesクラスタ移行ガイド
title_original: Storage options for a Kubernetes cluster
ai_relevant: false
industry: cross-industry
cloud:
- aws
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/aws-professional/eks-to-aks/storage
published_at: '2026-06-04'
---

## 概要

Amazon EKSに慣れたエンジニアがAzure Kubernetes Service（AKS）のストレージ設計を理解できるよう、両サービスの一時ボリューム・永続ボリュームの選択肢を対比した記事。EBSやEFS、FSx for LustreなどEKS側の代表的なストレージオプションと、それぞれのCSIドライバやバックアップ手段（AWS Backup、Velero等）の役割を整理し、AKSへの移行時にどのAzureストレージを選ぶべきかの判断材料を提供している。
