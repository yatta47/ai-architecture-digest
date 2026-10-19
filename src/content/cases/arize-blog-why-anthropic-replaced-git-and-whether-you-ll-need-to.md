---
type: opinion
title: AnthropicのScionとGitの違いとエージェント時代のソース管理
title_original: Why Anthropic replaced Git, and whether you'll need to
company: Anthropic
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- ci-cd
components:
- Scion
- Git
- Arize AX
- Arize Phoenix
outcome:
  type: speed
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/anthropic-scion-vs-git/
published_at: '2026-10-19'
---

## 概要

Anthropicは1日3万件超のマージが発生するモノレポでGitをやめ、独自のソース管理Scionに移行した。1日約2,500万回のCIチェックアウトでGit通信量が膨大になる点が理由で、多くのチームはGitのままで足りるが、エージェント主体の開発ではソース管理、レビュー、CIのスケールが課題になると論じている。

## 設計のポイント

- Gitはclone時に全履歴を複製する前提で、人間のオフライン作業には向くがCI規模のチェックアウトでは高コストになる。
- エージェントは人間よりはるかに高速に動くため、マージ頻度が急増する。
- モノレポの規模が特殊なため、全チームが同じ壁に当たるとは限らない。

## 使いどころ

- AIコーディングエージェントでマージ数が急増している開発組織。
- CIのチェックアウトコストが問題になっている大規模モノレポ。
- エージェント時代のソース管理を検討する場面。
