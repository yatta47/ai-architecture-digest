---
type: announcement
title: 開発者コンソールのプロンプト生成機能
title_original: Generate better prompts in the developer console
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
components:
- Anthropic Console
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/prompt-generator
published_at: '2024-05-20'
---

## 概要

Anthropic Console上でタスクを説明するだけで、Chain-of-Thoughtやロール設定などのベストプラクティスを反映した本番投入可能なプロンプトテンプレートを自動生成する機能を追加。プロンプトエンジニアリング初心者の立ち上がりを早め、熟練者の作業時間も削減する。

## 設計のポイント

- ロール設定(役割の付与)とChain-of-Thought用のスクラッチパッドをテンプレートに組み込み、推論の質を高める
- 変数部分をXMLタグで明示的に区切り、プロンプト構造を明確化する

## 使いどころ

- プロンプトエンジニアリングに不慣れなユーザーが高品質なプロンプトを素早く作りたい場合
- 熟練プロンプトエンジニアがベースラインとなるテンプレートを高速に用意したい場合
