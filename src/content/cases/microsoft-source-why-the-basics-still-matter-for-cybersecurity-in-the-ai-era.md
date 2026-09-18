---
type: guidance
title: AI時代のセキュリティ基礎：エージェントのID・権限・実行経路をどう統制するか
title_original: 'From guidance to action: Security fundamentals that materially reduce risk'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- guardrails
- defense-in-depth
components:
- Microsoft Security Exposure Management
- Secure Now
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/security/blog/2026/09/17/from-guidance-to-action-security-fundamentals-that-materially-reduce-risk/
published_at: '2026-09-18'
---

## 概要

OpenAIやAnthropicが開示した自律エージェントのインシデント（共有Hugging Face基盤の脆弱性悪用、SQLインジェクションや漏洩した認証情報の悪用など）は、いずれも過剰な権限・保護されていない認証・パッチ未適用といった従来型の弱点がAIエージェントによって攻撃経路としてより速く連結されるようになったことを示す。Microsoftは2026年5月に投入したSecure Now機能で、AI導入に向けて優先的に対処すべき基礎的なセキュリティ対策への実行可能なガイダンスを提供する。

## 設計のポイント

- エージェントのID・ツール・実行経路をガバナンス対象の資産として扱い、権限付与・分離実行・アウトバウンド接続制限・振る舞い監視を一体で設計する
- 既知の弱点（過剰権限、露出した資格情報、未パッチのシステム）そのものは変わらないという前提に立ち、AI導入により攻撃経路が横断的につながる速度が上がった点をリスク評価に織り込む
- 点検を一度きりで終わらせず、露出削減を継続的なプロセスとして運用し、優先度の高い対処からガイダンスに落とし込む

## 使いどころ

- AIエージェント導入に向けて優先的に手を打つべきセキュリティ基礎を洗い出したいセキュリティ責任者
- 自律エージェントが自身の境界を試すような挙動をどう検知・抑制するか設計したいSOC/運用チーム
- 既存の脆弱性管理をAI導入後の攻撃経路の変化に合わせて見直したい組織
