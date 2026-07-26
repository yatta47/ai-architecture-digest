---
type: guidance
title: HarnessでRAGアプリケーションのCI/CD・セキュリティ・コスト管理を自動化するパイプライン
title_original: Harness CI/CD pipeline for RAG applications
industry: cross-industry
cloud:
- gcp
patterns:
- ci-cd
- rag
- policy-as-code
components:
- Harness CI
- Harness CD
- Harness STO
- Harness SCS
- Harness FME
- Harness CCM
- Cloud Run
- Artifact Registry
- Cloud Logging
- Cloud Monitoring
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/partners/harness-cicd-pipeline-for-rag-app
published_at: '2026-07-19'
---

## 概要

RAG対応生成AIアプリケーションをCloud Runへ継続的にデプロイするためのCI/CDパイプライン。HarnessのCI/CD・セキュリティテスト・サプライチェーンセキュリティ・機能フラグ・コスト管理を組み合わせ、カナリアリリースと承認ゲートで安全に本番反映する。

## 設計のポイント

- SAST/DAST/SCAのセキュリティスキャンとSBOM生成をパイプラインに組み込み、リリース前に脆弱性とライセンスリスクを検出する
- 開発→ステージング→本番の各段階でカナリア・ブルーグリーンのトラフィックシフトと承認ゲートを設け、失敗時は自動ロールバックする
- 機能フラグで新機能を限定的なトラフィックに公開し、コスト管理システムでリソース利用の異常検知とオートスケーリング提案を行う

## 使いどころ

- 生成AIアプリケーションを頻繁に更新しつつ、セキュリティ・コンプライアンス・コストを継続的に管理したいDevOpsチーム
- サプライチェーンセキュリティ（SBOM・来歴検証）が求められる規制業種のRAGアプリケーション運用
