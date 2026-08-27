---
type: case
title: Warp、Claude Skillsで自己改善するコードレビュー/課題トリアージエージェントを構築
title_original: How Warp builds self-improving agents on Claude
company: Warp
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- prompt-optimization
- ci-cd
components:
- Claude Platform
- Claude Code
- GitHub Actions
- Agent Skills
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude
published_at: '2026-08-26'
---

## 概要

AIターミナル企業Warpは、セッション終了とともに消えてしまう人間フィードバックをスキルファイルに蓄積し続ける「自己改善ループ」を構築した。ドメイン知識を持つ基本スキルと、フィードバックを分析して基本スキルへの修正案をPRとして提案する改善役スキルの2層構成で、コードレビューやIssueトリアージなどのエージェントを継続的に賢くしている。

## 設計のポイント

- 基本スキル（実行担当）と改善スキル（定期実行の観測者）を分離し、人間フィードバックを介して基本スキルを段階的に更新する
- フィードバックはPRコメントなど普段の作業導線で自然に集め、提出の手間をゼロに近づけることで継続的なシグナル収集を可能にする
- スキルは『変数命名の規則を列挙する』のではなく『重複コードを探す』のような原則と理由（why）を書き、汎化しやすくする
- スキルは小さく保ち、詳細はリソースファイルへの参照で段階的開示（progressive disclosure）することでコンテキストを圧迫しない

## 使いどころ

- 数百人規模のコントリビューターが数千件のコードレビューを回すOSSプロジェクトで、レビューエージェントの品質を継続的に底上げしたい場合
- Issueトリアージなど定型だが判断基準が暗黙知に依存するタスクを、人間の訂正から学習するエージェントに任せたい場合
- プロンプトの手動チューニングがスケールしなくなった、複数の類似エージェント（レビュー/トリアージ/spec作成）を運用するチーム
