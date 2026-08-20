---
type: announcement
title: LangSmith Preview Builds：PRごとに本番同等環境でエージェント変更を検証
title_original: 'LangSmith Preview Builds: Test agent changes before production'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ci-cd
- llmops
- eval
components:
- LangSmith
- LangSmith Deployment
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-preview-builds-test-agent-changes-before-production
published_at: '2026-08-20'
---

## 概要

LangSmithのPreview Buildsは、プルリクエストのブランチから一時的な本番同等のデプロイを自動生成し、マージ前にエージェントの挙動をチームで確認できる新機能。プロンプト・ツール・モデル・依存関係の変更による影響をローカルテストでは見えにくい形で可視化し、PMやドメインエキスパートなどコードを書かないレビュアーとも同じ環境を共有できる。

## 設計のポイント

- PRのソースブランチから親デプロイにリンクした隔離環境を作り、親デプロイを更新せずに変更後のエージェントをそのまま動かして検証する
- 新しいコミットがプッシュされるたびにプレビューデプロイメントの新リビジョンを自動生成し、レビュー中も常に最新の変更を反映し続ける
- Every PR/Label onlyのトリガー方式を選べるようにし、挙動レビューが必要な変更にだけプレビューを絞れるようにする
- アイドルTTLと同時実行数の上限でプレビュー環境のライフサイクルを管理し、信頼度の低い外部コントリビューターのPRには本番と別スコープの認証情報を使う

## 使いどころ

- プロンプト・ツール・モデルの変更がエージェントの挙動にどう影響するか、コードレビューだけでは分からないチーム
- PM・ドメインエキスパート・QAなどコードを書かない関係者にも変更後のエージェントを触ってレビューしてもらいたい場合
- 複数のPRを並行してレビューしており、共有ステージング環境を使い回すと変更が混線してしまう開発チーム
