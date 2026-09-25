---
type: announcement
title: '新Copilot: Home・Code・Autopilotと管理ランタイム'
title_original: Introducing the new Copilot with Home, Code and Autopilot
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- unified-runtime
- context-engineering
components:
- Microsoft Copilot
- Copilot Managed Runtime
- Microsoft IQ
- Fabric IQ
- Copilot Studio
- GitHub Copilot
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/
published_at: '2026-09-25'
---

## 概要

MicrosoftがCopilotアプリにHome(チャットとCoworkの統合)、Code(自然言語で小さなアプリを作る)、Autopilot(常駐する自律エージェント)を追加すると発表した。テナント内でコードを安全に動かすCopilot Managed Runtimeや、AI向けFinOps機能も併せて示された。

## 設計のポイント

- Autopilotに独自のID・メモリ・ワークスペースを持たせ、権限・監査・ガバナンスの下で運用する。
- Copilot Managed Runtimeで生成コードをM365環境内でIT管理下に実行する。
- Microsoft IQ/Fabric IQで業務文脈とセマンティックモデルをエージェントの根拠にする。

## 使いどころ

- M365中心の企業でエージェントを全社展開する際の参考。
- 従業員が作る小規模アプリのホスティングを統制したい場面。
