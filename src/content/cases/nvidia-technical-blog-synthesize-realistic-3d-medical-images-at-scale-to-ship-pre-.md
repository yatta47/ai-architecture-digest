---
type: announcement
title: MAISI基盤のオープンソース3D医療画像合成フレームワークNV-Generate-CTMR
title_original: Synthesize Realistic 3D Medical Images at Scale to Ship Pre-Trained Models
company: NVIDIA
industry: healthcare
cloud:
- on-prem
patterns:
- generative-data-synthesis
- fine-tuning
components:
- NV-Generate-CTMR
- NV-Generate-MR-Brain
- MAISI
- MAISI-v2
- Latent Rectified Flow
- MR-RATE dataset
- CT-RATE dataset
- NVIDIA RTX GPUs
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/synthesize-realistic-3d-medical-images-at-scale-to-ship-pre-trained-models/
published_at: '2026-06-11'
---

## 概要

NVIDIAはMAISI（Medical AI for Synthetic Imaging）を拡張し、CT・MRIの3D医療画像とセグメンテーションをスケールで合成できるオープンソースフレームワークNV-Generate-CTMR、および脳MRI特化のNV-Generate-MR-Brainを公開した。あわせて10万件の脳MRI検査からなる世界最大級のオープンMRIデータセットMR-RATEも公開し、データ不足・プライバシー制約・アノテーションコストによる3D医療画像AIのボトルネックを解消する狙いがある。可変ボクセルサイズ・全身対応を単一モデルで扱え、コード・重み・学習設定を含め再学習なしですぐ利用・微調整できる点が特徴。

## 設計のポイント

- MAISIの生成アーキテクチャ系列を土台に、Latent Rectified Flowを組み合わせて高速かつ高忠実度な3D生成を実現し、ゼロから作り直さない。
- 可変ボクセルサイズ・可変ボリューム次元・全身対応を単一モデルでサポートし、撮影プロトコルごとに別モデルを再学習する必要をなくす。
- コード・学習済み重み・学習設定・データセットをオープンライセンス（NVIDIA Open Model LicenseやCC-BY-NC）で公開し、RTX GPUでのロイヤリティフリー推論を可能にして導入・計算コストの障壁を下げる。
- 生成したボリュームにピクセル単位のセグメンテーションラベルを付与し、プライバシー保護型のデータ拡張やベンチマークに使えるようにする。

## 使いどころ

- 3D CT/MRIの学習データが少ない・偏っている・共有しにくい研究チームが、データ拡張として合成データを利用したい場合。
- モデル開発者が事前学習済みの生成モデルを自施設の解剖部位・スキャナー・モダリティに合わせて微調整したい場合。
- 実患者データを露出せずに、複数施設・複数スキャナー間でプライバシー保護型のデータ共有やベンチマークを行いたい場合。
