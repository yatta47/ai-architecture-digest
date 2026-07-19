---
type: opinion
title: AIワークロードはどこで動かすべきか—Kubernetesを軸にした主権的インフラ選択
title_original: Where Should AI Workloads Run? A Sovereign and Sensible Approach
company: KubeOps
industry: public-sector
cloud:
- on-prem
- multi-cloud
patterns:
- unified-runtime
- policy-as-code
- disaster-recovery
components:
- Kubernetes
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/10/where-should-ai-workloads-run-a-sovereign-and-sensible-approach/
published_at: '2026-07-10'
---

## 概要

KubeOpsは、AIワークロードをどこで実行すべきかという問いに対し、Kubernetesが資源管理・自動化・移植性・運用一貫性の面で共通基盤になりつつあると論じる。デジタル主権を『運用自律性・コンプライアンス・監査可能性・移植性・レジリエンス』の5要素として捉え、機密性の高いタスクはオンプレミスやプライベートクラウドへ、非機密タスクや検証環境は外部ホスティングへ、といった使い分けと、コストや規制、モデル性能の変化に耐えられる移植可能なプラットフォーム設計を提案している。

## 設計のポイント

- 全てのAIワークロードを一律にクラウドAPIへ寄せるのではなく、機密性・規制要件に応じてオンプレミス/プライベートクラウド/外部ホスティングを使い分ける
- デジタル主権を運用自律性・コンプライアンス・監査可能性・移植性・レジリエンスの5要素に分解し、要件チェックリストとして扱う
- 本番投入前にアクセラレータ容量・ストレージ性能・データ局所性・ネットワーク分離・ID統合・監視・バックアップ・脆弱性管理・ポリシー適用などのAIレディネスチェックを行う
- Kubernetes/CNCFエコシステムを共通基盤に採用し、特定のモデル・プロバイダ・配置先を前提にしない移植可能な運用でベンダーロックインや将来の要件変化に備える

## 使いどころ

- 公共部門や重要インフラなど高度規制業界で、データ主権・コンプライアンスを重視しつつAI基盤を構築したい組織
- AIワークロードをオンプレミス・プライベートクラウド・エッジ・マルチクラウドにまたがって将来移動させる可能性がある企業のプラットフォームチーム
- サブスクリプション型AIサービスのコスト高騰やベンダーロックインを避けたい意思決定者
