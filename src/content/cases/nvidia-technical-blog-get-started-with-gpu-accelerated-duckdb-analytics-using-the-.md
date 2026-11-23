---
type: guidance
title: DuckDBをGPUで高速化するSirius拡張の導入ガイド
title_original: Get Started with GPU-Accelerated DuckDB Analytics Using the Sirius Core Extension
ai_relevant: false
company: NVIDIA
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/get-started-with-gpu-accelerated-duckdb-analytics-using-the-sirius-core-extension/
published_at: '2026-11-23'
---

## 概要

NVIDIAとDuckLabsがDuckDBのコア拡張としてGPUネイティブSQLエンジンSiriusを公開した。INSTALL siriusとLOAD siriusの2コマンドで、SQLやスキーマを変えずに対応する分析クエリをNVIDIA GPUで実行でき、非対応機能はCPUへフォールバックする。TPC-Hで最大10TBまで3.25〜5.50倍の高速化と最大79%のクエリ時間コスト削減を示した。
