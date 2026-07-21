---
type: guidance
title: Amazon Bedrock RAGにCedarポリシーで部門横断のドキュメントアクセス制御を組み込む設計
title_original: Secure multi-tenant RAG with Amazon Bedrock and Verified Permissions
industry: cross-industry
cloud:
- aws
patterns:
- multi-tenant-rag
- rag
- policy-as-code
- defense-in-depth
components:
- Amazon Bedrock
- Amazon Bedrock Knowledge Bases
- Amazon Verified Permissions
- AWS Lambda
- Amazon Cognito
- Amazon SQS
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/secure-multi-tenant-rag-with-amazon-bedrock-and-verified-permissions/
published_at: '2026-06-22'
---

## 概要

単一のAmazon Bedrock Knowledge Baseを複数部門で共有しつつ、Amazon Verified PermissionsのCedarポリシーで検索時のメタデータフィルタを動的に生成することで、部門・役職ごとのドキュメントアクセスを制御する設計を紹介する。ナレッジベースをテナントごとに複製せずに済むためコストと運用負荷を抑えられ、認可ルールもコード再デプロイなしで随時更新できる。

## 設計のポイント

- 認可ロジックをアプリケーションコードから切り離し、Cedarポリシーとして外部化することで、監査可能かつ実行時に変更可能なガバナンスを実現する。
- メタデータフィルタリングによる論理的分離とIAMによるインフラ分離を使い分け、テナント間の強い境界にはナレッジベースを分ける一方、テナント内の部門間には本パターンを重ねる。
- 認可サービス障害時はdeny-by-default（拒否優先）とし、フィルタ構築ロジックがフェイルオープンして他部門のドキュメントが露出しないよう設計する。
- ドキュメント取り込みとタグ付けの間に生じる競合状態を考慮し、サイドカー未生成のドキュメントを除外する取り込みガードを設ける。

## 使いどころ

- 単一組織内で部門・役職ごとに閲覧可能なドキュメントを分けたいが、テナントごとにナレッジベースを増やすコストは避けたい企業。
- アクセスルールが頻繁に変わり、コード再デプロイなしで運用したい社内向け生成AIアプリケーション担当チーム。
- 経営層など複数部門を横断する権限を持つユーザーへの例外的アクセスを、監査可能な形で管理したい場合。
