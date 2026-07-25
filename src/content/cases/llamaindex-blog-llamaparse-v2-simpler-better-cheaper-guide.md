---
type: announcement
title: 文書解析サービスをティア制に単純化し大幅値下げしたLlamaParse v2
title_original: 'Introducing LlamaParse v2: Simpler, Better, Cheaper'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- cost-optimization
- llmops
components:
- LlamaParse
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llamaparse-v2-simpler-better-cheaper
published_at: '2026-07-19'
---

## 概要

LlamaIndexが文書解析サービスLlamaParseをv2に刷新し、複雑な設定パラメータの代わりにFast/Cost Effective/Agentic/Agentic Plusの4段階ティア制を導入した。精度向上とともにAgentic Plusティアで50%の値下げを実施し、日付指定によるバージョン固定機能で本番運用の安定性も確保している。

## 設計のポイント

- 内部パラメータのチューニングではなく「必要な性能レベル」を選ぶティア制に変換し、意思決定コストを下げる
- 裏側で複数のモデルプロバイダに自動ルーティングしつつ、ユーザーには単純なティア選択のみを見せる
- YYYY-MM-DD形式のバージョン固定機能で、モデル更新による本番挙動の予期せぬ変化を防ぐ

## 使いどころ

- パース設定の専門知識がなくても高品質な文書取り込みパイプラインを組みたい開発者
- 本番運用中に解析結果が意図せず変わることを避けたいチーム
- コストを抑えつつ複雑なレイアウトやマルチモーダル文書を扱いたいプロダクト
