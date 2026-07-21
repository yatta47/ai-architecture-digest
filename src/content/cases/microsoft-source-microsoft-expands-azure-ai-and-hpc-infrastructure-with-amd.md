---
type: case
title: OpenAIがユーザーフィードバックをプロダクト改善に変える仕組み
title_original: How OpenAI uses human feedback to evaluate and improve LLMs
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- human-in-the-loop
- ai-agent
components:
- Codex
- MCP
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/blog/2026/07/20/microsoft-expands-azure-ai-and-hpc-infrastructure-with-amd/
published_at: '2026-07-20'
---

## 概要

OpenAIは、明示的・暗示的なフィードバックを来歴(provenance)付きの共有イベントストアに集約し、階層的なタクソノミーと埋め込みベースのk近傍クラスタリングで未知の障害パターンも検出する仕組みを構築した。会話内の訂正発言をLLMで抽出することで実用的なフィードバック量を2〜3倍に増やし、MCP/スキル経由でCodexなどのエージェントがフィードバックを調査・PR作成まで自動化できるようにしている。

## 設計のポイント

- Google SheetsやAirtableなど散在していたフィードバックを、生テキストと出所(ソース・会話ID・トレースID)を保持した単一のイベントスキーマに統一する。
- ユーザーが会話中に発する訂正(「いや、違う、XYZだから」)をLLMで抽出し、能動的な報告をしないユーザーからも実用的なシグナルを回収する。
- そのLLM抽出器自体を本番評価器として扱い、モデル・プロンプトのバージョン管理、カテゴリごとの精度、棄却(abstention)ポリシーを整備する。
- MCP経由でCodexにフィードバックストアを検索させ、スクリーンショット1枚から再現条件・関連ログ・原因コードまで遡ってPRを自動生成させる。

## 使いどころ

- Slack・サポートチケット・SNS・レーティングなど複数チャネルに散在するユーザーフィードバックを統合したいプロダクトチーム。
- バグ報告からPR作成までのエンジニアリングループをエージェントで自動化したい開発組織。
