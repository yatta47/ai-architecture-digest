---
type: announcement
title: GitHub Copilot in Visual Studio 8月アップデート(組織カスタムエージェント・モデル制御・レビューエージェント)
title_original: GitHub Copilot in Visual Studio — August update
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-model-routing
- prompt-optimization
components:
- GitHub Copilot
- Visual Studio
- Git agent
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-28-github-copilot-in-visual-studio-august-update-2
published_at: '2026-08-28'
---

## 概要

GitHub Copilot for Visual Studioの8月アップデートで、組織/エンタープライズ管理者がリポジトリ横断でカスタムエージェントを公開・共有できる機能、モデルごとの思考の深さ(Low/Medium/High)を切り替えるthinking effort制御、お気に入りモデルのピン留めやコンテキストウィンドウ・コスト情報を確認できるモデル管理ビューが追加された。さらにGitエージェントがコミット前の未コミット変更やコミット単位のレビューをエディタ内にインラインで表示し、Copilot Chatでそのまま議論を継続できるようになった。

## 設計のポイント

- 組織単位でカスタムエージェントを公開し、エディタ側が自動検出してピッカーに出所(組織)付きで表示することで、チーム標準のワークフローを横断的に再利用できるようにする
- モデルの思考の深さ(Low/Medium/High)をタスクごとに切り替え可能にし、単純作業と複雑な設計判断とでトークン消費と推論品質のバランスを使い分けられるようにする
- コードレビューをPR作成前のローカルなGitエージェント呼び出しとして組み込み、指摘をインラインリストで可視化してチャットで深掘りできる導線にする

## 使いどころ

- 組織全体でCopilotの使い方やカスタムエージェントを標準化したいエンタープライズ開発チーム
- PRを出す前にコミット単位でセルフレビューを済ませ、レビュー往復を減らしたい開発者
