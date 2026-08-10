---
type: announcement
title: Claude Codeをセルフホスト環境で実行し、実行系を自社インフラに残す
title_original: Run Claude Code sessions on your own compute
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- reasoning-computation-separation
components:
- Claude Code
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
published_at: '2026-08-06'
---

## 概要

Claude Codeのセッションを自社インフラ上で実行できる「セルフホスト環境」がパブリックベータで公開された。Webやモバイル、ルーティンから開始したセッションが自社ネットワーク内の内部サービスやツールチェーンに直接アクセスしながら動作し、リポジトリのチェックアウトやビルド成果物、シークレットは自社が管理するインフラ上に留まる仕組み。

## 設計のポイント

- 長時間稼働のランナー（プロセス）がセッションを受け取ってClaude Codeプロセスを起動する構成で、固定台数のFixedモードと需要に応じて起動・停止するOn-demandモードを選べる
- 会話内容（プロンプト・応答・ツール結果）は推論のためAnthropicに送信される一方、リポジトリチェックアウトやビルド成果物・シークレットは顧客インフラ側に残り、実行系と推論系の責務を分離する
- 1つのランナーが複数セッションを処理できるが、セッションごとに独立したチェックアウトで分離し、開発者・アカウント間の作業が混ざらないようにする
- Web・モバイル・デスクトップ・ルーティンなどどの入口から始めたセッションも同じ環境にルーティングされるため、セットアップは一度で済む

## 使いどころ

- 内部データベースやレジストリなど、パブリックインターネットに晒したくない社内サービスにエージェントからアクセスさせたい企業
- コンパイラや社内CLIなど独自ツールチェーンを事前インストールした環境でエージェントを毎回ゼロから準備したくないチーム
- ソースコードやビルド成果物を自社管理インフラ内に留める必要があるコンプライアンス要件の厳しい組織
