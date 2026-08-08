---
type: announcement
title: GitHub Copilotコードレビューの「深さ」を選べるEffort Levelsが正式提供
title_original: Copilot code review effort levels are generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot code review
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-07-copilot-code-review-effort-levels-are-generally-available
published_at: '2026-08-07'
---

## 概要

GitHub Copilotのコードレビューに、変更の複雑さやリスクに応じてレビューの深さを選べるLite/Balancedのeffort levelが正式提供された。Balancedではより高い推論能力を持つモデルで詳細な分析を行い、組織単位でデフォルトのレビュー深度を設定しつつ個別レビューでの上書きも可能にしている。

## 設計のポイント

- ドキュメント修正など軽微な変更向けのLiteと、セキュリティや複雑なロジック向けに高推論モデルを使うBalancedを分離し、コストと精度のバランスを取れるようにした。
- 組織単位のデフォルトeffort levelを設定しつつ、リポジトリやレビュー単位での上書きを許容し、ガバナンスと柔軟性を両立させた。
- どのeffort levelでレビューが実行されたかをタイムラインやPR概要に明示し、レビュー深度の追跡を可能にした。

## 使いどころ

- 大量のPRを扱うチームが、変更の重要度に応じてレビューコストとレイテンシを最適化したい場合。
- セキュリティ影響の大きい変更にはより厳密なAIレビューを、日常的な軽微な変更には軽量なレビューを適用したい組織。
