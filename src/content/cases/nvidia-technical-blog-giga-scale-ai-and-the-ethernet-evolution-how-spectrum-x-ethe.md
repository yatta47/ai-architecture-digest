---
type: announcement
title: AI学習クラスタ向けEthernetファブリックSpectrum-Xがもたらす低レイテンシ・マルチテナント分離
title_original: 'Giga-Scale AI and the Ethernet Evolution: How Spectrum-X Ethernet Rewrites the Rules'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- ai-training-networking
components:
- NVIDIA Spectrum-X Ethernet
- SuperNIC
- RoCEv2
- DCQCN
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/giga-scale-ai-ethernet-evolution-spectrum-x-ethernet-rewrites-rules/
published_at: '2026-08-24'
---

## 概要

NVIDIAは、GPU数十万台規模のAI学習クラスタ向けに、ハードウェアアクセラレートされた適応ルーティング・輻輳制御・NIC側ロードバランシングを実装した「Spectrum-X Ethernet」を解説する。従来のECMPベースEthernetは低エントロピーで巨大な同期フローを扱えずAll-Reduceが遅延するのに対し、Spectrum-Xはプレーン単位で輻輳を隔離しDeepSeek-V3学習シミュレーションでノイズ下でもステップタイムをほぼ劣化させなかった(668ms対1.18秒)。

## 設計のポイント

- スイッチ内のper-packet適応ルーティング・エンドポイント輻輳制御・NIC側プレーンロードバランシングという3つの独立した制御ループに責務を分離し、干渉によるファブリック不安定化を避ける
- マイクロ秒未満で反応するハードウェアアクセラレーションを前提に設計し、ソフトウェア制御では間に合わないAI学習の同期バーストに対応する
- プレーン単位でトラフィックを分離することで、あるテナントのノイズが他テナントのAll-to-All帯域を80%以上劣化させる問題を防ぐ

## 使いどころ

- 数万〜数十万GPU規模の分散学習クラスタでAll-Reduce/All-Gatherのストラグラー遅延を減らしたい場合
- マルチテナントのAI学習/推論基盤でノイジーネイバー問題を回避したい場合
