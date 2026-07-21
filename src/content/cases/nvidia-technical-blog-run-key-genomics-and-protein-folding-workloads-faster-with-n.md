---
type: case
title: RTX PRO 4500 Blackwellでゲノム解析とタンパク質構造予測を高速化
title_original: Run Key Genomics and Protein Folding Workloads Faster with NVIDIA RTX PRO 4500 Blackwell
company: Pacific Biosciences (PacBio)
industry: healthcare
cloud: []
patterns:
- inference-optimization
- cost-optimization
components:
- NVIDIA BioNeMo
- NVIDIA Parabricks
- RTX PRO 4500 Blackwell Server Edition
- Minimap2
- fq2bam
- DeepVariant
- Openfold3
- NVIDIA L4 Tensor Core GPU
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-key-genomics-and-protein-folding-workloads-faster-with-nvidia-rtx-pro-4500-blackwell/
published_at: '2026-06-11'
---

## 概要

NVIDIAのBioNeMoプラットフォーム（Parabricksと新GPU RTX PRO 4500 Blackwell Server Edition）は、ゲノム解析のアライメントやバリアントコールを従来のCPU処理で数時間かかっていたものを数分に短縮する。Minimap2・fq2bam・DeepVariantは旧世代GPU（L4）比で約2倍、AI駆動のタンパク質構造予測Openfold3は最大2.4倍高速化し、シーケンシング企業PacBioはベースコーリングのスループットが2倍以上向上したと報告している。

## 設計のポイント

- Minimap2・BWA-MEM（fq2bam）・DeepVariantなど信頼された既存オープンソースツールをゼロから作り直さずGPUアクセラレータ版として提供し、既存パイプラインとの互換性を保つ。
- 省電力・コンパクトなサーバー向けGPU（RTX PRO 4500 Blackwell Server Edition）を選定し、データセンターからエッジまで同一アーキテクチャで展開できるようにする。
- 古典的なバイオインフォマティクス処理（配列アライメント）とAI駆動の新手法（Openfold3によるタンパク質構造予測）を同じGPU基盤上で組み合わせ、ゲノムから治療法探索までの一連の流れを高速化する。
- 旧世代GPU（L4）との比較ベンチマークと実顧客（PacBio）の実測値の両方で性能改善を裏付ける。

## 使いどころ

- 腫瘍学やNICUなど、一分一秒が診断・治療判断を左右する時間制約の厳しい臨床現場でのバリアントコール高速化。
- シーケンシング企業がベースコーリングのスループットを高めつつ、設置面積や消費電力を抑えたい場合。
- 創薬チームがOpenfold3などのAIによるタンパク質構造予測を高速化し、治療候補のハイスループットスクリーニングを行いたい場合。
