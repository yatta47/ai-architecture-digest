---
type: announcement
title: 開発者コンソールのプロンプト自動改善機能
title_original: Improve your prompts in the developer console
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
components:
- Anthropic Console
- Workbench
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/prompt-improver
published_at: '2024-10-14'
---

## 概要

Anthropic Consoleに、既存プロンプトをChain-of-Thought追加や例の標準化・強化、書き直し、プレフィル追加などの手法で自動改善するprompt improverを追加した。マルチラベル分類タスクで精度を30%向上させ、要約タスクでは文字数制約の遵守率を100%まで引き上げた。

## 設計のポイント

- Chain-of-Thought挿入・例のXML標準化・プレフィル追加など複数の改善手法を組み合わせてプロンプトを自動リライトする
- 改善後のプロンプトに対してユーザーがフィードバックを与え反復改善できるようにする
- few-shot例をワークベンチ上で構造化管理しinput/outputペアとして編集可能にする

## 使いどころ

- 他のモデル向けに書かれたプロンプトをClaude向けに移植したい場合
- プロンプトエンジニアリング初心者が品質の高いプロンプトを短時間で作りたい場合
