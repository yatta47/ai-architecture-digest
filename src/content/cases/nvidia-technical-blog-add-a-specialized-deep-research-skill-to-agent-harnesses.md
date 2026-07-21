---
type: guidance
title: エージェントハーネスへのAI-Qディープリサーチスキル統合
title_original: Add a Specialized Deep Research Skill to Agent Harnesses
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- document-processing
- rag
- out-of-band-inference
components:
- NVIDIA AI-Q
- Claude Code
- Codex
- OpenCode
- NeMo Agent Toolkit
- MCP
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/add-a-specialized-deep-research-skill-to-agent-harnesses/
published_at: '2026-06-11'
---

## 概要

NVIDIA AI-Qはマルチドキュメント統合や出典付き意思決定ブリーフ生成などのディープリサーチ機能を、オープンソースのポータブルなエージェントスキルとしてパッケージ化した。Claude Code、Codex、OpenCodeなどのエージェントハーネスはこのスキルをインストールするだけで、ローカルまたはホストされたAI-Qサーバーにリサーチタスクを委譲し、構造化された引用付きレポートを受け取れる。さらにMCP経由で認証済みの企業データソースに接続する3つの統合パターンが用意されており、機密データを企業環境内に留めたまま利用できる。

## 設計のポイント

- リサーチパイプライン（意図分類、明確化、浅い調査、深い調査、評価）全体をAI-Qサーバー側に集約し、ハーネス側はSKILL.mdとヘルパースクリプトを通じて非同期にジョブを投げてポーリングするだけにする。
- スキルはSKILL.mdと補助スクリプトという移植可能な形式で配布し、Claude Code/Codex/OpenCodeなど複数のハーネスに同じ資産を再利用できるようにする。
- MCPサーバーへの認証は、無認証・サービスアカウント認証・ユーザーのベアラートークン転送の3パターンに分類し、用途に応じて使い分ける。
- AI-QはDocker ComposeやHelmチャートで企業データと同じ環境にデプロイできるようにし、機密データを外部に出さずに検索・統合できるようにする。

## 使いどころ

- Claude CodeやCodexなど既存のエージェントハーネスに、独自のリサーチパイプラインを実装せずディープリサーチ能力を追加したい開発チーム。
- 医療、金融、政府、防衛など機密データを扱う規制産業で、出典付きの調査レポートを社内データに閉じたまま生成したい場合。
- 社内の複数システム（MCP経由）にまたがる情報を横断的に調査し、引用付きの意思決定資料を作成したい業務担当者。
