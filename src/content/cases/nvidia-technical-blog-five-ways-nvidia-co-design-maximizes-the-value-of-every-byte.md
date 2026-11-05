---
type: guidance
title: HBMの1バイトあたりの仕事量を高めるAI工場のコデザイン5手法
title_original: Five Ways NVIDIA Co-Design Maximizes the Value of Every Byte in the AI Factory
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- cost-optimization
components:
- NVFP4
- TensorRT-LLM
- NVIDIA Dynamo
- NIXL
- NVIDIA Vera CPU
- NVIDIA CMX
- BlueField-4 STX
- Vera Rubin NVL72
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/five-ways-nvidia-co-design-maximizes-the-value-of-every-byte-in-the-ai-factory/
published_at: '2026-11-05'
---

## 概要

NVIDIAが、HBM容量が同じ288GBでもVera Rubin NVL72がGB300 NVL72の最大30倍のメガワット当たりスループットを出せる理由を、5つの協調設計で説明した記事。4bit量子化、MoEのワイドエキスパート並列、KVキャッシュの階層化と共有などで、メモリ1バイトの有効活用度を高める。

## 設計のポイント

- NVFP4で重みを約3.5倍（対FP16）小さくし、空いたHBMをKVキャッシュ・バッチ・並行度に回す。
- MoEのエキスパートを8GPU以上に分散し、GPUごとの重み占有を減らして演算強度を上げる。
- KVキャッシュをフリート全体の資源として扱い、KV対応ルーティング・分離サービング・GPU/CPU/ストレージの階層化で再利用する。
- ツール呼び出し中の待機セッションのKVをCPUメモリへ退避して、HBMを他の生成に使う。

## 使いどころ

- 長コンテキストのエージェント推論を大規模に運用する基盤担当
- 電力あたりのトークン生成量を重視するAI基盤の設計者
