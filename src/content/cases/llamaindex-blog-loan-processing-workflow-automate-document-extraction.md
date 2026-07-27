---
type: guidance
title: LlamaParseで構築する住宅ローン審査書類の自動抽出・クロス検証パイプライン
title_original: 'Loan Processing Workflow: Automate Document Extraction'
industry: financial-services
cloud: []
patterns:
- document-processing
- human-in-the-loop
- ai-agent
- guardrails
components:
- LlamaParse
- LlamaCloud
- Pydantic
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/loan-processing-workflow-document-extraction
published_at: '2026-07-21'
---

## 概要

住宅ローン審査書類（W-2、銀行明細、確定申告書、鑑定書など150〜200ページ規模）はレイアウトが多様で、多くの金融機関では今も手作業でのデータ入力がボトルネックになっている。この記事はLlamaParseとLlamaCloudを使い、書類ごとにコスト効率重視/エージェント型の抽出モードを使い分けつつ、複数書類間のクロス検証やTRIDなどのコンプライアンスチェックまでを組み込んだ抽出パイプラインの構築方法を解説している。信頼度スコアに基づく人間確認の閾値も設け、リアルタイム審査ワークフローに統合する構成を示す。

## 設計のポイント

- 書類の構造の複雑さに応じてコスト効率モード（定型書類）とエージェントモード（多セクション・非定型書類）を使い分け、全件を高コストモードで処理するコストとの無駄を避ける
- 単一書類の抽出だけでなく、書類間（申告書の所得と銀行明細の入金額など）を突き合わせるクロスドキュメント検証を仕組み化する
- 抽出結果に信頼度スコアを付与し、一定閾値を下回った項目だけ人間確認に回すことで自動化率を上げつつ精度を担保する
- TRIDなど規制要件のチェックを抽出パイプラインの一部として自動化し、審査プロセスに組み込む

## 使いどころ

- 自営業者向けなど書類構成が複雑な住宅ローン・商業用不動産ローンを扱う金融機関の審査部門
- 多様なフォーマットのW-2・銀行明細・確定申告書からの手入力を減らしたいローンオフィサー
- 書類間の整合性チェックや規制対応（TRIDなど）を自動化したいコンプライアンス担当者
- 信頼度に応じた人間確認の運用を設計したいAI導入担当チーム
