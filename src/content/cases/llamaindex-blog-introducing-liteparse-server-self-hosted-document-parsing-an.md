---
type: announcement
title: キャッシュ・レート制限・分散トレーシングを備えたセルフホスト型LiteParse-Server
title_original: 'Introducing LiteParse Server: Self-Hosted Document Parsing'
industry: cross-industry
cloud:
- on-prem
patterns:
- document-processing
components:
- LiteParse
- Redis
- OpenTelemetry
- Prometheus
- Grafana
- Jaeger
- LibreOffice
- ImageMagick
- Tesseract.js
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/liteparse-server-self-hostable-document-parsing
published_at: '2026-07-18'
---

## 概要

クラウドOCR APIはレイテンシ・従量課金・プライバシー懸念という制約を持つため、LlamaIndexはLiteParseをHTTP API化したliteparse-serverを公開した。/parseと/screenshotsの2エンドポイントに加え、Redisによるコンテンツハッシュベースのキャッシュとレート制限、OpenTelemetry/Prometheus/Grafanaによる本番運用向けの可観測性をフルスタック構成として提供する。

## 設計のポイント

- ファイル内容とconfigのSHA-256ハッシュでパース結果をキャッシュし、同一文書の再パースを避ける
- IPベースのレート制限をサーバー層で強制し、パース処理前に過剰リクエストを弾く
- リクエストごとにファイル名・サイズ・MIMEタイプなどのスパン属性を持つ分散トレースを発行し、障害切り分けを容易にする

## 使いどころ

- プライバシー要件や従量課金コストを理由にクラウドOCR APIを避けたい組織
- 複数サービスから共有される社内ドキュメント解析基盤として運用したいチーム
