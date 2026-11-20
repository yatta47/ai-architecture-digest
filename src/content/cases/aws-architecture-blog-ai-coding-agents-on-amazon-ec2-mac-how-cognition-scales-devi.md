---
type: case
title: Cognition DevinがEC2 Mac上でmacOS環境を提供する構成
title_original: 'AI coding agents on Amazon EC2 Mac: How Cognition scales Devin for macOS'
company: Cognition
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- parallel-execution
components:
- Amazon EC2 Mac
- AWS Nitro System
- Devin
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/ai-coding-agents-on-amazon-ec2-mac-how-cognition-scales-devin-for-macos/
published_at: '2026-11-20'
---

## 概要

AIソフトウェアエンジニアDevinがiOSアプリをビルド・検証できるよう、CognitionはEC2 Macホスト群上でセッションごとに新規macOS VMを1分未満で起動する。6リージョンのフリートで、ローンチ後6週間で約1,000組織が利用した。

## 設計のポイント

- セッションごとに新規VMを用意し、永続ディスク・ネットワーク規則・事前構築済み開発環境を他OSワークスペースと同等に揃える。
- 物理Macをクラウドで借り、調達・保守の負担を避ける。
- ユーザーとエージェントの双方が実行中アプリを操作・確認できる経路を用意する。

## 使いどころ

- Apple向けアプリ開発をエージェントに任せたい企業に向く。
- macOSフリートをCIや自動テスト用に計画する際の参考になる。
