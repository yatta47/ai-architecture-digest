---
type: guidance
title: KiroとスキルファイルによるPHPからJavaへの再現可能な移行エンジン
title_original: Build a repeatable PHP-to-Java migration engine with Kiro
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- spec-driven-development
- human-in-the-loop
- eval
components:
- Kiro
- AWS Transform
- Spring Boot
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-repeatable-php-to-java-migration-engine-with-kiro/
published_at: '2026-10-29'
---

## 概要

PHPアプリをJavaへ移行する作業を、スキルファイル群・機械的な探索スキャナ・8フェーズのワークフローからなる再利用可能なエンジンとして構成する方法。元のPHPを仕様とみなし、パリティハーネスで検証が通るまで移行完了としない。Kiroで対話的に、またAWS Transformでポートフォリオ規模に実行できる。

## 設計のポイント

- 移行知識をバージョン管理されたMarkdownのスキルとして切り出し、複数の実行環境で再利用する。
- 既存コードを仕様とし、パリティハーネスで振る舞い同等性を検証してから完了とする。
- 各フェーズに承認ゲートを置き、探索マニフェストやルールブックを人が確認する。

## 使いどころ

- レガシーWebアプリの言語移行を複数案件で標準化したい開発組織。
- AIエージェントに大規模移行を任せつつ品質を担保したい場面。
