---
type: case
title: 下水メタゲノム解析をエージェント協調で加速するMicrosoft Discovery
title_original: 'Decoding Environmental Viromes: Amplifying Human Expertise with Microsoft Discovery'
company: Microsoft
industry: healthcare
cloud:
- azure
patterns:
- multi-agent-orchestration
- human-in-the-loop
- ai-agent
- eval
components:
- Microsoft Discovery
- Premonition Insights
- Microsoft Azure
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://techcommunity.microsoft.com/blog/microsoft-discovery-blog/decoding-environmental-viromes-amplifying-human-expertise-with-microsoft-discove/4555806
published_at: '2026-09-23'
---

## 概要

環境メタゲノム解析で得た約750万件の候補マッチ（6GB）の探索的解釈を、Microsoft Discoveryアプリの協調エージェントで支援した事例。データ準備、環境設定、コード生成、API連携、可視化をエージェントが担い、仮説設定や文献選定、評価基準の策定、結果の判断は専門家が行う。半日未満で探索分析を完了したという。

## 設計のポイント

- 科学的判断は自動化せず、仮説立案、文献の選別、評価ルーブリック、中間出力の検証を専門家が握る。
- Scientific Bookshelfで参照文献を管理し、エージェントの根拠を文献に紐づける。
- エージェントの作業と前提を記録し、再現性、共同作業、教育に使えるドキュメントを生成する。
- クラウド側の大規模並列処理で構造化した分類表を作り、その後の解釈段階のみをエージェントで支援する。

## 使いどころ

- 大規模な生物学データの探索的解釈に時間がかかる公衆衛生・疫学の研究チーム。
- データ整形や環境構築に専門家の時間が奪われている科学研究ワークフロー。
- 監査可能で解釈可能な結果が求められる規制・科学領域。
