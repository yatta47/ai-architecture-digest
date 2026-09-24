---
type: announcement
title: 3D CT向けに放射線科医の思考連鎖を再現するオープンVLM「NV-Reason-CT」
title_original: Introducing NV-Reason-CT Open 3D CT VLM for Radiologist Chain-of-Thought Reasoning
company: NVIDIA
industry: healthcare
cloud: []
patterns:
- fine-tuning
- human-in-the-loop
components:
- NV-Reason-CT
- NV-Reason-CXR
- Qwen3.5-4B
- Primus 3D ViT
- Colipri
- 3D MRoPE
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning/
published_at: '2026-09-23'
---

## 概要

NVIDIAが、3D CTボリュームを直接扱う3D ViTエンコーダとQwen3.5-4Bを組み合わせたビジョン言語モデルNV-Reason-CTを公開した。構造化レポート生成、放射線科医の系統的読影を模した思考連鎖、複数ターンの追質問に対応し、CT-RATEベンチマークで Macro-F1 0.614 を達成、NIHの放射線科医が推論過程の妥当性を確認している。研究開発用の基盤で、臨床承認済み製品ではない。

## 設計のポイント

- CTを2Dスライスの束として扱わず、フル3D ViT（192³ボクセル、8x8x8パッチ）でスライス間の空間関係を保持する。
- 3Dトークンの格子座標を3D MRoPEでLLMに渡し、全層で空間的な相互関係を推論に利用する。
- 診断ラベルだけでなく、解剖領域を順に確認する思考連鎖と構造化レポートを学習させ、監査可能性と信頼性を高める。
- 30の胸部・29の腹部異常からなるCTオントロジーで生成と評価を導く。

## 使いどころ

- 特定のCT用途向けにポストトレーニングしたい医療AIの研究者・開発者。
- 推論過程を提示して放射線科医のレビューを支援するワークフローを設計するとき。
- セグメンテーションや合成データ生成モデルと組み合わせた医用画像パイプラインの基盤として。
