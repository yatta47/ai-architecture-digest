---
type: case
title: 推論サービング基盤の変更をライブサーバ検証まで含めて評価するSWE-Serveベンチマーク
title_original: How SWE-Serve Exposes the Gap Between Local Tests and Live Serving
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- eval
- inference-optimization
- ai-agent
components:
- SWE-Serve
- SGLang
- mini-swe-agent
- NVIDIA Nemotron
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-swe-serve-exposes-the-gap-between-local-tests-and-live-serving/
published_at: '2026-09-23'
---

## 概要

NVIDIAはSGLangのマージ済みPR83件から53件の実行可能タスクを作り、AIコーディングエージェントが推論サービング基盤を正しく変更できるかを評価するSWE-Serveを公開した。ライブサーバを起動する19タスクでは、ライブ検証を除くと69.4%通るパッチが完全検証では45.9%に下がり、ローカルテストだけでは不十分と示した。

## 設計のポイント

- 実モデルをロードしサーバを立てて公開インターフェース経由で結果を確認する検証を含め、テスト通過と実サービング正しさのギャップを測っている。
- 各タスクで未修正リポジトリが新規テストに失敗し回帰は通ること、参照パッチが全検証を通ることを宣言済みハードウェア上で確認している。
- 評価中はWebアクセスを遮断し、上流の解答の取得による汚染を防いでいる。

## 使いどころ

- 推論エンジンやLLMサービング基盤の変更をエージェントに任せたいチーム。
- コーディングエージェントを評価するベンチマークの設計者。
- 複数ランタイム領域にまたがる変更の自動化リスクを見積もりたい基盤エンジニア。
