---
type: announcement
title: 音声モードでOpusとSonnetを使い難問を考え抜く
title_original: Think through hard problems in voice mode
industry: cross-industry
cloud: []
patterns:
- voice-agent
- ai-agent
components:
- Claude Opus
- Claude Sonnet
- Claude Haiku
- Gmail
- Slack
- Google Calendar
- Canva
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/think-through-hard-problems-in-voice-mode
published_at: '2026-07-23'
---

## 概要

Claudeの音声モードが、これまでのHaiku限定からOpus・Sonnetでも動作するようになり、会話中にモデルを切り替えられるようになった。接続済みのGmailやSlackなどのツールも音声から直接操作でき、対応言語も大幅に拡大した。

## 設計のポイント

- 音声モードは選択中モデルの最速版を使い、テキストチャットと音声の間でモデル選択を引き継いで会話を途切れさせない
- ツール利用の実行前には必ず許可を求める設計とし、話す(思考)から実行(ツール操作)への移行に人の確認を挟む
- 言語設定は音声モード専用で保持し、テキスト側の言語設定を自動的には引き継がない

## 使いどころ

- 商談や意思決定前に考えを声に出して整理し、フィードバックを得たいビジネスパーソン
- 会話から派生したタスク(カレンダー調整やメール下書き)をそのまま音声から実行したい場合
