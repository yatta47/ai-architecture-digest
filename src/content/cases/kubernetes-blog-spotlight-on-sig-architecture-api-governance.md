---
type: opinion
title: KubernetesのAPI Governanceはどう安定性と進化を両立するか
title_original: 'Spotlight on SIG Architecture: API Governance'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: quality
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/02/12/sig-architecture-api-spotlight/
published_at: '2026-02-12'
---

## 概要

Kubernetes BlogによるSIG Architecture: API Governanceのリード、Jordan Liggittへのインタビュー。REST APIだけでなくCLIフラグや設定ファイルなど全てのAPI表面で「安定性」と「変化の許容」を両立させる方針や、KEPプロセスにおける設計時/実装時のAPIレビューの使い分けを語る。Custom Resource Definitions(CRD)が「何でも定義できる」自由をもたらした一方でスキーマ検証の整備に時間を要し、直近のリリースでビルトインの検証機能がようやくGAに達した経緯を振り返っている。
