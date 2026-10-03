---
type: announcement
title: Claude CodeをTypeScriptで拡張する「mods」
title_original: Customize Claude Code with mods
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- policy-as-code
components:
- Claude Code
- TypeScript
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-code-mods
published_at: '2026-10-01'
---

## 概要

Claude Codeの動作とUIを変更する小さなTypeScript関数「mods」が発表された。イベントの前後や代替として動き、プロンプト書き換え、ツール呼び出しの遮断・再試行、権限判断、秘密情報のマスクなどができる。プラグインとして配布でき、サンドボックスは無いため信頼できる提供元のみ導入する。

## 設計のポイント

- エージェントの各イベントにフックし、前・後・代替・ラップのいずれでも介入できる。
- 複数のmodは読み込み順に積み重ねられ、別作者のものを組み合わせられる。
- ツール出力から秘密情報を除去してからモデルに渡せる。

## 使いどころ

- Claude Codeの挙動をチーム向けに統制・カスタマイズしたい開発組織。
- 権限承認やログのマスキングなどの運用ルールをコード化したい場面。
