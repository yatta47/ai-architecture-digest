---
type: guidance
title: Claude Codeのスキル運用から得た9分類のベストプラクティス
title_original: 'Lessons from building Claude Code: How we use skills'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- llmops
components:
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
published_at: '2026-06-03'
---

## 概要

Anthropicは社内で数百のスキルをClaude Codeに実装してきた経験から、スキルをライブラリ/APIリファレンス、プロダクト検証、データ取得・分析、業務自動化、コードスキャフォールディング、コード品質レビュー、CI/CDなど9つのカテゴリに整理した。優れたスキルは単一のカテゴリに明確に収まり、複数の役割を欲張ったスキルはエージェントを混乱させやすいこと、特にプロダクト検証系のスキルが出力品質への効果が最も大きいことが分かったという。

## 設計のポイント

- スキルは単一のカテゴリ（例:ライブラリ参照、検証、データ取得、業務自動化など）に明確に収まるよう設計し、複数の役割を混在させない
- スキルはただのMarkdownではなくスクリプトやアセットを含むフォルダであり、動的フックの登録などClaude Code固有の設定を活用することで効果が高まる
- プロダクト検証スキル（PlaywrightやtmuxによるE2E確認、出力動画の記録、各ステップでの状態アサーションなど）への投資は出力品質に対する効果が最も大きい
- 業務自動化スキルでは過去の実行結果をログファイルに保存させることで、モデルが一貫性を保ち前回の実行を踏まえた判断をしやすくする

## 使いどころ

- 社内ライブラリやCLIの落とし穴・ガードレールをエージェントに継続的に守らせたい開発基盤チーム
- サインアップやチェックアウトなど重要フローの検証をヘッドレスブラウザ等で自動化し、Claudeの出力品質を底上げしたい場合
- スタンドアップ投稿やチケット作成、週次レポートなど定型的な社内業務をコマンド化して自動化したいチーム
- コードレビューやCI/CDのフローにフックとして組み込み、コード品質やデプロイの安全性を継続的に担保したい組織
