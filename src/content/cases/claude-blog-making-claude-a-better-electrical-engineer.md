---
type: case
title: Diode Computersとの協業でClaudeの回路基板設計能力を強化
title_original: Making Claude a better electrical engineer
company: Diode Computers
industry: manufacturing
cloud: []
patterns:
- ai-agent
- eval
- fine-tuning
- human-in-the-loop
components:
- Claude Code
- Claude Sonnet 4.5
- Claude Opus 4.1
- Zener
- pcb
- KiCad
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/making-claude-a-better-electrical-engineer
published_at: '2025-12-12'
---

## 概要

Diode Computersは、チップのデータシートから回路基板（PCB）のリファレンス設計をZener言語で自動生成するためにClaude Codeを利用している。AnthropicはDiodeの電気エンジニアと協業し、成果を高レベル要件で採点するカスタムテストベンチを用いてSonnet 4.5以降のClaudeモデルの訓練を改善した。ブラインドの比較評価では、DiodeのエンジニアがSonnet 4.5の設計をOpus 4.1やSonnet 4より高い割合で選好した。

## 設計のポイント

- 成功・失敗基準が明確に定義できるエージェントタスクは、ドメイン専門家との協業によってモデルの訓練自体を改善できる
- 個別部品の有無を厳密に判定するのではなく「静電容量22uF以上」のような高レベル要件でテストベンチを設計し、過度に厳格な採点を避ける
- エージェントにはファイル読み書き・bash実行・コンパイラなど最小限のツールのみを与え、ドキュメント読解から成果物生成までを一貫して行わせる
- 自動生成した設計は人間のエンジニアがレビューしてから採用するヒューマン・イン・ザ・ループ運用とする

## 使いどころ

- 深い専門知識が必要かつ成功・失敗基準が明確なドメインタスクを持つ企業
- 大量の技術ドキュメントから構造化された成果物（回路図やコンフィグ等）を自動生成したい設計チーム
- 特定分野でのLLM精度向上のためにモデル提供元との協業を検討している企業
