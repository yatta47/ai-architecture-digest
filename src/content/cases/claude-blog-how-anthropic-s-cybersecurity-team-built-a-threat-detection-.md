---
type: case
title: Anthropic社内セキュリティチームのClaude活用脅威検知基盤『CLUE』
title_original: How Anthropic's cybersecurity team built a threat detection platform with Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- text-to-sql
- context-engineering
components:
- Claude Code
- CLUE (Claude Looks Up Evidence)
- Slack
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropic-uses-claude-cybersecurity
published_at: '2026-05-12'
---

## 概要

Anthropicの検知プラットフォームエンジニアリングチームは、Claude Codeとの協働でCLUE(Claude Looks Up Evidence)という自然言語インターフェースの脅威検知・対応プラットフォームを構築した。CLUEはSlackや社内ドキュメント、コードリポジトリ、データウェアハウスから文脈情報を取り込んでアラートを事前トリアージし、オーケストレーターと並列サブエージェントが自然言語からSQLクエリを実行して調査を数時間から3〜4分に短縮する。

## 設計のポイント

- アラート受信時にSlackの会話や社内ドキュメント、コードリポジトリなど社内システム横断のコンテキストで自動エンリッチし、確信度スコア付きで偽陽性/真陽性/悪意/想定内の挙動に分類する。
- オーケストレーターが複数のサブエージェントへ自然言語クエリの実行を並列委任し、結果を統合して調査サマリーを合成するエージェンティックループを採用する。
- Claude Code自体を設計パートナーとして活用し、プロトタイプを1日、設計文書と実装を1週間で完成させて開発サイクルを圧縮した。

## 使いどころ

- 大量のセキュリティアラートに追われ、ツールごとに異なるクエリ言語へのコンテキストスイッチで消耗しているSOC/セキュリティアナリストチーム。
- 契約社員や外部関係者のドキュメントアクセスを横断調査するデータガバナンス・コンプライアンスレビュー担当。
- 複数の断片化されたログ基盤を横断した根本原因調査を高速化したい検知エンジニアリングチーム。
