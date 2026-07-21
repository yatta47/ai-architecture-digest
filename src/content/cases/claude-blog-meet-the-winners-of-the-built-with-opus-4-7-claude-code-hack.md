---
type: case
title: 医療教育・電子修理・CS教育、ハッカソン優勝作品に見るClaude Codeの実践パターン
title_original: Meet the winners of the Built with Opus 4.7 Claude Code hackathon
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- eval
components:
- Claude Code
- Claude Managed Agents
- Claude Opus 4.7
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon
published_at: '2026-06-15'
---

## 概要

Claude Opus 4.7ハッカソンの優勝作品を紹介。医療研修シミュレーター「Medkit」は患者対応をエージェントがグレーディングし、電子修理支援「Wrench Board」は複数エージェントを並列実行して基板の故障箇所を診断し、CS教育IDE「Maieutic」は生徒に仕様を言語化させるまでコーディングを止める設計で『考えずにコードを生成する』問題に対処している。

## 設計のポイント

- 音声エンジン・コンテンツ生成・3Dゲーム層・コアアプリなど機能ごとに別々のClaude Codeセッションを分け、各コンテキストをクリーンに保ちながら並行開発する
- 設計フェーズで責務（デザイン・データ取り込み・診断エージェントなど）を分割し、それぞれ仕様書とプランを作ってからマルチエージェントモードで実行する
- 診断や採点を行うエージェントには、人間の専門家が使うのと同じ評価基準（臨床ガイドライン等）を明示的に与えて判定させる
- 生徒が仕様を精緻に言語化するまでコード編集をロックし、自動補完に頼らせないことで『考える』ステップを強制する

## 使いどころ

- 限られた期間で野心的なエージェント型システムを立ち上げたい個人開発者やスタートアップ
- AIに考えさせず、学習者自身に問題を言語化・検証させたい教育ツール開発者
