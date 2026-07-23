---
type: guidance
title: gpt-oss-20bを多言語で思考連鎖(CoT)推論させるLoRAファインチューニング手法
title_original: Fine-tuning with gpt-oss and Hugging Face Transformers
industry: cross-industry
cloud: []
patterns:
- fine-tuning
components:
- gpt-oss-20b
- Hugging Face Transformers
- TRL
- LoRA
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/articles/gpt-oss/fine-tune-transfomers/
published_at: '2025-08-05'
---

## 概要

推論モデルは質問の言語に関わらず英語で思考連鎖(CoT)を生成しがちという課題に対し、gpt-oss-20bのシステムプロンプトに『推論言語』オプションを追加し、Hugging Face TRLライブラリで多言語推論データセットを使ったLoRAファインチューニングを行う手法を解説する。

## 設計のポイント

- システムプロンプトに新しい『推論言語』オプションを追加し、モデルに明示的に思考連鎖の言語を指定させる
- メモリ効率の良いLoRAを用いることで、大規模な計算資源なしにgpt-oss-20bのファインチューニングを行えるようにする
- 質問言語・思考連鎖言語・最終回答言語を独立に混在させられる柔軟性を持たせる

## 使いどころ

- 英語以外の言語で説明可能な思考連鎖を提供したい多言語プロダクトの開発者
- オープンウェイトモデルを自社データでファインチューニングしたいML実装者
