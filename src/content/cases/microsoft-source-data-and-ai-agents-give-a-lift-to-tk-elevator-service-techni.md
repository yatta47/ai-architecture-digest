---
type: case
title: 保守技術者を支援するブリーフィング／音声デブリーフ用AIエージェント
title_original: Data and AI agents give a lift to TK Elevator service technicians
company: TK Elevator
industry: manufacturing
cloud:
- azure
patterns:
- ai-agent
- voice-agent
- rag
components:
- Microsoft Foundry
- Azure OpenAI in Foundry Models
- Microsoft Azure
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/emea/features/data-and-ai-agents-give-a-lift-to-tk-elevator-service-technicians/
published_at: '2026-10-22'
---

## 概要

TK Elevatorは、現場の保守技術者向けにエージェント型AIアプリを構築した。訪問前に機器・作業内容・必要工具を端末で提示し、デジタルマニュアルや保守履歴も検索でき、作業後は音声エージェントが聞き取りで記録を作る。基盤は約10年かけて整備したコネクテッド機器データとクラウドである。

## 設計のポイント

- 訪問前のブリーフィングと訪問後の音声デブリーフを別エージェントに分け、現場の流れに合わせる。
- デブリーフで得た知見を履歴に蓄積し、他の技術者の次回作業で参照できるようにする。
- 機器データ・保守情報・技術文書をAzure上に統合した基盤の上にエージェントを載せる。

## 使いどころ

- 現場作業者が手書きメモやマニュアル検索に時間を取られている保守・点検業務。
- 世界中の作業知見を共有したい大規模サービス組織。
