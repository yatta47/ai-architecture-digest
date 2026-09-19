---
type: announcement
title: GitHub Copilotコードレビューのレビュー体験刷新
title_original: 'Copilot code review: An improved review experience'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Copilot code review
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience
published_at: '2026-09-18'
---

## 概要

GitHub Copilotのコードレビュー機能が、レビューの進捗を『未対応』『前回レビュー以降に解消』『見落とし』に分類して表示するようになり、コメントごとにタイトルが付くようになった。人間の返信内容を踏まえてコメントを自動解決するかどうかを判断し、Copilotの提案をバッチで適用した際にはコミットメッセージも自動生成する。

## 設計のポイント

- レビュー結果を『未対応』『解消済み』『見落とし』に分類し、差分プッシュのたびに進捗を保持したまま再レビューできるようにする
- 人間がコメントへ返信して対応不要と示した場合はその判断を尊重し、それ以外はコミット内容から自動的に解決理由（Won't Fix/Incorrect）を判定する
- 複数のCopilot提案をバッチで適用する際、変更内容から適切なコミットメッセージを自動生成する

## 使いどころ

- 多数のCopilotレビューコメントに埋もれず優先度の高い指摘から着手したい開発者
- レビューのたびに同じ指摘を何度も確認し直す手間を減らしたいチーム
