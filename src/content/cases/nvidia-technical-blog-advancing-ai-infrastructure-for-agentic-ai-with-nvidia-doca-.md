---
type: announcement
title: NVIDIA BlueField DPUによるエージェントAI基盤のシリコン内蔵セキュリティ
title_original: Advancing AI Infrastructure for Agentic AI with NVIDIA DOCA In-Silicon Security
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- defense-in-depth
- confidential-computing
- guardrails
components:
- NVIDIA BlueField-4 DPU
- NVIDIA DOCA
- DOCA Argus
- DOCA Vault
- DOCA Flow
- NVIDIA Vera Rubin
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/
published_at: '2026-06-11'
---

## 概要

自律性の高いエージェントAIが新たな攻撃対象になる中、NVIDIA BlueField DPUとDOCAセキュリティスタックがホストとは独立した信頼実行ドメインでランタイム脅威検知・アクセス制御・ネットワークポリシー強制を行うシリコン内蔵セキュリティを解説。ホストが侵害されてもBlueField側の監視・ポリシー適用は継続し、ソフトウェアのみのエージェントレス手法比で最大1000倍高速な脅威検知と800Gb/sでのポリシー強制を実現する。

## 設計のポイント

- セキュリティ機能をホストと同じ信頼境界に置かず、DPU上の独立した信頼実行ドメインに分離することで、ホスト侵害時にもセキュリティポリシーの改ざん・迂回を防ぐ
- DOCA Argusがゼロコピーのダイレクトメモリアクセスでホストメモリのスナップショットを取得し、ホストCPUを消費せずランタイムの挙動を監視する
- DOCA Argus/Vault/Flowを役割分担させ、ランタイム脅威検知・ファイルアクセスのゼロトラスト化・高速ネットワークポリシー強制をそれぞれ専任させる

## 使いどころ

- 推論・学習・エージェント実行が同居するAIファクトリー全体を、ホスト資源を消費せずに保護したいインフラ運用者
- 自律性の高いエージェントに権限を持たせる中で、侵害時の被害範囲を限定したいセキュリティ担当者
