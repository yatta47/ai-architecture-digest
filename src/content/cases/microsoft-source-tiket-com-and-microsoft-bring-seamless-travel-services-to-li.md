---
type: case
title: tiket.comが構築した旅行カスタマーサポート向けマルチエージェントAI「CRATER」
title_original: Tiket.com and Microsoft bring seamless travel services to life with AI
company: tiket.com
industry: other
cloud:
- azure
patterns:
- ai-agent
- multi-agent-orchestration
- multi-model-routing
- guardrails
components:
- Microsoft Foundry
- Microsoft AutoGen
- Azure OpenAI Service
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/asia/2026/07/14/tiket-com-and-microsoft-bring-seamless-travel-services-to-life-with-ai/
published_at: '2026-07-17'
---

## 概要

インドネシアの旅行OTA tiket.comが、Microsoft Foundry上にマルチエージェント方式の顧客対応AI「CRATER」を構築し、予約状況確認や返金処理などをアプリ内の自然言語対話だけで完結できるようにした事例。導入後は月間の対応件数が約10,000件から75,000件超へと650%増加し、姉妹施策の「halo tiket」は問い合わせの87%を自動化してCSAT 84.6%を達成した。

## 設計のポイント

- Microsoft Foundryのモデルカタログからユースケースごとに最適なLLMを選択し、特定ベンダーへのロックインを避ける
- Microsoft AutoGenによるマルチエージェントオーケストレーションで、予約・支払い・返金など複数のリアルタイム業務システムに接続する
- Foundry AI Guardrailsを全ての本番インタラクションに適用し、安全ポリシーを一貫して強制する
- カスタマーサービス・CX・プロダクト・技術・デザイン・データサイエンスの部門横断チームで開発し、単一のアプリ内会話でチャネル切替なく完結させる

## 使いどころ

- 問い合わせ内容が予約変更・返金・追加サービスなど多岐にわたるカスタマーサポートを、チャネルをまたがず1つの会話で解決したい事業者
- 問い合わせ急増（数十倍規模）に人員増なしでスケールさせたいカスタマーサービス部門
- ベンダーロックインを避けつつ用途ごとに異なるLLMを使い分けたいエンタープライズAI基盤担当者
