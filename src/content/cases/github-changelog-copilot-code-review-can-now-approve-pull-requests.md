---
type: announcement
title: GitHub CopilotコードレビューがプルリクエストのAI承認判定に対応
title_original: Copilot code review can now approve pull requests
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Copilot
- GitHub Copilot code review
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests
published_at: '2026-09-01'
---

## 概要

GitHub Copilotのコードレビューが、プルリクエストが承認可能な状態かどうかを判定する「承認アセスメント」をレビューコメントに含めるようになった。管理者がエンタープライズ・組織・リポジトリの各レベルで許可した場合、Copilotは必須承認ルールにカウントされる承認自体を実行でき、新規コミットが来ると人間のレビュアーと同様に承認が取り消される。

## 設計のポイント

- AIによる承認はデフォルトで無効化し、有効化はエンタープライズ／組織／リポジトリの各階層で段階的に管理者が制御できるようにする。
- AIの承認済みステータスを新規コミットで自動的に無効化し、人間レビュアーと同じ整合性のあるレビュー状態管理を維持する。
- AIの判断（承認アセスメント）と実際の承認アクションを分離して提示し、権限付与前に人間が判断内容を確認できるようにする。
- 承認対象を特定のファイルパスに限定できるようにし、AIの自律性をスコープ限定で付与する。

## 使いどころ

- 定型的なプルリクエストのレビュー待ち時間を減らしたいが、重要な変更には人間の判断を残したい開発チーム。
- AI承認機能を全社一括ではなく組織・リポジトリ・ファイル単位で段階的に展開したい管理者。
- 既にCopilotのレビューコメントを活用しており、承認プロセスまでAIに拡張したいチーム。
