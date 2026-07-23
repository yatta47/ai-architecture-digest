---
type: guidance
title: Claude Codeのフック機能でエージェント動作を自動制御・検証する設計
title_original: 'Claude Code power user customization: How to configure hooks'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- guardrails
- human-in-the-loop
components:
- Claude Code
- Prettier
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-to-configure-hooks
published_at: '2025-12-11'
---

## 概要

Claude Codeにはツール実行の前後やセッション開始・終了などのタイミングで任意のシェルコマンドを発火させる「フック」機能があり、PreToolUse・PermissionRequest・PostToolUse・PreCompact・SessionStart・Stop・SubagentStop・UserPromptSubmitの8種類のイベントで自動化ができる。手動でのフォーマッタ実行や繰り返しの権限承認、毎回のコンテキスト貼り付けといった摩擦を、JSON設定でイベント・マッチャー・実行コマンドを紐づけることで解消する。危険なコマンドのブロックやファイルパス検証などのガードレールも、フックにより毎回確実に適用できる。

## 設計のポイント

- ツールが実際に実行される前(PreToolUse)と権限ダイアログが出る前(PermissionRequest)を分離し、危険操作のブロックと定型操作の自動承認をそれぞれ別のフェーズで扱う
- matcherでツール名やコマンドパターン(例: Bash(npm test*))を絞り込み、対象を限定したピンポイントな自動化を可能にする
- PostToolUseでファイル書き込み直後にフォーマッタやリンタを自動実行し、コード品質チェックを人手の記憶に依存させない仕組みにする
- PreCompactやSessionStartのフックでコンテキスト圧縮前のバックアップや、セッション開始時のgit状態・TODO注入を行い、エージェントが持つ状況認識を継続的に補強する

## 使いどころ

- 毎回同じフォーマッタ実行やnpm testの権限承認を繰り返している開発者が、定型作業をフックに委譲したい場面
- rm -rfや強制pushなど危険なコマンドを未然にブロックし、プロジェクト固有のルールを常に強制したいチーム
- セッションごとにスプリント方針やgitステータスなどのコンテキストを手動で貼り付けるのをやめ、自動注入したい場合
- コンテキスト圧縮で重要な意思決定が失われる前に、トランスクリプトを自動バックアップしておきたい長時間セッションの運用
