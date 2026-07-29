---
type: opinion
title: AI時代のセキュリティ意思決定は『良い問い』から始まるという提言
title_original: Better security starts with better questions
industry: cross-industry
cloud: []
patterns:
- defense-in-depth
- human-in-the-loop
- guardrails
components: []
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/security/blog/2026/07/29/better-security-starts-with-better-questions/
published_at: '2026-07-29'
---

## 概要

Microsoft Security幹部による、AIが防御側に与える情報量・分析力の拡大は自動的に良い意思決定を意味しないという論考。多層防御(defense in depth)とAI出力への人間による検証・ガバナンスを組み合わせ、単一のツールやシグナルに答えを委ねない『システム思考』での設計を提唱する。

## 設計のポイント

- 多層防御(defense in depth)によりコード・データ・ID・統合面の各層で単一障害点を作らない
- AIが生成した洞察は検証・ガバナンス・人間の判断を経てから意思決定に反映する
- 単一のシグナル・ツール・モデルに答えを委ねず、複数の情報源と専門知を組み合わせて確信度を高める

## 使いどころ

- AI活用を拡大しているセキュリティ組織のガバナンス・ポリシー設計
- 脅威インテリジェンスなど不確実性が高く迅速な判断が求められるチームの意思決定プロセス設計
