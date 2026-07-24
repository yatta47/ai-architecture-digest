---
type: announcement
title: Anthropic APIのトークン効率化：キャッシュ対応レート制限とツール呼び出し最適化
title_original: Token-saving updates on the Anthropic API
company: Cognition
industry: other
cloud:
- aws
- gcp
patterns:
- llmops
- cost-optimization
- inference-optimization
components:
- Claude 3.7 Sonnet
- Anthropic API
- Amazon Bedrock
- Google Cloud Vertex AI
- text_editor tool
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/token-saving-updates
published_at: '2025-03-13'
---

## 概要

Anthropic APIにキャッシュ読み取りトークンをレート制限対象外にする「キャッシュ対応レート制限」、キャッシュ管理を自動化する仕組み、出力トークンを最大70%削減する「トークン効率的なツール利用」、ドキュメント編集用のtext_editorツールが追加された。AIコーディングエージェントDevinを開発するCognitionが早期採用事例として紹介されている。

## 設計のポイント

- プロンプトキャッシュの読み取りトークンをInput Tokens Per Minute制限から除外し、既存レート制限内でスループットを最大化する
- キャッシュブレークポイント設定時に最長の一致プレフィックスを自動選択させ、開発者がキャッシュ区間を手動管理する負担を無くす
- ベータヘッダー付与のみでツール呼び出しを出力トークン効率化し、最小限のコード変更で導入できるようにする
- 文書全体でなく差分編集を行うtext_editorツールにより、大規模ドキュメントやコードベースへの編集コストを抑える

## 使いどころ

- 大規模なナレッジベースをコンテキストに保持し続ける必要があるドキュメント分析プラットフォーム
- 巨大なコードベースを参照しながら支援するコーディングアシスタント
- 詳細な製品ドキュメントを踏まえて回答するカスタマーサポートシステム
