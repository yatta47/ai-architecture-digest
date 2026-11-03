---
type: case
title: Copilot Cowork：エージェント主体開発で9人が1日1,211PR、ランタイムをPythonからRustへ稼働中移行
title_original: 'Nine engineers, 1,211 pull requests in a day: Lessons from building Copilot Cowork'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- spec-driven-development
- ci-cd
- human-in-the-loop
components:
- Copilot Cowork
- Work IQ
- Microsoft 365
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://commandline.microsoft.com/how-we-built-copilot-cowork-python-to-rust-migration/
published_at: '2026-11-02'
---

## 概要

Microsoftの小規模チームはCopilot Cowork（マルチステップ業務を代行するエージェント層）を約4.5か月でGAし、稼働中にランタイムをPythonからRustへ移行した。コードの大半はエージェントが書き、人は仕様・境界設定・高リスク変更のレビューに集中した。

## 設計のポイント

- 仕様を明確にし、アーキテクチャとセキュリティ境界は人が決める
- 全変更に自動チェックとエージェントレビューを通し、人は高リスクや意見相違に注力
- ライブ移行で信頼性・セキュリティ・コストを維持しつつ高速に回す

## 使いどころ

- エージェント主導開発を導入する開発組織
- 大規模ランタイム移行を無停止で進めたいチーム
