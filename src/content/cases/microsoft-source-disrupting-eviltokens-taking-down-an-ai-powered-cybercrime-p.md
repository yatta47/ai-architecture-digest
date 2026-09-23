---
type: case
title: AIチャットボットを組み込んだ詐欺基盤EvilTokensのMicrosoftによる摘発
title_original: 'Disrupting EvilTokens: taking down an AI-powered cybercrime platform'
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
components:
- Microsoft Threat Intelligence
- EvilTokens
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/on-the-issues/2026/09/22/disrupting-eviltokens-the-ai-chatbot-built-for-cybercrime/
published_at: '2026-09-22'
---

## 概要

MicrosoftはAIチャットボットで侵害した受信箱を分析し、標的選定やなりすましまで支援していた犯罪基盤EvilTokensを摘発し、50サイトを押収、150超のドメインを無効化した。2026年2月の開始から1.2万超の受信箱が侵害され、AIの悪用が攻撃の判断まで自動化した事例である。

## 設計のポイント

- デバイスコードフィッシングで認証コードを入力させ、パスワードなしで受信箱にアクセスする。
- AIが受信箱から資金移動担当や請求書を抽出し、なりすまし文面まで提案する。
- パスワード変更だけでなくセッションとトークンの失効も必要になる。

## 使いどころ

- AI悪用型のBEC・詐欺への防御を設計するセキュリティチーム。
- デバイスコード認証の運用を見直す管理者。
- 脅威インテリジェンスの事例を収集する担当者。
