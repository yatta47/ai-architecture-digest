---
type: announcement
title: フルマネージドのエージェント向けナレッジベースでRAG基盤構築を数分に短縮
title_original: Build enterprise search for agents with Amazon Bedrock Managed Knowledge Base
industry: cross-industry
cloud:
- aws
patterns:
- rag
- document-processing
- full-text-search
components:
- Amazon Bedrock Managed Knowledge Base
- Amazon S3
- Microsoft SharePoint
- Atlassian Confluence
- Google Drive
- Microsoft OneDrive
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-enterprise-search-for-agents-with-amazon-bedrock-managed-knowledge-base/
published_at: '2026-07-16'
---

## 概要

Amazon BedrockのManaged Knowledge Baseが一般提供となり、コネクタ・パーサー・ベクトルストア・アクセス制御をそれぞれ個別に構築していたRAG基盤を、フルマネージドな単一サービスに集約した。SharePointやConfluenceなど6種のネイティブコネクタとリアルタイムACLチェック、自動チャンキング、ハイブリッド検索を標準搭載し、Syngenta GroupやOpenAIなどが社内ナレッジ検索やエージェント向けRAGに採用している。

## 設計のポイント

- 取得・解析・ベクトルストア・検索をすべてサービス側で自動プロビジョニングし、利用者はモデルやチャンク戦略を選ばなくても数分で最初の検索結果を得られるようにする。
- 事前フィルタリングされたACLチェックに加え、クエリ時に認可元へリアルタイムでアクセス権を確認する二重のアクセス制御で、権限情報の陳腐化を防ぐ。
- コンテンツ種別ごとに解析戦略を自動選択し、表・図・音声・動画を含む多様なドキュメントを個別パイプラインなしで扱えるようにする。
- 差分同期により変更・追加されたドキュメントのみを再処理し、コストと鮮度劣化を抑える。

## 使いどころ

- 複数の企業ナレッジソース（SharePoint、Confluence、Google Driveなど）を横断してエージェントに検索させたい企業。
- ベクトルDBの選定・運用やチャンキング戦略の設計にリソースを割けないチームが、素早くRAGを立ち上げたい場合。
- 文書レベルのアクセス制御を維持したまま、大量の社内文書をエージェントの回答根拠として使いたいセキュリティ重視の組織。
