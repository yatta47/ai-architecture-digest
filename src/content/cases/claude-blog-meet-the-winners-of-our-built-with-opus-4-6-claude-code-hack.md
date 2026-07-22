---
type: case
title: Claude Codeハッカソン優勝作品、非エンジニアが作るAI実務アプリ群
title_original: Meet the winners of our Built with Opus 4.6 Claude Code hackathon
company: CrossBeam
industry: public-sector
cloud:
- multi-cloud
patterns:
- ai-agent
- document-processing
components:
- Claude Code
- Opus 4.6
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon
published_at: '2026-04-20'
---

## 概要

Claude Codeを使ったOpus 4.6ハッカソンの優勝者を紹介する記事で、5人の優勝者のうち4人は非エンジニア。1位のCrossBeamは、カリフォルニア州の住宅建築許可申請が初回却下率90%超・平均半年遅延という「許可危機」に対し、AIで書類不備（署名漏れ・条例引用ミス・記入漏れ）を検出しボトルネックを解消するツールを構築した。

## 設計のポイント

- 専門知識を持つ非エンジニアがドメイン課題を定義し、Claude Codeで実装まで一気通貫に担う
- 行政手続きのような定型書類審査は、欠落項目や引用ミスの検出という具体的なチェックに絞ることで実用化しやすい

## 使いどころ

- 許可申請や行政書類のように、形式不備によるリジェクトが多い定型審査プロセスの効率化
- 専門職（弁護士・医師等）が自らの業務課題をAIエージェントで解決したい場合
