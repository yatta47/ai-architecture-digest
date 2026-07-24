---
type: case
title: AIがSalesforceの数十年来のローカライゼーションパイプラインを再構築
title_original: How AI rebuilt Salesforce's decades-old localization pipeline
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- multilingual-localization
- context-engineering
- llmops
components:
- Translation Management System (TMS)
outcome:
  type: cost
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-ai-rebuilt-salesforces-decades-old-localization-pipeline/
published_at: '2026-07-23'
---

## 概要

リリースごとの翻訳量が35%以上増える一方で予算とリリース期間は固定という制約の中、Salesforceは単一プロンプトでのLLM翻訳ではなく、最大85段階の専門特化プロンプトからなるAIオーケストレーションパイプラインを構築し、ローカライゼーションコストを50〜90%削減した。

## 設計のポイント

- 単一プロンプトの改善では文法・ブランディング・製品文脈のいずれかが常に犠牲になったため、プロンプトエンジニアリングとコンテキストエンジニアリングを組み合わせた多段パイプラインに設計を転換した
- 翻訳対象がSales CloudかHealth Cloudかなど製品文脈を先に確定させてから翻訳することで、同一UI文字列でも製品ごとに適切な訳語を選べるようにする
- 人間翻訳者向けだったスタイルガイドや用語集を構造化されたLLM用コンテキストとして再設計し、翻訳と自己検証双方の基盤資産として再利用する
- 単一モデルによる判定に頼らず、用語・品質・一貫性を専門に評価する独立した検証パイプラインを翻訳生成パイプラインとは別に設けて本番投入前にゲートする

## 使いどころ

- リリース頻度・言語数が増える一方で翻訳者を増員できないエンタープライズソフトウェア企業
- 顧客がオブジェクト名などをカスタマイズできる製品で、文脈依存の一貫した多言語対応が必要な場合
