---
type: announcement
title: 大規模GPUフリートをリアルタイム可視化・健全性監視するNVIDIA Fleet Intelligence
title_original: Introducing NVIDIA Fleet Intelligence for Real-Time GPU Fleet Visibility and Optimization
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
- multi-cloud
patterns:
- gpu-fleet-reliability
- confidential-computing
components:
- NVIDIA Fleet Intelligence
- NVIDIA DCGM
- GPUd
- NVIDIA Attestation SDK
- NVIDIA NGC
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/introducing-nvidia-fleet-intelligence-for-real-time-gpu-fleet-visibility-and-optimization/
published_at: '2026-06-11'
---

## 概要

大規模GPUフリートの運用では、異種ハードウェアや逼迫した電力枠、マルチテナントの負荷変動により、単一のホットスポットや設定ミスがSLA違反やコスト浪費に波及しうる。NVIDIA Fleet Intelligenceは、電力・温度・性能・健全性（ECC/XIDエラー等）・構成の一様性を低フットプリントなホストエージェントで継続監視し、GPUdやDCGM、Attestation SDKを活用した暗号学的な完全性検証まで含めて可視化するデプロイメント非依存のマネージドサービスとして正式提供が始まった。

## 設計のポイント

- 低フットプリントのホストエージェントがGPUテレメトリをフルマネージドのクラウドサービスへストリーミングし、電力・温度・性能・健全性・構成一様性を横断的に可視化する。
- エージェントは読み取り専用でホスト設定を変更せず、テレメトリ収集のみに限定することで安全に大規模展開できる設計とする。
- GPUd・DCGM・Attestation SDKなど既存のNVIDIA OSSを組み合わせ、RAS信号の解析からファームウェア/BIOSの整合性検証まで一貫して提供する。
- スケジューラやソフトウェアスタックに依存しないデプロイメント非依存設計により、異種混在・マルチクラウドのフリートにも対応する。

## 使いどころ

- 数万〜数十万GPU規模のフリートを運用し、ホットスポットや設定ドリフトを早期検知したいデータセンター/クラウドインフラチーム。
- NVIDIA Cloud Partner（NCP）など大規模GPUフリートのSLA遵守と稼働率向上を図りたい事業者。
- GPUのファームウェア・ドライバの真正性を暗号学的に検証し、コンプライアンス要件を満たしたいセキュリティ担当者。
