---
type: announcement
title: Claude Codeがセッションの文脈から共有可能なライブWebページ「Artifacts」を生成する機能
title_original: Claude Code now supports artifacts
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
components:
- Claude Code
- Artifacts
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/artifacts-in-claude-code
published_at: '2026-06-18'
---

## 概要

Claude Codeのセッションが持つコードベース・接続先・会話の文脈全体から、PRウォークスルーやダッシュボード、インシデントページなどのインタラクティブなWebページ「Artifacts」を自動生成できるようになった。作業が進むたびに同じURLで新しいバージョンとして再公開されるため、チームは進行中の調査結果を毎回説明し直すことなく同じ画面を見ながら状況を共有できる。

## 設計のポイント

- 既存のデータソース接続やインフラ構築を必要とせず、セッションがすでに持っているコード・コネクタ・会話ログだけからページを組み立てる。
- 公開のたびに同一リンク上で新バージョンとして更新し、バージョン履歴からいつでも復元できるようにすることで、更新の追跡と巻き戻しを両立する。
- 作成者本人にのみ既定で非公開とし、組織内のみに共有範囲を限定するアクセス制御をデフォルトに据える。

## 使いどころ

- インシデント調査の進行状況を、スタンドアップのたびに口頭で説明し直す手間をなくしたいSRE・オンコール担当。
- PRやバグ修正のレビューを、差分と推論過程をまとめた1枚のページでレビュアーに追跡してもらいたいエンジニア。
- 依存関係のライセンス監査やコスト内訳など、リポジトリやIaCから機械的に導ける一覧をすぐに可視化したい法務・FinOps担当。
