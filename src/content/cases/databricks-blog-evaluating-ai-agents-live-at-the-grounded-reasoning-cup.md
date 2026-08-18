---
type: case
title: 企業文書に対するAIエージェントの根拠推論力をライブ競技で検証(Grounded Reasoning Cup)
title_original: Evaluating AI Agents Live at the Grounded Reasoning Cup
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
- document-processing
- parallel-execution
components:
- OfficeQA
- OfficeQA Pro V2
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/evaluating-ai-agents-live-grounded-reasoning-cup
published_at: '2026-08-18'
---

## 概要

Databricksは米財務省の文書約12万ページから構築した新ベンチマークOfficeQA Pro V2を使い、11の大学チームがOpenAI・Anthropic・Google DeepMindのモデルで開発したエージェントをライブ競技で評価するGrounded Reasoning Cupを開催した。既存ベンチマークで培った手法は必ずしも新しいコーパスに汎化せず、素のフロンティアエージェントの平均正答率は30%未満にとどまったが、優勝したスタンフォードチームは再利用可能なスキルライブラリ、文書表現のフォールバック、適応的検証を組み合わせて63.3%の正答率を達成した。同一モデルを使うチーム間でも最大30.4ポイントの性能差が生じ、エージェント性能はモデル単体でなくパース・検索・ツール利用・検証・並列処理を含むシステム全体設計に依存することが示された。

## 設計のポイント

- 新しいベンチマークでのheld-out評価により、既存ベンチマークでの改善が実世界の別コーパスに汎化するかを検証する
- エージェント性能はモデル選択だけでなく、文書パース・検索・ツール利用・検証・並列実行を含むシステム全体の設計で決まる
- 再利用可能なスキルライブラリ、文書表現のフォールバック手段、適応的な検証ステップを組み合わせることで高精度化できる
- 競技形式(短時間ラウンド・再提出制限)により、実運用に近い時間制約下でのエージェント性能を評価する

## 使いどころ

- 大量の社内文書やドメイン固有コーパスに対するエージェントの根拠に基づく質問応答能力を検証したいチーム
- 既存ベンチマークでのチューニングが新しいデータセットに汎化するかを事前に見極めたいAI開発チーム
- フロンティアモデルまかせではなく検索・検証・並列処理を含むエージェントシステム全体を設計したいチーム
