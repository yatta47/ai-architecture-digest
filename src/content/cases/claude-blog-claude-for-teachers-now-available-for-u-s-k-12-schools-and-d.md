---
type: announcement
title: Claude for Teachers、米国K-12の学校・学区向けにEnterprise提供を開始
title_original: Claude for Teachers, now available for U.S. K-12 schools and districts
company: Anthropic
industry: public-sector
cloud: []
patterns:
- guardrails
components:
- Claude for Teachers
- Claude Enterprise
- SSO
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-for-teachers-now-available-for-schools-and-districts
published_at: '2026-08-28'
---

## 概要

Anthropicは無料の個人向け教育者提供だったClaude for Teachersを、米国のK-12学校・学区が一元管理できる無料Enterpriseプランとして拡張した。ドメイン認証とSSOで教職員を組織アカウントに統合し、州の学習基準に沿った授業準備・理解度確認などの教育スキルとFERPA準拠のデータ保護契約を学区単位で提供する。

## 設計のポイント

- 学区管理者がドメイン認証とSSOでアカウントを一元管理し、既に個人検証済みの教員もドメインキャプチャで自動的に組織アカウントへ移行する設計。
- 生徒データはモデル学習に利用しない方針とK-12向けデータ処理契約（DPA）をセットで提供し、FERPA準拠を学区単位で担保している。
- 利用上限は個人版Claude for Teachersと同水準に揃え、追加課金はデフォルトで無効化することでコスト超過リスクを抑えている。

## 使いどころ

- 学区・学校のIT管理者が多数の教職員アカウントを一括管理し、アクセス権限やポリシーを統制したい場面。
- 教員が学習指導要領に沿った授業準備や理解度確認クイズを短時間で作成したい場面。
