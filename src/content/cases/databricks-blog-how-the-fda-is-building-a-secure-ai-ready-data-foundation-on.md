---
type: case
title: FDAのセキュアなAI基盤刷新（Databricks on AWS GovCloud + Unity Catalog）
title_original: How the FDA is building a secure, AI-ready data foundation on Databricks for Government
company: FDA（米国食品医薬品局）
industry: public-sector
cloud:
- aws
patterns:
- multi-tenant-analytics
- text-to-sql
- data-federation
- cost-optimization
components:
- Databricks
- Unity Catalog
- AWS GovCloud
- Genie
- PrivateLink
- Terraform
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-fda-building-secure-ai-ready-data-foundation-databricks-government
published_at: '2026-09-01'
---

## 概要

FDA（米国食品医薬品局）は、Databricks on AWS GovCloudとUnity Catalogを基盤に、複数の規制センターが共通基盤を共有しつつ各自のガバナンスを維持する「HALO」というエンタープライズAIデータ基盤を構築した。5,000人超のユーザーと8,000超のジョブ・パイプラインを無停止で移行し、SQLクエリ速度30%向上、計算コスト20%削減、データ提供・共有にかかる時間75%削減を実現し、利用者数も6,000人超（当初は約500人）に拡大した。

## 設計のポイント

- Unity Catalogを単一のガバナンス層とし、各規制センターが共通基盤を共有しつつ独自の鍵と方針を持つマルチテナント設計（『アパート方式』）を採用
- Terraformによるセキュリティ参照アーキテクチャで、PrivateLinkや顧客管理キー、コンプライアンスセキュリティプロファイルを標準装備し、監査対応環境を迅速に構築
- FedRAMP High認証取得、AWS GovCloud移行、Unity Catalog導入という3段階のマイルストーンを踏み、業務を止めずに基盤を刷新
- サーバーレスコンピュートとGenie、モデルサービングを組み合わせ、レガシーダッシュボードをAI対応の対話型体験へ刷新

## 使いどころ

- FedRAMP High／IL5など厳格な規制下でAI・分析基盤を運用する必要がある政府機関
- 複数部門・複数センターにまたがるデータをガバナンスを保ったまま共有したい組織
- サービス停止が許されない中で大規模なレガシー基盤の刷新を進めたい情報システム部門
