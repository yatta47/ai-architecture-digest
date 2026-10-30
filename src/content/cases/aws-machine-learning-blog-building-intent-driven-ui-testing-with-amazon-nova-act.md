---
type: case
title: Epsilonのマルチテナント型インテント駆動UIテスト基盤
title_original: Building intent-driven UI testing with Amazon Nova Act
company: Epsilon
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-tenant-rag
- ci-cd
components:
- Amazon Nova Act
- Amazon Bedrock AgentCore Browser
- Playwright
- Model Context Protocol
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-intent-driven-ui-testing-with-amazon-nova-act/
published_at: '2026-10-29'
---

## 概要

Publicis傘下のEpsilonは、Playwrightの回帰テストを置き換えず補完する形で、Amazon Nova ActとBedrock AgentCore Browserによる自然言語のUIテストを社内エージェント基盤のマネージド機能として提供した。セレクタ変更に強く、各プロダクトチームはブラウザ基盤やID連携を個別に用意せず利用できる。

## 設計のポイント

- 決定的な回帰テスト(Playwright)は残し、意図ベースのテストを上乗せして補完する。
- UIテストを共通エージェントAPIの1機能として提供し、ID連携・認可・ブラウザ基盤を各チームから隠蔽する。
- 自然言語のテスト記述でセレクタや画面構造への依存を減らし、UI変更による壊れやすさを抑える。

## 使いどころ

- 多数のプロダクトチームが同一のテスト基盤を共有する大規模組織。
- UI変更が頻繁でスクリプト保守負荷が高いWebアプリの品質保証。
