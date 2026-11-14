---
type: guidance
title: Jetson AGX OrinのDLA推論をPythonのcuDLAバインディングで回す手引き
title_original: Run Native DLA Inference in Python on NVIDIA Jetson AGX Orin Using cuDLA
company: NVIDIA
industry: manufacturing
cloud:
- on-prem
patterns:
- inference-optimization
components:
- NVIDIA Jetson AGX Orin
- cuDLA
- cuda.bindings
- TensorRT
- JetPack
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-native-dla-inference-in-python-on-nvidia-jetson-agx-orin-using-cudla/
published_at: '2026-11-14'
---

## 概要

Jetson AGX OrinのDLAでの推論をPython（cuda.bindings.cudla）から直接扱う手順の解説。TensorRTのtrtexecで作ったスタンドアロンloadableを読み込み、CUDAストリームでGPU前後処理とDLA推論を連携させる9ステップを示す。

## 設計のポイント

- trtexecで一度だけスタンドアロンloadableをビルドし、実行時はTensorRT不要でlibcudla.soのみで動かす。
- ハイブリッドモードでCUDAストリームにより、GPUの前後処理とDLA推論を1つのPythonアプリ内で連携させる。
- DLA非対応レイヤーはONNX側で事前に切り出す前提で、固定機能アクセラレータに合わせたモデル分割を行う。

## 使いどころ

- 電力・計算予算が限られたエッジで複数モデルを動かし、GPUを他処理に空けたいロボティクス用途。
- C++を書かずにPythonでDLAの実行管理をしたい開発者。
