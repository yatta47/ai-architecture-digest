---
type: opinion
title: コーディングエージェントは実際どれだけコードを外部送信しているか——5製品のデータ取り扱い比較
title_original: Is your coding agent uploading all your code?
industry: cross-industry
cloud: []
patterns:
- guardrails
- data-privacy
components:
- Claude Code
- Codex
- Cursor
- GitHub Copilot
- Grok Build
outcome:
  type: risk-compliance
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/ai-coding-agent-privacy/
published_at: '2026-08-20'
---

## 概要

SpaceXAIのGrok Build CLIがGitリポジトリ全体を無断でクラウドストレージへ送信していたことが発覚した事件を受け、Claude Code・Codex・Cursor・GitHub Copilot・Grok Buildの5つの主要コーディングエージェントについて、送信されるコード量・学習利用の有無・外部から検証可能かをプライバシー文書ベースで比較する。ゼロデータ保持（ZDR）は送信そのものではなく保持のみを制御する契約上の約束であり、個人サブスクリプションでは通常適用されないという誤解しやすい点を指摘する。

## 設計のポイント

- モデルにコードを読ませる以上、どのエージェントも何らかのコードを外部の推論基盤へ送信せざるを得ない。問われるべきはタスクに必要な範囲を超えて送っていないかという点
- 『モデル改善への利用』トグルはトレーニング同意を制御するだけで、コードがマシンから出て行くかどうかとは無関係な場合がある（Grok Buildの事例）
- ゼロデータ保持（ZDR）は主にエンタープライズ/API向けの契約条項であり、送信後の保持のみを制御する。個人サブスクリプションのユーザーには基本的に適用されない
- 不正利用監視のログは、Privacy Mode/ZDR下でもプロンプトや応答を保持し得るため、『保持しない』という約束にも例外がある

## 使いどころ

- 社内コードをAIコーディングエージェントに読ませる前に、送信範囲と保持ポリシーを比較検討したいセキュリティ/コンプライアンス担当
- 複数のコーディングエージェントを組織で許可リスト化する際の判断材料が欲しいプラットフォームチーム
- ゼロデータ保持や『モデル改善に使わない』設定の実際の効力を正しく理解したい開発者・購買担当
