---
type: guidance
title: NVIDIA Metropolis VSSをコーディングエージェントで自動デプロイし、映像を検索可能なインテリジェンスに変換する
title_original: Transform Video Into Instantly Searchable, Actionable Intelligence with AI Agents and Skills
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- video-intelligence
- ai-agent
- rag
components:
- NVIDIA Metropolis Blueprint for VSS
- vision-language models
- large language models
- Codex
- OpenClaw
- NVIDIA Brev
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/transform-video-into-instantly-searchable-actionable-intelligence-with-ai-agents-and-skills/
published_at: '2026-06-22'
---

## 概要

NVIDIA Metropolis Blueprint for video search and summarization（VSS）は、ビジョン言語モデルとLLM、リトリーバを組み合わせて大量の映像をリアルタイムに検索・要約可能にするリファレンスアーキテクチャである。最新版ではエージェントスキルとして提供されるようになり、Codex・Claude Code・OpenClawなどのコーディングエージェントがVSSのデプロイやプロファイル設定、映像の取り込み・検索・要約ワークフローの構築までをチャットインターフェース経由で自動化できる。

## 設計のポイント

- デプロイ・検索・要約・アラート検証といった定型作業をエージェントスキル仕様に沿ったスキルとして提供し、複数のコーディングエージェントから共通の手順で呼び出せるようにする。
- 手動での各マイクロサービス設定を、コーディングエージェントとの自然言語チャットに置き換えることで、VSS導入の専門知識の壁を下げる。
- 既存のコンピュータビジョンパイプラインが検知したイベントクリップをVSSに連携し、VLMによるレビューやQ&Aへつなげるイベントレビュー構成も併用できる。

## 使いどころ

- 膨大な録画・ライブ映像から異常やトレンドをリアルタイムに検出したい監視・オペレーション部門。
- 映像分析基盤のセットアップに毎回時間がかかっており、コーディングエージェントで構築を自動化したい開発チーム。
- 既存のCVパイプラインにVLM/LLMベースのレビューやアラート検証を追加拡張したいチーム。
