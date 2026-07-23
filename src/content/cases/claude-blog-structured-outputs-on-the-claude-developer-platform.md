---
type: announcement
title: Claude開発者プラットフォームのJSON/ツール出力をスキーマ準拠で保証する構造化出力
title_original: Structured outputs on the Claude Developer Platform
industry: cross-industry
cloud:
- aws
- azure
patterns:
- guardrails
- multi-agent-orchestration
- document-processing
- llmops
components:
- Claude Developer Platform
- Amazon Bedrock
- Microsoft Foundry
outcome:
  type: reliability
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/structured-outputs-on-the-claude-developer-platform
published_at: '2025-11-14'
---

## 概要

Claude Developer Platformに構造化出力機能が追加され、APIレスポンスが指定したJSONスキーマやツール定義に必ず一致するようになった。データ抽出やマルチエージェント間通信、複雑な検索ツールなど、フォーマットの正確性が重要な場面での信頼性向上を狙う。Sonnet 4.5・Opus 4.5・Haiku 4.5で提供され、Amazon BedrockやMicrosoft Foundryでも利用可能。

## 設計のポイント

- JSONモードとツールモードの2通りの適用方法を用意し、用途に応じて出力保証の方式を選べるようにしている
- スキーマ準拠を保証することでパースエラーや失敗したツール呼び出しを構造的に排除する設計とした
- モデル性能への影響なしに出力形式を保証することで、リトライやフェイルオーバーロジックを不要にしアプリケーションコードを簡素化できる

## 使いどころ

- 下流システムが一貫した誤りのないフォーマットに依存するデータ抽出パイプライン
- エージェント間の一貫した通信フォーマットが安定動作の鍵となるマルチエージェントアーキテクチャ
- 複数の検索フィールドを特定のパターンに沿って正確に埋める必要がある複雑な検索ツールの実装
