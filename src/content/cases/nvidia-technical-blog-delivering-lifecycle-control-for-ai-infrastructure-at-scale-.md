---
type: announcement
title: NVIDIA DGX Spark/GB10向けEnterprise ManageabilityフレームワークによるエージェントレスなAIインフラのライフサイクル管理
title_original: Delivering Lifecycle Control for AI Infrastructure at Scale with NVIDIA DGX Spark Enterprise Manageability
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- root-cause-analysis
- defense-in-depth
components:
- NVIDIA DGX Spark
- NVIDIA GB10
- Canonical Landscape
- Progress Chef
- Perforce Puppet
- spark_diagctl.py
- reset_reason_reporter.py
- cloud-init
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/delivering-lifecycle-control-for-ai-infrastructure-at-scale-with-nvidia-dgx-spark-enterprise-manageability/
published_at: '2026-06-25'
---

## 概要

NVIDIAはDGX SparkおよびGB10システム向けに、調達からEnd-of-Lifeまでの6フェーズを網羅するモジュール型のEnterprise Manageabilityフレームワークを提供開始した。常駐エージェントを置かずSSH経由で実行し標準化されたJSON出力を返す方式により、Chef・Puppet・Canonical Landscapeなど既存のIT管理ツールやCMDB/SIEMパイプラインにそのまま統合できる。診断ツールspark_diagctl.pyやreset_reason_reporter.py、Custom Installationによる事前構成機能により、インターネット接続環境だけでなく完全エアギャップ環境でも一貫した運用・診断・セキュリティ監査が可能になる。

## 設計のポイント

- 常駐エージェントを置かずSSH経由で実行し、すべてのツールが同じ構造の標準JSON(status/rc/summary/warnings/artifacts)を返す設計により、任意のオーケストレーション基盤やCMDB/SIEMへの統合を容易にしている。
- 読み取り専用で高頻度実行可能な『コレクタ』と、状態変更を伴い最小権限sudo・変更管理承認が必要な『コントローラ』を明確に分離し、既存のエンタープライズITガバナンスモデルにそのまま対応させている。
- 診断をL1(高速・軽量なヘルスサマリー)とL2(GPUテレメトリやカーネルログを含む詳細証跡バンドル)の2段階に分け、常時監視とインシデント時の深掘り調査を両立している。
- cloud-initとOEMデータパーティション、プロビジョニングフックスクリプトを用いたCustom Installationにより、追加インフラなしでインターネット接続環境と完全エアギャップ環境の両方で既知良好状態の初期構成を実現している。

## 使いどころ

- 複数拠点にDGX Sparkを展開する企業ITチームが、常駐エージェントを追加導入せずに既存のCMDB/SIEM/監視パイプラインへ組み込みたい場合。
- 金融・防衛・政府機関など、インターネット接続が制限または禁止されたエアギャップ環境でAIインフラを調達からEoLまで一貫管理したい場合。
- GPUインフラの予期しない再起動やファームウェア/PCIe障害を、現地対応なしにリモートで一次切り分け・エスカレーション用証跡収集したい運用チーム。
- 検証済みブートやRBAC、chain-of-custodyを備えた形でハードウェアの調達からリタイアまでの証跡を残したいセキュリティ/コンプライアンス担当者。
