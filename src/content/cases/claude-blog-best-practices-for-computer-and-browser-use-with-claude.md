---
type: guidance
title: Claudeでコンピュータ操作・ブラウザ操作エージェントを実装する際のベストプラクティス
title_original: Best practices for computer and browser use with Claude
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- prompt-optimization
components:
- Claude Computer Use API
- Claude Opus 4.7
- Claude Sonnet 4.6
- Claude Haiku 4.5
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
published_at: '2026-05-13'
---

## 概要

AnthropicがClaude 4.6ファミリーとOpus 4.7を対象に、コンピュータ操作・ブラウザ操作エージェントを実装する開発者向けのベストプラクティスを公開した。スクリーンショットをAPIの解像度上限に収まるよう事前にダウンスケールし、返却された座標を実画面解像度へ変換すること、メッセージ内でテキスト指示を画像より先に置くことがクリック精度向上の鍵だと説明している。

## 設計のポイント

- スクリーンショットはAPI内部の解像度上限(4.6系は長辺1568px/1.15MP、Opus 4.7は長辺2576px/3.75MP)に収まるよう事前にダウンスケールし、内部での自動縮小によるモデルの認識座標とハーネス側座標のずれを防ぐ
- 安全なデフォルトとして1280x720を使い、Opus 4.7では1080pを推奨。ソース画像のアスペクト比を保ったまま画素予算いっぱいまで使う『max API fit』計算も選択肢として提示する
- モデルが返す座標は送信した表示解像度(display_width_px/display_height_px)基準なので、実行前にscale_x/scale_yで実画面解像度へ変換してからクリックを実行する
- messagesのcontent配列ではテキスト指示をスクリーンショットより先に置くことで、モデルが何を探すべきか把握した状態で画像を処理でき、クリック精度が上がる

## 使いどころ

- Claudeでデスクトップ/ブラウザ操作を自動化するエージェント(RPA・E2Eテスト・レガシーアプリ操作)を実装する開発者
- マルチステップのGUI操作を伴うエージェント統合でクリック失敗率を下げたいプロダクトチーム
- Computer Use APIをプロダクションに組み込む際の解像度設計・座標変換の実装リファレンスとして
