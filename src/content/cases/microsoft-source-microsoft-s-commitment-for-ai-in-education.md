---
type: opinion
title: 教育向けAI活用における5原則とCopilotベースの学習支援
title_original: Microsoft's commitment for AI in education
company: Microsoft
industry: other
cloud:
- azure
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- Microsoft 365 Copilot
- Teach in Microsoft 365 Copilot
- Copilot Chat
- Minecraft Education
- Learning Accelerators
- Study and Learn Agent
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/blog/2026/09/16/microsofts-commitment-for-ai-in-education/
published_at: '2026-09-16'
---

## 概要

Microsoftは教育現場でのAI活用について、安全性・プライバシー、教員の主導権維持、思考力を代替しない設計など5つの原則を掲げ、全米教員連盟(AFT)と共同で学校向けのプライバシー・安全基準を新設した。Teach in Microsoft 365 CopilotやCopilot Chat、Study and Learn Agentなど学年に応じたAI体験を展開し、Brisbane Catholic Educationでの学習意欲275%向上やMiami Dade Collegeでの合格率15%向上などの導入効果を報告している。

## 設計のポイント

- 教員向けCopilot（Teach）と生徒向けCopilot Chatを分離し、K-12ではデフォルトオフ＋管理者制御で学年に応じ段階的に有効化する
- American Federation of Teachersと共同策定したPrivacy & Safety Standardで、データ利用範囲の制限と重要判断への人的関与を必須化する
- Education Insiders Programで現場教員のフィードバックを製品開発に反映し、教員が意思決定の中心であり続ける設計とする
- Minecraft Education→Learning Accelerators→Study and Learn Agentと学年進行に合わせてAIの関与度を段階的に引き上げる

## 使いどころ

- AI導入時に学校区・教育委員会が説明責任あるプライバシー/安全基準を必要とする場面
- 教員の事務負担（教材の個別最適化・授業設計）をAIで削減しつつ教育の質を落としたくない現場
- K-12など未成年向けにAIアクセスを年齢適応的かつ管理者統制のもとで段階導入したいケース
