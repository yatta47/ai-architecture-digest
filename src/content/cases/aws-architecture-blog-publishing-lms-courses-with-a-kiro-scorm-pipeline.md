---
type: case
title: KiroエージェントでLMS用SCORMコースを素材から自動パッケージ化
title_original: Publishing LMS courses with a Kiro SCORM pipeline
company: AWS
industry: other
cloud:
- aws
patterns:
- ai-agent
- spec-driven-development
- document-processing
components:
- Kiro
- kiro-cli
- SCORM 1.2
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/publishing-lms-courses-with-a-kiro-scorm-pipeline/
published_at: '2026-10-27'
---

## 概要

スライドや文書などの研修素材から、Kiroが計画・執筆・lint・ビルド・検証までを会話で進め、LMSにアップロードできるSCORM 1.2のzipを出力する。小規模コースなら数分で生成できる。

## 設計のポイント

- course.yamlマニフェストにモジュールやSCORM設定を集約し、エージェントの作業と成果物の形を固定する。
- Steering・Specs・Hooksの3つのKiro機能で常時文脈と手順、自動検証を分担させる。
- lintと検証を工程に入れ、構造不備やSCORM不適合を取り込み前に検出する。

## 使いどころ

- 研修担当者がパッケージ作業なしでコンテンツ制作に集中したい場面。
- エージェントIDEで定型の変換・ビルドを手順化したいチーム。
