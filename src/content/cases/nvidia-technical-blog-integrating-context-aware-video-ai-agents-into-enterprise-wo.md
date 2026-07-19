---
type: guidance
title: 映像分析エージェントを企業ワークフローに接続しチケット起票まで自動化
title_original: Integrating Context-Aware Video AI Agents Into Enterprise Workflows
industry: cross-industry
cloud: []
patterns:
- ai-agent
- video-intelligence
- rag
- human-in-the-loop
components:
- NVIDIA NemoClaw
- NVIDIA Metropolis VSS Blueprint
- NVIDIA AI Blueprint for RAG
- Jira
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/
published_at: '2026-07-16'
---

## 概要

NVIDIA NemoClawがVideo Search and Summarization（VSS）BlueprintとRAG Blueprintをオーケストレーションし、映像分析の結果を組織固有の知識で裏付けたレポートに変換したうえで、Jiraチケットなど下流業務システムへ自動的につなげる仕組みを解説する。人間参加型（HITL）プロンプトでユーザー意図を先に確定させてから処理を始める設計により、「映像に何が映っているか」から「それに対して何をすべきか」へと踏み込んでいる。

## 設計のポイント

- 映像処理を始める前にHITLプロンプトでシナリオ・検出対象・参照したい知識を確定させ、意図に合わない分析結果を後から手戻りさせない。
- 映像理解ツールが先にRAG Blueprintへ問い合わせて組織固有の参照知識を取得し、その文脈を織り込んだうえで長尺映像を階層的に要約する。
- レポート生成ツールがタイムスタンプ付きの検出結果・根拠文書への引用・推奨アクションを1つの構造化レポートにまとめ、下流システムへのアクション生成につなげる。

## 使いどころ

- 映像から得た知見を業務システム（チケット管理、エスカレーション経路など）に自動連携させたい現場。
- 規定文書やSOPなど組織固有の知識と映像内容を突き合わせて判断根拠を示したい監査・品質管理業務。
- バッチ実行時にはHITLの回答をプログラムから供給し、大量の映像を自動処理したいケース。
