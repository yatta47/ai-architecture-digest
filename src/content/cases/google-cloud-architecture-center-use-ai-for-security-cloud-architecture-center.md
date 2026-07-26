---
type: guidance
title: AIを活用したセキュリティ運用の自律度モデル
title_original: Use AI for security
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- human-in-the-loop
- decision-execution
- llmops
components:
- Gemini in Security
- Gemini in Security Command Center
- Gemini in Google SecOps
- Google Threat Intelligence
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/framework/security/use-ai-for-security
published_at: '2026-07-19'
---

## 概要

Google Cloud Well-Architected Frameworkが、脅威検知・対応・ガバナンスにAIを組み込むための原則を提示。Manual→Assisted→Semi-autonomous→Autonomousという4段階の『セキュリティ自律度』モデルを軸に、Geminiや脅威インテリジェンスAIをセキュリティ運用のどこにどう組み込むかを整理する。

## 設計のポイント

- Manual/Assisted/Semi-autonomous/Autonomousの4段階でAIの関与度を定義し、タスクごとに適切な自律レベルを選ぶ
- GeminiによるアラートのAI要約・自然言語クエリで、非専門家でもセキュリティ運用にアクセスできるようにする
- マルウェア解析やルール生成などの反復作業をAIに自動化させ、アナリストの負荷と対応時間を削減する
- AIをリスク管理・ガバナンスプロセス(モデルインベントリ、リスクプロファイリング)にも組み込み、セキュアなAI開発を支える

## 使いどころ

- サイバー攻撃の増加・巧妙化に対して、限られたセキュリティ人材で対応範囲を広げたいSOCチーム
- アラート内容の解釈やクエリ作成を専門家以外にも開放し、セキュリティ対応を組織全体に広げたい企業
- AI活用の段階を『支援』から『半自律』へ計画的に引き上げたいセキュリティ運用の高度化プロジェクト
