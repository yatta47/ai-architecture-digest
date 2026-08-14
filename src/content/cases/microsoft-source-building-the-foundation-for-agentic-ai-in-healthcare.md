---
type: case
title: Microsoft Fabric/Dragon Copilot/Copilot Studioで築くヘルスケア向けエージェント基盤:3つの医療機関の事例
title_original: Building the foundation for agentic AI in healthcare
company: Brown University Health, Peterborough Regional Health Centre
industry: healthcare
cloud:
- azure
patterns:
- ai-agent
- data-federation
- context-engineering
components:
- Microsoft Fabric
- Microsoft Dragon Copilot
- Microsoft 365 Copilot
- Copilot Studio
- Azure
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/microsoft-cloud/blog/healthcare/2026/08/11/building-the-foundation-for-agentic-ai-in-healthcare/
published_at: '2026-08-11'
---

## 概要

Microsoftは、統制されたデータ基盤(Microsoft Fabric)・臨床医のワークフローに組み込まれた臨床エージェント(Dragon Copilot)・誰でもエージェントを作れるCopilot Studio・常時稼働のセキュアなAzure基盤の4層で医療機関のエージェント導入を支える。Brown University Healthはドキュメント負担を減らすDragon Copilotから始め、Copilot Studioで1日でプロトタイプ化した20以上のエージェントを展開、Peterborough Regional Health Centreは18の分断されたシステムをMicrosoft Fabricに統合してからエージェントを載せることで、入院ベッド待ち時間43%減など具体的な患者フロー改善につなげた。

## 設計のポイント

- モデルではなくデータ統合から着手し、統制された単一の信頼できるデータソース(Fabric)をエージェントの推論基盤とする
- 臨床エージェントは臨床医が普段使うワークフロー(Dragon Copilot)の内側に組み込み、別画面への切り替えを発生させない
- ローコードのCopilot Studioで現場チーム自身がアイデアから1日でプロトタイプを作れるようにし、全社的なエージェント展開を専門チームのボトルネックにしない
- ガバナンスポリシー策定のような非エンジニアリング業務にもリサーチエージェントを活用し、通常1年かかる作業を4ヶ月に短縮した

## 使いどころ

- ドキュメント負担による臨床医のバーンアウトを軽減したい病院
- 買収・合併等でシステムが分断され、まずデータ統合から着手する必要がある大規模医療システム
- IT専任者以外の現場チームが自分たちでエージェントを作って業務改善したい組織
