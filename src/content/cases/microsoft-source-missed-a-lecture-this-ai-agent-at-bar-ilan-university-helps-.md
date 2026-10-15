---
type: case
title: Moodle上の講義資料に限定して回答する大学向け学習支援エージェント
title_original: Missed a lecture? This AI agent at Bar-Ilan University helps students catch up
company: Bar-Ilan University
industry: public-sector
cloud:
- azure
patterns:
- ai-agent
- rag
- multilingual-localization
components:
- Microsoft Copilot Studio
- Azure AI Services
- Moodle
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/emea/features/missed-a-lecture-this-ai-agent-at-bar-ilan-university-helps-students-catch-up/
published_at: '2026-10-15'
---

## 概要

バル=イラン大学はMoodle上に、講義録画・書き起こし・資料のみを根拠とする学習エージェントをKPMGとOpenAppがCopilot Studioで構築し試験導入した。71科目・約2,400人で検索・要約・小テストを提供し、次学期は100科目へ拡大する。

## 設計のポイント

- 回答の根拠を教員がアップロードした教材に限定する
- ヘブライ語・アラビア語・英語に対応する
- 大学のセキュアなAzure環境内で運用する

## 使いどころ

- 欠席した講義の内容を素早く補いたい学生
- 教材ベースの学習支援を導入したい教育機関
