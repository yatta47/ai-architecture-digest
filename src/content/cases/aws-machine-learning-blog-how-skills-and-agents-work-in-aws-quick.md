---
type: guidance
title: AWS Quickにおけるエージェントとスキルの構成
title_original: How skills and agents work in AWS Quick
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
components:
- AWS Quick
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-skills-and-agents-work-in-aws-quick/
published_at: '2026-11-10'
---

## 概要

AWS Quickでエージェント、スキル、スペース(データ)、コネクタがどう組み合わさるかを解説し、チームで共有できるスキルの作り方を説明する。エージェントは指示に従い、必要なスキルを読み込み、コネクタで操作し、スペースやナレッジベースで回答を接地する。

## 設計のポイント

- 繰り返しタスクをスキルとして符号化し、エージェントが必要時にのみ読み込む。
- エージェントごとに指示・スペース・コネクタ・スキルを絞り、権限をユーザー権限の範囲に限定する。
- カスタムエージェントを公開してチームやグループで共有する。

## 使いどころ

- 週次報告やリリースノート作成など定型業務の標準化
- 部門固有のオンボーディング支援エージェントの展開
