---
type: guidance
title: 商取引エージェントの実践アーキテクチャガイド：サブエージェントではなくスキルで構成する
title_original: A guide to the anatomy of effective commerce agents
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- multi-agent-orchestration
- inference-optimization
components:
- Claude
- Agent SDK
- Claude Code
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/the-anatomy-of-effective-commerce-agents
published_at: '2026-09-02'
---

## 概要

Anthropicが小売・旅行・通信など複数業界の商取引エージェント構築で得た知見をまとめたガイド。ドメインごとにサブエージェントへ分割するのではなく、単一のエージェントループにスキルを持たせる構成の方が、状態喪失やハンドオフのコスト・レイテンシ増を避けられ品質・コスト・速度の面で優れると解説する。頻度に応じてシステムプロンプトとスキルのどちらに指示を置くかを決める指針や、レイテンシ・コスト最適化、本番運用でのメモリ・安全性・評価の設計も扱う。

## 設計のポイント

- 会話全体でカートや顧客履歴などの状態を共有し続けるため、ドメインごとのサブエージェントに分割せず単一エージェント+スキル構成にする
- 全ターンの3分の1以上で使われる指示はシステムプロンプトに置き、それ以外はロード時に1ターン消費するスキルに分離する
- 安全・法務ルールやブランド制約、アレルギーなど重要な顧客情報は頻度に関わらず必ずシステムプロンプトに含める
- サブエージェントは、深いリサーチのように専用コンテキストウィンドウが有効な自己完結タスクや、独自コンプライアンスを持つ別ドメインへのハンドオフに限定して使う

## 使いどころ

- 小売・旅行・通信など複数の意図が絡み合う会話型コマースエージェントを設計するエンジニアリングチーム
- サブエージェント方式と単一エージェント+スキル方式のどちらを採用すべきか判断に迷っているチーム
- システムプロンプトの肥大化とスキルロードのレイテンシのバランスを取りたいプロダクト開発チーム
- 本番運用でのメモリ管理・安全性・評価体制を組織横断で整備したいエンジニアリング組織
