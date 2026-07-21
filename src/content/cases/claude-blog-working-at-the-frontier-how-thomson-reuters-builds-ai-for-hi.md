---
type: case
title: Thomson Reuters、Claude Agent SDKで高リスク専門職向けAIエージェントを構築
title_original: 'Working at the frontier: How Thomson Reuters builds AI for high-stakes professional work'
company: Thomson Reuters
industry: other
cloud: []
patterns:
- ai-agent
- rag
- human-in-the-loop
- eval
components:
- Claude Agent SDK
- Claude Fable 5
- CoCounsel Legal
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work
published_at: '2026-07-08'
---

## 概要

Thomson ReutersはCoCounsel LegalをClaude Agent SDK上で再構築し、複数ツールを横断して計画・委任・実行する単一エージェントに刷新した。引用検証を組み込み、専門家によるレビューに耐える出力を担保しながら、従来数十時間かかっていたリサーチを数分に短縮した。

## 設計のポイント

- 検索・要約だけでなく引用の妥当性検証を専用の仕組みとして組み込み、提示前に出典を裏取りする
- 従来は逐次実行していた個別スキルをClaude Agent SDK上のエージェントに統合し、ツールと情報源をまたいだ計画・委任・実行をリアルタイムに行わせる
- モデル選定の基準を『専門家によるレビューに耐えるか』に置き、ベンチマークではなく実務での検証可能性を重視する
- 長い連鎖のツール呼び出しでも文脈を保持し続けられるかを評価基準に加え、専門家を意思決定の最終地点に据えるワークフローを維持する

## 使いどころ

- 法務・税務・会計など、出力の正確性と説明責任が強く求められる専門職向けAI
- 膨大な文献・判例調査を高速化しつつ人間の最終検証を必須にしたいナレッジワーク
- 複数の社内ツール・コンテンツソースを横断するエージェント型製品を設計するチーム
