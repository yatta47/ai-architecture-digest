---
type: announcement
title: Claudeが日常アプリ（AllTrails・Instacart等）と連携するコネクタを拡充
title_original: New connectors in Claude for everyday life
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
components:
- Claude
- AllTrails
- Instacart
- Audible
- Tripadvisor
- Intuit TurboTax
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/connectors-for-everyday-life
published_at: '2026-04-23'
---

## 概要

Claudeのコネクタが仕事用ツールに加え、AllTrails・Instacart・Booking.comなど200以上の日常アプリに拡大した。会話の文脈から適切なアプリを動的に提案し、複数の候補がある場合はユーザーに選ばせる仕組みで、広告や有料掲載なしに提案を行う。

## 設計のポイント

- 会話の文脈とユーザーの好みからClaude自身が適切なコネクタを動的に提案する
- 複数アプリが候補になり得る場合は両方を提示し、選択権をユーザーに残す
- 広告や有料掲載を排除し、提案順位はユーザーにとっての有用性のみで決める

## 使いどころ

- 旅行の予約や外食・買い物など、複数の日常サービスを一つの会話の中で横断的に使いたい場面
- 1つの会話内で複数アプリを連携させて成果物を作りたいプロダクトマネージャーなどの業務利用
