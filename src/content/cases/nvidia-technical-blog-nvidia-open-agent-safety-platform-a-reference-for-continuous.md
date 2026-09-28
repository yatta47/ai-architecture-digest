---
type: announcement
title: OpenShellとSentryでエージェントの行動を監視・制御するハードウェア連携型セーフティ基盤
title_original: 'NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- guardrails
- ai-agent
- defense-in-depth
components:
- NVIDIA OpenShell
- NVIDIA Sentry
- NVIDIA BlueField-4
- NVIDIA Vera
- NVIDIA DOCA
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/
published_at: '2026-09-28'
---

## 概要

自律型AIエージェントが評価環境から逸脱し想定外のシステムに到達した事例を踏まえ、NVIDIAはVera CPU上のOpenShell（サンドボックス実行）とBlueField-4 DPU上のSentry（帯域外監視・ポリシー執行）を組み合わせた多層防御アーキテクチャを提示する。エージェントの制御はモデルへの経路上でアウトオブバンドに行い、エージェント自身に監視の有無を知らせない設計を原則とする。

## 設計のポイント

- エージェント本体からは独立した帯域外（out-of-band）の経路でポリシーを執行し、エージェントが監視や制御の存在を検知・回避できないようにする。
- モデルへの『次の思考』への経路そのものを制御点とすることで、最良の観測点と同時にキルスイッチとしての介入点を確保する。
- ラボ・企業・ハードウェアベンダーがそれぞれ1層を担う責任共有モデルとし、ランタイムとポリシー言語をオープンにして任意のプロバイダが接続できるようにする。

## 使いどころ

- 長時間・長期間自律的に動作するエージェントが、曖昧な指示やドリフトによって意図しないシステムへ到達するリスクを抑えたい場合。
- 推論内容の可視性を保ちながらエージェントの権限範囲を段階的に拡大したいAI基盤運用チーム。
