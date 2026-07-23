---
type: guidance
title: Realtimeモデル自身によるアウトオブバンド音声文字起こし
title_original: Transcribing User Audio with a Separate Realtime Request
industry: cross-industry
cloud: []
patterns:
- voice-agent
- realtime-transcription
- out-of-band-inference
components:
- OpenAI Realtime API
- gpt-4o-transcribe
- whisper-1
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/realtime_out_of_band_transcription/
published_at: '2025-11-20'
---

## 概要

OpenAIのRealtime APIでは音声応答生成と文字起こしを別モデル（gpt-4o-transcribe等）で行うため、発話内容と応答内容にズレが生じることがある。本記事は、同一のRealtimeセッション上でconversationを"none"に設定した2回目のresponse.createリクエストを送ることで、応答生成に使ったのと同じモデル・同じセッション文脈を使って高精度な文字起こしを得る手法を解説する。この手法はコストが増える一方、応答との整合性・文脈認識・指示追従性の面で優れる。

## 設計のポイント

- 同じWebSocketセッション上でconversationを"none"、output_modalitiesを["text"]に指定した2回目のresponse.createを送ることで、会話状態を汚さずに文字起こし専用の推論パスを分離する
- 音声応答生成用と文字起こし用でシステムプロンプトを分け、文字起こし用プロンプトは逐語性を重視した指示にチューニングする
- セッション全体の文脈を使うか直近の発話のみに絞るかで、精度とコスト（3〜22倍程度）のトレードオフを調整できる設計にする
- 文字起こし専用の出力は本会話に書き戻さないことで、ツール呼び出しや要約など下流処理への誤り伝播とコンテキスト汚染を防ぐ

## 使いどころ

- 音声エージェントの発話内容をツール呼び出しや構造化データ抽出のトリガーとして使う場合に、誤字による誤動作を防ぎたいとき
- 保険金請求受付や医療問診など、ユーザーへの表示や記録として正確な逐語トランスクリプトが必要な業務システム
- 文字起こしモデルと応答生成モデルの不一致（例:「otoo accident」のような誤認識）による顧客体験の劣化を避けたいカスタマーサポート音声AI
- 音声要約や背景でのバリデーション処理など、会話フローを止めずにアウトオブバンドで追加推論を行いたいケース
