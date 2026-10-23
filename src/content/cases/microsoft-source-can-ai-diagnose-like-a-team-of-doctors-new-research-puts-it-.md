---
type: case
title: 診断の議論を行う仮想医師パネル型AI「MAI-DxO」と逐次診断ベンチマーク
title_original: Building Medical Superintelligence
company: Microsoft
industry: healthcare
cloud: []
patterns:
- multi-agent-orchestration
- eval
- reasoning-computation-separation
components:
- MAI-DxO
- SDBench
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://microsoft.ai/news/building-medical-superintelligence/
published_at: '2026-10-23'
---

## 概要

MicrosoftはMAI-DxOを、複数の仮想医師が診断案・検査選択・反論を数ラウンドで行うオーケストレーターとして構築した。逐次診断ベンチマークSDBenchで、救急症例では医師の1.7倍の精度、複雑症例では2倍以上の精度を、1/2〜1/3のコストで達成したと報告している。

## 設計のポイント

- 単一モデルの即答でなく、複数の役割が議論して診断を更新するパネル型オーケストレーションにしている。
- 試験形式でなく、情報を段階的に要求させるSDBenchで、正答だけでなく検査コストと経路も評価する。
- 精度とコストを同時に評価指標とし、不要な検査を減らす方向に最適化している。

## 使いどころ

- 段階的な意思決定が必要な医療・高度専門領域のAI評価設計。
- 複数エージェントの議論でコスト対精度を改善したい設計者。
