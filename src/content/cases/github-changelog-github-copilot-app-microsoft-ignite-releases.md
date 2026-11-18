---
type: announcement
title: GitHub CopilotアプリがAzure DevOps・ブラウザ操作に対応
title_original: GitHub Copilot app, Microsoft Ignite releases
company: GitHub
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- ci-cd
components:
- GitHub Copilot app
- Azure DevOps
- GitHub Enterprise Server
- Browser use
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-17-github-copilot-app-microsoft-ignite-releases
published_at: '2026-11-17'
---

## 概要

GitHub CopilotアプリがAzure DevOpsリポジトリ（公開プレビュー）、GitHub Enterprise Server、ブラウザ操作に対応した。エージェントがブランチ作成からPR、CI失敗修正、agent mergeまで進められ、ブラウザ操作は分離タブグループで実行される。

## 設計のポイント

- エージェントのブラウザ操作を分離タブグループに閉じ込める。
- Azure DevOpsのポリシー通過後にagent mergeを行う。

## 使いどころ

- Azure DevOpsやGHESを使う企業でPR作業をエージェント化したいチーム。
