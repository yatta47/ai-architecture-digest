---
type: case
title: Coinbase Walletのエージェントファースト製品開発ライフサイクル
title_original: How Coinbase Wallet built an agent-first product development lifecycle
company: Coinbase
industry: financial-services
cloud: []
patterns:
- ai-agent
- spec-driven-development
- ci-cd
- human-in-the-loop
components:
- Arize AX
- Slack
outcome:
  type: speed
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-coinbase-wallet-built-an-agent-first-product-development-lifecycle/
published_at: '2026-09-02'
---

## 概要

Coinbase Walletは開発を一時停止しIDEを捨てる実験を経て、Slackからの依頼を実装・レビュー・検証まで運ぶ社内エージェントハーネス(Forge・Sail・Tracer Bullet)を構築した。結果として簡単な修正が20〜25日から1.8日、セキュリティレビューが3日から5分に短縮され、intentから本番投入までの時間を北極星指標として計測する運用に移行した。

## 設計のポイント

- 「plan, don't prompt」を原則とし、意図・制約・受け入れ基準・必要な証跡までを含む計画を契約として定義し、失敗時はコードでなく計画を修正して再実行する
- Forge(実装とPR/ビルド生成)、Sail(セキュリティレビューとリスク判定)、Tracer Bullet(仕様との整合検証)に役割を分担したエージェント群で計画から内部リリースまでをつなぐ
- モバイルシミュレータ群でビフォー/アフターの挙動を記録し仕様と自動照合する評価駆動開発により、生成コードを検証済みの成果物として扱う
- 送金など影響の大きい変更には人間レビューを必須とし、低リスクな変更のみエージェントレビュー評議会に委ねることでレビューリソースを重要箇所に集中させる

## 使いどころ

- コーディングエージェント導入後にPRレビューやCI・ビルド環境がボトルネックになっている開発組織
- 規制環境下で自動化とコンプライアンス上必須の人間承認のバランスを取る必要がある金融プロダクトチーム
- スプリントやPRD、デザインハンドオフといった従来の開発儀式そのものを見直したいプロダクトエンジニアリング組織
