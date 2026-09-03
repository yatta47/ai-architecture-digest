---
type: announcement
title: ページ並列処理でレイテンシを抑えたLlamaParseの高速抽出ティア「Turbo」
title_original: Introducing Turbo, our fastest extraction tier
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- inference-optimization
- ai-agent
components:
- LlamaParse
- ExtractBench
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-turbo-our-fastest-extraction-tier
published_at: '2026-09-03'
---

## 概要

LlamaIndexが、ドキュメント抽出を高速化する新ティア「Turbo」をベータ公開。個別のパース処理を省いてページを並列処理することで、中〜長尺文書では1ページあたり約0.5秒まで高速化し、レスポンスパスに抽出処理が組み込まれるエージェントのループを高速化する用途を想定している。

## 設計のポイント

- 独立したパース工程を廃し文書ページから直接抽出することでレイテンシを削減する
- ページ単位の並列処理により文書が長くなってもレイテンシがほぼ増加しない設計にする
- リアルタイム性が必要なTurbo、コスト重視のCost Effective、精度重視のAgentic/Agentic Plusをワークロード特性で使い分けられるようにする

## 使いどころ

- フォーム入力のオートフィルなどユーザーが待っている場面でのリアルタイム抽出
- 契約書や請求書を読んでから次のツール呼び出しに進むエージェントの応答待ち時間短縮
- メール添付のPOなど高頻度で流れ込む書類から即座に構造化データを取り出す業務
