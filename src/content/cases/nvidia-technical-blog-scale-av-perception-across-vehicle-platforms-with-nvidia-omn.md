---
type: case
title: 3Dガウシアンスプラッティングで新型車向け認識モデルを合成データ適応
title_original: Scale AV Perception Across Vehicle Platforms with NVIDIA Omniverse NuRec
company: NVIDIA
industry: other
cloud: []
patterns:
- video-intelligence
- ai-agent
components:
- NVIDIA Omniverse NuRec
- NVIDIA Harmonizer
- Physical AI NuRec Dataset
- Hugging Face
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/scale-av-perception-across-vehicle-platforms-with-nvidia-omniverse-nurec/
published_at: '2026-08-28'
---

## 概要

NVIDIA Omniverse NuRecは、実車走行データを3Dガウシアンスプラッティングで再構成し、既存の走行シーンから未発売の新型車のセンサー配置に合わせた新規視点の映像をレンダリングする。再構成済みシーンとターゲットのセンサーリグをペアリングし、NVIDIA Harmonizerでフレームを時間的に一貫化した上で認識モデルを学習させることで、新しい車種に対する物体検出の精度・再現率がゼロショットのベースラインより向上したという社内実験結果を示している。

## 設計のポイント

- 実車データの再収集・再ラベリングをせず、既存の走行記録を3D再構成して視点変換することで新型車向けの学習データを合成する
- 再構成シーンは元のリグ軌跡・カメラキャリブレーション・物体トラック・地図データを保持し、新規視点でもラベルを再利用できるようにする
- レンダリング後のフレームをHarmonizerで後処理し、フレーム間の時間的一貫性を担保してから認識モデルの学習に投入する
- ダウンロード・レンダリング・後処理のワークフローをエージェントスキルとしてパッケージ化し、コーディングエージェントから一連の処理を呼び出せるようにする

## 使いどころ

- 新しい車種・センサー構成へ認識スタックを展開する際、実車データの収集前に性能を検証したい自動運転開発チーム
- レアケース（特定の遮蔽・照明条件など）を狙って合成データで補いたい場合
- 複数の車種バリアントに同じ認識ソフトウェアを横展開する際、各車種ごとのデータ収集コストを抑えたい場合
