---
type: announcement
title: Azure Copilotで実現するエージェント型クラウド運用――可観測性・ガバナンス・最適化の統合
title_original: 'From insight to action: The next phase of agentic cloud operations'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- root-cause-analysis
- cost-optimization
- policy-as-code
components:
- Azure Copilot
- Azure Copilot observability agent
- Azure Resource Manager MCP Server
outcome:
  type: speed
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/from-insight-to-action-the-next-phase-of-agentic-cloud-operations/
published_at: '2026-06-23'
---

## 概要

Microsoftは、AIエージェントが継続的に観測・推論・アクションを行う「エージェント型クラウド運用」を提唱し、可観測性・ガバナンス・最適化を1つのループとして統合するビジョンを示した。GAとなったAzure Copilot観測エージェントはテレメトリを継続分析してインシデントの検知から根本原因調査までを支援し、プレビュー中のAzure Resource Manager MCP Serverはコスト/使用状況データを標準インターフェースで外部ツールに公開する。KPMGでは同エージェント導入により月間約250時間の工数削減を実現したと報告されている。

## 設計のポイント

- 可観測性から得たシグナルをそのままアクションに直結させず、ポリシー・アクセス制御・監査可能性を備えたガバナンス層を間に挟むことでエージェントの行動を統制する
- 観測エージェントはアプリのトポロジー・依存関係・ベースライン挙動を常時分析し、関連シグナルを自動グルーピングしてノイズを削減した上で根本原因調査を先行実施する
- コスト最適化はMCPサーバーを介して標準化されたインターフェースで公開し、ポータル外の開発環境やカスタムワークフローからも自然言語でコスト調査・最適化を行えるようにする
- 最適化を定期レビュー型の別作業ではなく、リソース作成前のコスト提示など日常の開発・運用フローに組み込み継続的な改善サイクルとする

## 使いどころ

- ハイブリッドインフラ・マイクロサービス・AIワークロードが混在し、シグナル相関や原因調査に多くの工数を割いている運用チーム
- インシデント対応時間の短縮とオペレーション負荷の軽減を目指すSRE/クラウド運用チーム
- AIワークロードにより利用パターンが変動的になり、従来の定期コストレビューでは対応しきれなくなったFinOps担当者
- デプロイ前にコスト影響とポリシー適合性を把握した上で開発を進めたいアプリケーション開発者
