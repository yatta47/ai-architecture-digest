---
type: guidance
title: Amazon QuickとfalをMCPで繋ぐ、承認ゲート付きのエージェント型クリエイティブワークフロー
title_original: Build agentic creative workflows with Amazon Quick and fal
industry: media
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
components:
- Amazon Quick
- fal
- Model Context Protocol (MCP)
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-agentic-creative-workflows-with-amazon-quick-and-fal/
published_at: '2026-08-27'
---

## 概要

クリエイティブチーム向けに、オーケストレーション層のAmazon Quickと1,000以上の生成メディアモデルを持つfalをMCPで接続し、ストーリーボード制作やミュージックビデオのコンセプト検証を1つのセッション内で完結させるエージェントハーネスを構成する。Amazon Quickの『Skills』に承認ゲートや作業手順を再利用可能な形でエンコードし、コンテキスト（スタイル・キャラクター設定など）を工程間で保持したまま生成・比較・修正を繰り返せる。

## 設計のポイント

- ワークフローのオーケストレーション（Amazon Quick）と専門特化した生成メディア処理（fal）をMCPという共通のツールインターフェースで疎結合にする
- 承認ゲートや作業手順を『Skills』として再利用可能な形で定義し、キャンペーンやチームをまたいで同じプロセスを再現できるようにする
- 工程間でスタイル選定・キャラクター参照・ストーリー展開などの承認済みコンテキストを保持し、生成のたびに手戻りが起きないようにする
- 各ステージの後に人間の承認を挟み、フル制作サイクルに入る前に方向性を確認できるようにする

## 使いどころ

- 複数の生成モデル（画像・音声・動画）を使い分けるクリエイティブ制作で、ツール間のコンテキスト受け渡しを自動化したいチーム
- ストーリーボードやコンセプト検証など、フル制作前の早い段階で方向性を素早く確認したい場合
- チームの標準的な制作プロセスや承認基準を『Skill』として再利用・共有したい制作会社
