---
type: case
title: エージェント時代のプロビジョニング:Databricksの自己サービス型インフラ払い出し基盤
title_original: 'Provisioning for the agentic era: How Databricks built a self-serve infrastructure vending machine'
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- llm-gateway
- cost-optimization
components:
- Databricks Apps
- Terraform
- Lakebase
- MCP
- Claude
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/provisioning-agentic-era-how-databricks-built-self-serve-infrastructure-vending-machine
published_at: '2026-07-23'
---

## 概要

7,000人超に成長したDatabricksのフィールドエンジニアリング組織向けに、用途を自然言語で記述するだけで隔離・ガバナンス済みのクラウド環境を自動払い出しするField Engineering Vending Machine(FEVM)を構築。React+Python製アプリの裏でTerraformが実際のプロビジョニングを行い、MCP経由でチャットやエージェントからも同じAPIを叩ける。

## 設計のポイント

- 「ワークスペースをください」ではなく「何をしたいか」を平文で記述させるユースケースベースのプロビジョニングを設計原則とする
- MCPを中核に据え、UI・チャット・外部サービス・エージェントすべてを単一の制御点から同じAPIで扱えるようにする
- Lakebase上の状態管理DBで所有者・目的・有効期限をすべてのリソースについて追跡し、90日デフォルトTTLと自動失効通知で放置リソースを防ぐ
- 新しいTerraformテンプレートは繰り返し検証・堅牢化してから公開し、管理系アクションの自動化がセキュリティ境界を越えないよう設計する

## 使いどころ

- 急拡大するフィールド/セールスエンジニアリング組織向けに個別デモ環境を高速かつガバナンス付きで払い出したい場合
- 自然言語指示からエージェントが直接インフラAPIを叩いて複数ステップのセットアップを自動化したい場合
