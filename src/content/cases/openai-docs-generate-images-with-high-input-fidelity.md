---
type: guidance
title: input_fidelity=highで顔・ロゴを崩さず画像を部分編集する
title_original: Generate images with high input fidelity
industry: cross-industry
cloud: []
patterns:
- image-generation
components:
- Image API
- gpt-image-1
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/generate_images_with_high_input_fidelity/
published_at: '2025-07-17'
---

## 概要

OpenAIのクックブックは、Image API/Responses画像生成ツールのinput_fidelity=highパラメータを使い、顔やロゴなど崩れやすいディテールを保持したまま画像の一部だけを編集する手法を示す。マグカップの色替えのような局所編集、人物の顔を保った写真編集・アバター生成、複数人の顔を1枚に合成してからの編集、ブランドロゴの一貫性維持といった具体例を扱う。

## 設計のポイント

- input_fidelity=highを指定することで、背景や無関係な領域を変えずに指定箇所だけを編集できる。
- 複数人の顔を編集に使う場合は、個別に投げるのではなく1枚の合成画像にまとめてから渡すことで、全員の顔の再現度を高める。
- ロゴや商品デザインなどブランド資産を含む画像編集では、high fidelityによって元のブランド要素の同一性を保つ。

## 使いどころ

- 人物写真の背景だけを変えるなど、顔を保ったまま部分編集したいプロダクト機能。
- ロゴや商品パッケージの一貫性を保ちながらマーケティング画像をバリエーション生成したい場合。
