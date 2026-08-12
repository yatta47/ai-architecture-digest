---
type: announcement
title: OCIアーティファクトでAIモデルの相互運用性を実現(ModelPack×Docker)
title_original: Advancing AI Model Interoperability with Docker and ModelPack
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- ModelPack
- Docker Model Runner
- OCI
outcome:
  type: productivity
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/12/advancing-ai-model-interoperability-with-docker-and-modelpack/
published_at: '2026-08-12'
---

## 概要

CNCFのModelPackプロジェクトは、OCIアーティファクトを基盤にAIモデルのパッケージング仕様を標準化しており、DockerがDocker Model Runnerの出力フォーマットとしてModelPack形式をサポートするよう提携した。`docker model package --format=cncf`でモデルを標準準拠のOCIアーティファクトとして書き出せるようになり、Docker HubやQuayなど既存のOCIレジストリでの配布・相互運用が可能になった。

## 設計のポイント

- OCIアーティファクトを土台にモデルパッケージング仕様を標準化し、モデル資産をコンテナと同じ配布・保存エコシステムに載せられるようにした。
- DockerとModelPackで異なるOCIメディアタイプ(configディスクリプタ等)を突き合わせ、相互運用のためのマッピングを明文化した。
- フォーマット選択をCLIオプション化し、既存ツールを変えずに標準準拠の成果物を出力できるようにした。

## 使いどころ

- 特定のモデル管理ツールにロックインされず、フレームワーク間でモデル資産を移動・再利用したいMLプラットフォームチーム。
- 社内外にモデルを配布する際、コンテナと同じOCIレジストリをそのまま使いたい組織。
- Docker Model Runnerで作ったモデルを他のCNCF準拠ランタイムでも動かしたい開発者。
