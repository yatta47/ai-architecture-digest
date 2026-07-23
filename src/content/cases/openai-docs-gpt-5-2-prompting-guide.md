---
type: guidance
title: GPT-5.2のエンタープライズ向けプロンプティングガイド
title_original: GPT-5.2 Prompting Guide
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- context-engineering
- guardrails
components:
- GPT-5.2
- GPT-5.1
- /responses/compact
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide/
published_at: '2025-12-11'
---

## 概要

OpenAIのGPT-5.2はエンタープライズ・エージェント用途向けの最新フラッグシップモデルで、GPT-5.1比で指示追従性やトークン効率が向上している。本ガイドは出力の冗長性制御、スコープドリフト防止、長文コンテキストでの再グラウンディング、曖昧なクエリへの対処など、本番導入で効果的なプロンプトパターンを紹介する。長時間・多ツールのワークフロー向けに会話状態を圧縮するcompactエンドポイントについても解説している。

## 設計のポイント

- 出力の長さや形式は具体的な文字数・箇条書き数のタグで明示的に制約する
- スコープドリフトを防ぐため「要求された範囲のみを実装する」制約ブロックを明示し、勝手な機能追加やスタイル変更を禁止する
- 1万トークンを超える長文入力では、要約→制約の再確認→セクション引用という手順で回答をグラウンディングする
- 曖昧・情報不足なクエリには明確化の質問か複数解釈の提示を促し、高リスク領域では回答前の自己チェックを組み込む

## 使いどころ

- コーディング・文書解析・金融など複雑なエージェントワークフローを本番運用する開発者
- 長時間実行かつ多数のツール呼び出しを伴うエージェントでコンテキスト制限に直面するシステム
- 法務・金融など高リスク領域で過信した誤答や不正確な数値の生成を防ぎたい用途
