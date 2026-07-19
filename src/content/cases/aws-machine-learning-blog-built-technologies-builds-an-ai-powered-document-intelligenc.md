---
type: case
title: 不動産金融の契約書処理をエージェント型ドキュメント理解基盤に刷新
title_original: Built Technologies builds an AI-powered document intelligence solution on AWS to power agents across real
  estate finance
company: Built Technologies
industry: financial-services
cloud:
- aws
patterns:
- document-processing
- ai-agent
- human-in-the-loop
components:
- Amazon Bedrock
- AWS Intelligent Document Processing (IDP) Accelerator
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/built-technologies-builds-an-ai-powered-document-intelligence-solution-on-aws-to-power-agents-across-real-estate-finance/
published_at: '2026-07-15'
---

## 概要

5000億ドル規模の不動産プロジェクトを扱うBuilt Technologiesは、OCRと従来型MLによる26種類の抽出プロセッサでは対応しきれなくなった250種類以上・最大500ページの複雑な金融文書に対し、Amazon BedrockとAWS IDP Acceleratorを用いたエージェント型ドキュメント理解基盤を構築した。融資契約の中に明示的なラベルなく散在するコベナンツを文脈から推論・抽出するなど、単なる抽出から「文書を理解して推論する」方式へ転換し、数日かかっていたワークフローを数分に短縮している。

## 設計のポイント

- キーワード一致による抽出ではなく、文書の該当セクションを特定し定義・義務を推論する「エージェント型ドキュメント理解」へ転換することで、明示的ラベルのない情報（コベナンツ等）も拾えるようにする。
- 文書種別の識別からセクション特定、構造化抽出、原文への参照付けまでを一連のエージェントワークフローとして設計し、レビューのための根拠を常に残す。
- 信頼度が低い、または曖昧な結果は自動処理せず専門家によるレビューへルーティングし、その修正結果をスキーマ・プロンプト・評価にフィードバックする。
- 95%超という金融・コンプライアンス業務で求められる高い信頼度要件を満たすため、分類・抽出それぞれに評価ワークフローを組み込む。

## 使いどころ

- 融資契約や保険証券など、非定型かつドメイン固有の言い回しが多い金融文書を大量に処理する必要がある組織。
- 複数の製品・業務にまたがって再利用できる横断的なドキュメント理解基盤を構築したい企業。
- 抽出結果の信頼度に応じて自動処理と人手レビューを使い分けたいコンプライアンス重視の業務。
