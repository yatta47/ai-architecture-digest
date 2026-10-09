---
type: opinion
title: 生体医用画像AIの真のボトルネックはモデルでなくデータ基盤
title_original: Biomedical imaging's real bottleneck is the data, not the model
company: Databricks
industry: healthcare
cloud: []
patterns:
- fine-tuning
- data-federation
components:
- Databricks
- Unity Catalog
- PACS
- DICOM
- MONAI
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/biomedical-imagings-real-bottleneck-data-not-model
published_at: '2026-10-08'
---

## 概要

医用画像AIが成果を出せない原因は、PACSなどに分断され匿名化や他データとの連携が難しい画像データにあると論じる。画像を一元的に管理して検索可能にし、EHRやオミクス、治験データと結びつけるレイクハウスの基盤を提案する。

## 設計のポイント

- 画像のガバナンスを一箇所に集め、検索できる形にしてから学習に使う。
- DICOMヘッダやピクセルに含まれるPHIを大規模に匿名化する。
- 画像をEHR、オミクス、治験データと結び付けてバイオマーカーや患者層別に使う。
- 連合学習ではデータでなく重みだけを動かし、施設間のばらつきに対処する。

## 使いどころ

- 病院や製薬で画像データを研究に活用したいデータ基盤担当者。
- 複数施設で汎化する医療AIを作る医療機器メーカー。
