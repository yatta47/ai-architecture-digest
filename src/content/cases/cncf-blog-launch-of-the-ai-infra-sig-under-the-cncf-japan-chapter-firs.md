---
type: announcement
title: CNCF Japan ChapterにAI Infra SIGが発足、第1回ミートアップ開催へ
title_original: Launch of the AI Infra SIG under the CNCF Japan Chapter — First Meetup and Call for Speakers
industry: cross-industry
cloud: []
patterns:
- ai-agent
- gpu-fleet-reliability
components:
- Kueue
- KServe
- llm-d
- AIBrix
- kgateway
- Envoy AI Gateway
- agentgateway
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/23/launch-of-the-ai-infra-sig-under-the-cncf-japan-chapter-first-meetup-and-call-for-speakers/
published_at: '2026-07-24'
---

## 概要

Cloud Native Community Japanが、LLM/AIエージェント向けクラウドネイティブ基盤の知見共有を目的にCNCF Japan Chapter傘下でAI Infra SIGを発足。2026年10月1日に第1回ミートアップを開催し、スケジューリングからエージェント基盤までの実践知を扱う予定。

## 設計のポイント

- 動的リソース割当(DRA)やワークロード対応スケジューリング、KServe/llm-d/AIBrixなどAIデプロイ基盤、kgateway/Envoy AI GatewayなどAIゲートウェイを議論領域として明示する
- PyTorch FoundationやAgentic AI Foundationなど他のLinux Foundation系コミュニティとも連携し、日本のプラクティショナーをグローバルなOSSエコシステムに接続する

## 使いどころ

- LLM/エージェントワークロード向けにKubernetes基盤を設計・運用するプラットフォームチーム
- AI基盤の運用ノウハウを国内外のコミュニティで共有・アップストリーム貢献したいエンジニア
