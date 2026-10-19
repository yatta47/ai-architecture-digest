---
type: guidance
title: vLLMの分離推論でKV転送をプッシュ型にしてTTFTを短縮する
title_original: Push-based KV transfer to improve TTFT and TPOT for disaggregated inference in vLLM
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
components:
- vLLM
- NVIDIA NIXL
- AWS EFA
- Amazon EC2 P5en
- AWS Trainium
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/push-based-kv-transfer-to-improve-ttft-and-tpot-for-disaggregated-inference-in-vllm/
published_at: '2026-10-19'
---

## 概要

vLLMのprefill/decode分離構成では、KVキャッシュ転送の調整が最初のトークンまでの経路に入ってしまう。プッシュ型のNIXLコネクタで転送準備をクリティカルパスから外し、P5en上のQwen3-32BでTTFTを最大3倍、TPOTを最大30%改善した。

## 設計のポイント

- 従来のpull方式ではルーター中継、デコード側の確保、NIXL READが直列に並ぶため、これらを事前に済ませる。
- Trainiumクラスタで構築・検証した機能を、アクセラレータ非依存の機能としてvLLMへ還元している。
- EFAのRDMAでGPUやTrainiumのメモリ間を直接転送し、ホストメモリを経由しない。
- 効果は高リクエスト率で大きく、ワークロードと構成に依存する。

## 使いどころ

- 高負荷のLLMサービングでTTFTを下げたいプラットフォームチーム。
- prefillとdecodeを別ノードで運用している推論基盤。
- EFA対応のAWSインスタンスでvLLMを動かす場面。
