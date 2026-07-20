---
type: case
title: TradeshiftのレガシーBIからAmazon Quickエージェント型分析基盤への刷新
title_original: Evolving from legacy BI to agentic AI at Tradeshift with Amazon Quick
company: Tradeshift
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- business-intelligence-resilience
- multi-tenant-analytics
- text-to-sql
components:
- Amazon Quick
- Amazon QuickSight
- Amazon Quick Flows
- Amazon Quick Research
- Okta
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/evolving-from-legacy-bi-to-agentic-ai-at-tradeshift-with-amazon-quick/
published_at: '2026-07-20'
---

## 概要

買い手・売り手双方にサービスを提供するAP/e-InvoicingプラットフォームのTradeshiftは、行数上限1万行・レポート25MB上限・履歴6か月しか保持できない自社製BIツールの限界に達し、Amazon Quickへ移行した。組み込みQuickSightダッシュボード、自然言語で質問できるチャットエージェント「AP Auditor」、Designer Modeを含むPremium層という3層構成を、SSO・ネームスペース分離・署名付きURL・約1万4000件の行レベルセキュリティで保護しながら段階的に構築した。結果としてクエリ応答が最大30倍高速化し、TCOを40%削減し、埋め込み分析自体を収益を生むプロダクトへと転換した。

## 設計のポイント

- 埋め込みダッシュボード・自然言語チャットエージェント・ティア別データ自律性(Standard/Premium)の3層構成でBI体験を段階的に高度化する
- SSO認証・カスタムネームスペースによるテナント分離・時限署名付きURL・行レベルセキュリティ(約1万4000ルール)を重ねた多層防御でマルチテナント埋め込み分析を保護する
- PoC→組み込みMVP→フル機能ロールアウトという段階的移行により、社内BIと顧客向け分析の両方を無停止で置き換える
- 定型的な自然言語の問い合わせに答えるチャットエージェントを設けることで、BIチームへの依頼をなくし日次対応から解放する

## 使いどころ

- 自社開発BIツールの保守負荷と機能上限が事業成長に追いつかなくなった企業
- 買い手・売り手など複数の顧客セグメントにセルフサービス分析を提供したいマーケットプレイス型SaaS
- CSVエクスポートやExcel集計など手作業レポーティングに多くの工数を割いているカスタマーサクセスや財務チーム
