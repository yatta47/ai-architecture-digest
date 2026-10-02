---
type: announcement
title: NVIDIA DOCAのAIエージェントスキルでBlueField開発を正確化
title_original: Build Applications on NVIDIA BlueField Faster with NVIDIA DOCA Agent Skills
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- context-engineering
- eval
components:
- NVIDIA DOCA
- NVIDIA BlueField
- DOCA Flow
- DOCA GPUNetIO
- DOCA Comch
- SKILL.md
- NVIDIA Nemotron
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-applications-on-nvidia-bluefield-faster-with-nvidia-doca-agent-skills/
published_at: '2026-10-01'
---

## 概要

NVIDIAが、BlueField向けDOCA開発でAIエージェントに検証済みのAPI署名やハード要件、ビルド制約を渡すDOCAエージェントスキルをGitHubで公開した。65プロンプトの評価で、スキルなしではチェックリストの19%しか満たさなかったがスキルありでは100%を達成した。デモでは手書きコード量が73%、ハードウェアコマンドが46%減ったとしている。

## 設計のポイント

- SKILL.mdに実際のAPI署名やハード要件、ビルド制約を機械可読な仕様として置き、エージェントの推測を排除する。
- コード生成の前にデバイスのサポート有無を確認し、ファームウェア変更前にはプリフライトチェックを行わせる。
- スキルをDOCAコンポーネントや作業単位で分割し、必要なものだけをロードさせる。
- 必須回答のチェックリストを使った有無比較評価で効果を定量化する。

## 使いどころ

- DOCAでBlueField上のアプリを開発するチームが、API誤用による手戻りを減らしたいとき。
- ハード依存が強く学習データに乏しい領域でコーディングエージェントを使う開発者。
- 社内の専門SDKをエージェント向けのスキルとして提供する場合の参考。
