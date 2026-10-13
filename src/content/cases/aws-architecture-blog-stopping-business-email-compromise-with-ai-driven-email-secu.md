---
type: case
title: AIでビジネスメール詐欺を検知するVIPREのメールセキュリティ
title_original: 'Stopping business email compromise with AI-driven email security: How VIPRE protects modern enterprises on
  AWS'
company: VIPRE Security Group
industry: cross-industry
cloud:
- aws
patterns:
- event-driven
- defense-in-depth
components:
- AWS
- Microsoft 365
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/stopping-business-email-compromise-with-ai-driven-email-security-how-vipre-protects-modern-enterprises-on-aws/
published_at: '2026-10-13'
---

## 概要

VIPREはAWS上のサーバーレス・イベント駆動構成で、意味的類似度や文脈言語モデル等の多層MLによりBECを検知するIntegrated Email Securityを構築した。Microsoft 365とAPI連携しMXレコード変更なしで導入でき、本番で1日50万通超を処理する。

## 設計のポイント

- MXリダイレクト型SEGではなくM365とのAPI連携にして、内部トラフィックやスレッド乗っ取りも見る。
- 意味的類似・意図/トピック分析・リンクや添付の動的解析と複数のML層を重ねる。
- サーバーレスでメール量の変動に合わせてスケールする。

## 使いどころ

- 既存のM365環境へ業務を止めずに追加のメール防御を入れたい企業。
- なりすましメール対策を検討するセキュリティ部門。
