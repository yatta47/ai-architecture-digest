---
type: guidance
title: JSON Schema厳格準拠でLLM出力の型安全性を保証するStructured Outputs
title_original: Structured Outputs guide
industry: cross-industry
cloud: []
patterns:
- structured-outputs
components:
- Responses API
- Chat Completions API
- Pydantic
- Zod
outcome:
  type: reliability
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses
published_at: '2025-07-18'
---

## 概要

Structured Outputsは、指定したJSON Schemaに常に一致する形でモデル出力を生成させる機能で、必須キーの欠落や不正なenum値の混入を防ぎ、Pythonなら Pydantic、JavaScriptならZodでスキーマをコードとして定義できる。ツール呼び出し用途にはfunction calling経由、応答本文の構造化にはresponse_format/text.format経由と使い分ける。

## 設計のポイント

- モデル・外部システム間を繋ぐならfunction calling、ユーザー向け応答自体を構造化したいならresponse_format/text.formatと用途で経路を使い分ける。
- PydanticやZodでスキーマをコード上の型として定義し、パース結果を直接オブジェクトとして受け取ることでバリデーション処理を省略する。
- 安全性起因の拒否をプログラムから判定できるexplicit refusalの仕組みを活用し、フォーマット不整合と意図的拒否を区別する。

## 使いどころ

- LLM出力をそのままアプリのデータモデルに流し込みたい、型安全性が重要なプロダクション用途。
- 従来JSONモードやプロンプト指示だけでフォーマットを担保していた箇所を、スキーマ強制に置き換えたい場合。
