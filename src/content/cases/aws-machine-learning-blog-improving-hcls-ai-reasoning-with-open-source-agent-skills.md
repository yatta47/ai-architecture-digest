---
type: case
title: ヘルスケア・ライフサイエンス向けオープンソースAgent Skillsで推論精度を改善
title_original: Improving HCLS AI reasoning with open-source agent skills
company: AWS
industry: healthcare
cloud:
- aws
patterns:
- context-engineering
- multi-agent-orchestration
- ai-agent
- eval
components:
- Amazon Bedrock AgentCore
- AWS Strands Agents SDK
- Kiro
- Amazon Quick Desktop
- Claude Code
- OpenAI Codex
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/improving-hcls-ai-reasoning-with-open-source-agent-skills/
published_at: '2026-09-16'
---

## 概要

AWSは、ゲノム解析・保険金請求査定・臨床試験設計・医用画像などHCLS（ヘルスケア・ライフサイエンス）11領域をカバーする38種のオープンソースAgent Skills集を公開した。SKILL.mdという構造化Markdownにドメインの意思決定手順を記述し、Amazon Bedrock AgentCore・AWS Strands Agents SDK・Kiro・Amazon Quick Desktop・Claude Code・OpenAI Codexなど20以上のサービスでそのまま利用できる。RAGやファインチューニングとは異なり推論時にプロンプトとして段階的開示されるスキルにより、スキルなしのエージェントに対して70〜86%の勝率でヘッドツーヘッド評価に勝利し、特に批判的思考では78〜85%の勝率を記録した。

## 設計のポイント

- ドメイン知識をモデル重みに埋め込まず、人間が読める構造化Markdown（SKILL.md）として監査・保守しやすい形で外出しする
- 推論の手順を示す「reasoning skill」と実行コマンドを示す「pipeline skill」を分離し、判断力と実行精度の両方を担保する
- トリガーパターンに基づく段階的開示でスキルを選択的に発火させ、関連スキルのみを読み込んで出力の的確さを保つ
- 単一エージェント・マルチエージェント・本番ホスティング（AgentCore）まで同じスキル資産をそのまま使い回せるようにする

## 使いどころ

- ACMG/AMP基準など複雑な判定フレームワークを正確に適用したいゲノムバリアント解釈業務
- 診療コードの変更がリスク調整（RAF）に与える影響など、保険金請求・医療事務の専門判断を自動化したい場面
- モデルの再学習なしに、年次改定される医療ポリシーや実験基準を反映し続けたい運用チーム
- 複数のエージェント基盤（Kiro、Strands、AgentCore、Claude Code等）を横断して同じドメイン知識を再利用したい開発チーム
