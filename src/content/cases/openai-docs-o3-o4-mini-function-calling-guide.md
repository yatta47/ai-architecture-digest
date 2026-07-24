---
type: guidance
title: o3/o4-miniで関数呼び出し精度を上げるプロンプト設計ガイド
title_original: o3/o4-mini Function Calling Guide
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- o3
- o4-mini
- Responses API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide/
published_at: '2025-05-26'
---

## 概要

推論モデルo3/o4-miniのツール呼び出し性能を引き出すための開発者プロンプトと関数説明の書き方を解説する。ツール利用の境界条件明示、呼び出し順序の明示、関数descriptionへの使用条件記載など、誤発火を減らし精度を高める具体的なプラクティスを紹介する。

## 設計のポイント

- 開発者プロンプトでツールを使う/使わない境界条件を明示し、モデルの判断ぶれを減らす
- 高頻度かつ定型的なタスクでは関数呼び出しの順序をプロンプトで明示的に指定する
- 関数のdescriptionに使用条件や制約を書き込み、モデルとツールAPI間の恒久的なインターフェース契約として機能させる

## 使いどころ

- カスタマーサポートや発注処理など、複数ツールを正しい順序で確実に呼び出す必要があるエージェント開発
- 関数呼び出しの誤発火や過剰呼び出しを減らしたいプロダクションのツール利用エージェント
