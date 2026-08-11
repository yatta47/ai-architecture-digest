---
type: announcement
title: GitHub Copilot利用レポートにモデル別トークン内訳を追加
title_original: Per-model token breakdown in the usage report
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-11-per-model-token-breakdown-in-the-usage-report
published_at: '2026-08-11'
---

## 概要

GitHub Copilotの利用レポートに、モデルごとの入力・出力・キャッシュ読み書きトークン数をAI creditsの消費量と並べて表示する機能が追加された。従来はAI creditsの消費量だけが表示されトークンの内訳が見えなかったため、課金の説明や削減余地の特定が難しかった。管理者はBilling設定のAI usageページからレポートをダウンロードして確認できる。

## 設計のポイント

- AIクレジットのような抽象的な課金単位を、入力/出力/キャッシュ読み書きトークンという解釈可能な単位に分解して提示する
- モデル単位の内訳を持たせることで、モデル選択とコストの関係を可視化する

## 使いどころ

- AIクレジット消費の内訳をモデル単位・トークン種別単位で説明責任者やステークホルダーに示したい管理者
- キャッシュ読み書きトークンの比率を見てコスト削減余地を特定したいチーム
